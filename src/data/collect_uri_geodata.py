"""
Uri WMS Geodata Collector

Downloads geospatial data from Kanton Uri WMS service.
Creates ML-ready datasets from geographic features.

WMS URL: https://geo.ur.ch/wms
WFS URL: https://geo.ur.ch/wfs (for feature data)

Usage:
    python src/data/collect_uri_geodata.py --layer baumkataster
    python src/data/collect_uri_geodata.py --layer alpen
    python src/data/collect_uri_geodata.py --all-layers
"""

import requests
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import json
import time


# =============================================================================
# Configuration
# =============================================================================

WMS_BASE_URL = "https://geo.ur.ch/wms"
WFS_BASE_URL = "https://geo.ur.ch/wfs"

# Available layers from WMS GetCapabilities
URI_LAYERS = {
    "baumkataster": {
        "name": "weitere:baumkataster",
        "title": "Baumkataster (Tree Cadastre)",
        "description": "Individual trees with species, age, health",
        "type": "point",
        "ml_use": "classification, regression"
    },
    "alpen": {
        "name": "landwirtschaft:alpen_inkl_weideperimeter",
        "title": "Alpen inkl. Weideperimeter",
        "description": "Alpine pastures and grazing areas",
        "type": "polygon",
        "ml_use": "clustering, land use classification"
    },
    "agriflaechen": {
        "name": "landwirtschaft:ala_agrigis_flaechenanzeige_group",
        "title": "ALA Agrigis Flächen",
        "description": "Agricultural land parcels",
        "type": "polygon",
        "ml_use": "land use prediction"
    },
    "bodenbedeckung": {
        "name": "av:ch055_bodenbedeckung_flaechen",
        "title": "Bodenbedeckung Flächen",
        "description": "Land cover (buildings, roads, water, forest)",
        "type": "polygon",
        "ml_use": "image segmentation, classification"
    },
    "einzelobjekte": {
        "name": "av:ch056_einzelobjekte_flaechen",
        "title": "Einzelobjekte Flächen",
        "description": "Individual objects (small features)",
        "type": "polygon",
        "ml_use": "object detection"
    },
    "biotope": {
        "name": "raumplanung:ch023_uebrige_biotope_flaechen",
        "title": "Übrige Biotope",
        "description": "Protected biotopes and natural areas",
        "type": "polygon",
        "ml_use": "habitat suitability, conservation"
    },
    "amphibien": {
        "name": "raumplanung:ch029_amphibienlaichgebiete",
        "title": "Amphibienlaichgebiete",
        "description": "Amphibian breeding areas",
        "type": "polygon",
        "ml_use": "species habitat modeling"
    },
    "agglomassnahmen": {
        "name": "raumplanung:are_agglopgrogramm_massnahmen",
        "title": "Agglomerationsprogramm Massnahmen",
        "description": "Urban development measures",
        "type": "point",
        "ml_use": "urban planning analysis"
    }
}

# Bounding box for Uri canton (approximate)
URI_BBOX = {
    "minx": 8.403448,
    "miny": 46.525247,
    "maxx": 8.964656,
    "maxy": 46.994909
}


class UriGeodataCollector:
    """Collect geospatial data from Kanton Uri WMS/WFS."""
    
    def __init__(self, base_dir: Optional[Path] = None):
        self.base_dir = base_dir or Path(__file__).parent.parent.parent
        self.raw_dir = self.base_dir / "data" / "raw" / "uri_geodata"
        self.processed_dir = self.base_dir / "data" / "processed"
        
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)
    
    def get_wfs_features(self, layer_name: str, bbox: Dict = None) -> Dict:
        """
        Fetch features from WFS service.
        
        Args:
            layer_name: WFS layer name
            bbox: Bounding box dict with minx, miny, maxx, maxy
            
        Returns:
            GeoJSON FeatureCollection
        """
        print(f"\n🗺️  Fetching WFS features for layer: {layer_name}")
        
        # WFS GetFeature request
        params = {
            "service": "WFS",
            "version": "2.0.0",
            "request": "GetFeature",
            "typeName": layer_name,
            "outputFormat": "application/json",
            "srsName": "EPSG:4326"
        }
        
        # Add bounding box if provided
        if bbox:
            params["bbox"] = f"{bbox['minx']},{bbox['miny']},{bbox['maxx']},{bbox['maxy']},EPSG:4326"
        
        try:
            response = requests.get(WFS_BASE_URL, params=params, timeout=30)
            response.raise_for_status()
            
            geojson = response.json()
            
            print(f"   ✅ Retrieved {len(geojson.get('features', []))} features")
            
            return geojson
            
        except Exception as e:
            print(f"   ⚠️  Error: {e}")
            print(f"   💡 Trying alternative method...")
            
            # Fallback: Try WMS GetMap (returns image, not features)
            return self._get_wms_map(layer_name, bbox)
    
    def _get_wms_map(self, layer_name: str, bbox: Dict = None) -> Dict:
        """
        Fallback: Get map image from WMS (not ideal for ML).
        
        Args:
            layer_name: WMS layer name
            bbox: Bounding box
            
        Returns:
            Dict with metadata (no features)
        """
        print(f"   ⚠️  WFS not available, using WMS metadata only")
        
        # WMS GetMap request (returns image)
        params = {
            "service": "WMS",
            "version": "1.3.0",
            "request": "GetMap",
            "layers": layer_name,
            "crs": "EPSG:4326",
            "bbox": f"{bbox['miny']},{bbox['minx']},{bbox['maxy']},{bbox['maxx']}" if bbox else "46.525247,8.403448,46.994909,8.964656",
            "width": 800,
            "height": 600,
            "format": "image/png"
        }
        
        try:
            response = requests.get(WMS_BASE_URL, params=params, timeout=30)
            response.raise_for_status()
            
            # Save map image
            image_file = self.raw_dir / f"{layer_name.replace(':', '_')}_map.png"
            with open(image_file, 'wb') as f:
                f.write(response.content)
            
            print(f"   ✅ Map image saved: {image_file}")
            
            return {"type": "FeatureCollection", "features": [], "metadata": "WMS image only"}
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return {"type": "FeatureCollection", "features": []}
    
    def geojson_to_dataframe(self, geojson: Dict, layer_name: str) -> pd.DataFrame:
        """
        Convert GeoJSON to pandas DataFrame for ML.
        
        Args:
            geojson: GeoJSON FeatureCollection
            layer_name: Name of the layer
            
        Returns:
            DataFrame with features and properties
        """
        print(f"\n📊 Converting GeoJSON to DataFrame...")
        
        features = geojson.get('features', [])
        
        if not features:
            print(f"   ⚠️  No features found")
            return pd.DataFrame()
        
        # Extract properties from features
        rows = []
        for feature in features:
            props = feature.get('properties', {})
            geom = feature.get('geometry', {})
            
            # Add geometry info
            if geom.get('type') == 'Point':
                props['geometry_type'] = 'point'
                props['longitude'] = geom.get('coordinates', [None, None])[0]
                props['latitude'] = geom.get('coordinates', [None, None])[1]
            elif geom.get('type') == 'Polygon':
                props['geometry_type'] = 'polygon'
                # Calculate centroid for polygons
                coords = geom.get('coordinates', [[]])[0]
                if coords:
                    props['longitude'] = sum(c[0] for c in coords) / len(coords)
                    props['latitude'] = sum(c[1] for c in coords) / len(coords)
            
            props['layer'] = layer_name
            rows.append(props)
        
        df = pd.DataFrame(rows)
        
        print(f"   ✅ Created DataFrame with {len(df)} rows, {len(df.columns)} columns")
        print(f"   Columns: {', '.join(df.columns[:10])}{'...' if len(df.columns) > 10 else ''}")
        
        return df
    
    def download_all_layers(self) -> Dict[str, pd.DataFrame]:
        """
        Download all available layers.
        
        Returns:
            Dict of layer_name -> DataFrame
        """
        print("\n🇨🇭 Downloading ALL Uri geodata layers...")
        
        all_data = {}
        
        for layer_id, layer_info in URI_LAYERS.items():
            print(f"\n{'='*60}")
            print(f"Layer: {layer_info['title']}")
            print(f"{'='*60}")
            
            # Fetch features
            geojson = self.get_wfs_features(layer_info['name'], URI_BBOX)
            
            # Convert to DataFrame
            df = self.geojson_to_dataframe(geojson, layer_id)
            
            if len(df) > 0:
                # Save to file
                file_path = self.raw_dir / f"uri_{layer_id}.csv"
                df.to_csv(file_path, index=False)
                print(f"   💾 Saved to: {file_path}")
                
                all_data[layer_id] = df
            
            # Be nice to API
            time.sleep(1)
        
        return all_data
    
    def create_ml_dataset(self, layer_data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
        """
        Create combined ML-ready dataset from multiple layers.
        
        Args:
            layer_data: Dict of layer DataFrames
            
        Returns:
            Combined DataFrame for ML
        """
        print("\n🤖 Creating ML-ready dataset...")
        
        # For now, just return the layer with most features
        # In production, you'd combine layers spatially
        
        if not layer_data:
            print("   ⚠️  No data to combine")
            return pd.DataFrame()
        
        # Find layer with most features
        best_layer = max(layer_data.keys(), key=lambda k: len(layer_data[k]))
        df = layer_data[best_layer]
        
        print(f"   ✅ Using layer: {best_layer} ({len(df)} features)")
        
        # Add derived features for ML
        if 'longitude' in df.columns and 'latitude' in df.columns:
            # Distance from center of Uri
            uri_center_lat = 46.76
            uri_center_lon = 8.68
            df['dist_from_center'] = np.sqrt(
                (df['latitude'] - uri_center_lat)**2 + 
                (df['longitude'] - uri_center_lon)**2
            )
        
        # Add target variable placeholder
        df['ml_target'] = 0  # To be defined based on use case
        
        # Save ML-ready dataset
        ml_file = self.processed_dir / "uri_geodata_ml_ready.csv"
        df.to_csv(ml_file, index=False)
        print(f"   💾 ML dataset saved: {ml_file}")
        
        return df
    
    def generate_report(self, layer_data: Dict[str, pd.DataFrame]):
        """Generate summary report."""
        print("\n" + "="*60)
        print("📊 URI GEODATA SUMMARY")
        print("="*60)
        
        total_features = sum(len(df) for df in layer_data.values())
        
        print(f"\n🗺️  Layers Downloaded: {len(layer_data)}")
        print(f"📈 Total Features: {total_features:,}")
        
        print(f"\n📋 Layer Details:")
        for layer_id, df in layer_data.items():
            info = URI_LAYERS.get(layer_id, {})
            print(f"\n   {info.get('title', layer_id)}:")
            print(f"      Features: {len(df):,}")
            print(f"      Columns: {len(df.columns)}")
            print(f"      ML Use: {info.get('ml_use', 'N/A')}")
        
        print("\n" + "="*60)
        
        # Save report
        report_file = self.processed_dir / "uri_geodata_summary.txt"
        with open(report_file, 'w') as f:
            f.write("URI GEODATA SUMMARY\n")
            f.write("="*60 + "\n\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n\n")
            f.write(f"Total layers: {len(layer_data)}\n")
            f.write(f"Total features: {total_features:,}\n\n")
            
            for layer_id, df in layer_data.items():
                f.write(f"\n{layer_id}:\n")
                f.write(df.describe().to_string() + "\n")
        
        print(f"📄 Report saved to: {report_file}")


def main():
    """Main data collection pipeline."""
    print("🇨🇭 Uri WMS Geodata Collector")
    print("="*60)
    
    collector = UriGeodataCollector()
    
    # Download all layers
    layer_data = collector.download_all_layers()
    
    if layer_data:
        # Create ML dataset
        ml_df = collector.create_ml_dataset(layer_data)
        
        # Generate report
        collector.generate_report(layer_data)
        
        print("\n🚀 Next Steps:")
        print("   1. Review downloaded data in data/raw/uri_geodata/")
        print("   2. Open notebooks/02_uri_geodata_exploration.ipynb")
        print("   3. Build geospatial ML models!")
        
        print("\n✅ Data collection complete!")
    else:
        print("\n⚠️  No data downloaded - check API availability")
        print("   💡 Try manual download from: https://geo.ur.ch")


if __name__ == "__main__":
    main()
