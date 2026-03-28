"""
Download REAL Swiss Accident & Weather Data

This script downloads:
1. Accident data from BFS (Bundesamt für Statistik)
2. Weather data from Open-Meteo API (real historical data)

Then merges them by week and canton for ML training.

Usage:
    python src/data/download_real_data.py --years 2020 2021 2022 2023 2024
"""

import requests
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
import time
import json


# =============================================================================
# Configuration
# =============================================================================

CANTON_COORDINATES = {
    "ZH": {"lat": 47.3769, "lon": 8.5417, "name": "Zürich"},
    "BE": {"lat": 46.9480, "lon": 7.4474, "name": "Bern"},
    "LU": {"lat": 47.0502, "lon": 8.3093, "name": "Luzern"},
    "UR": {"lat": 46.8807, "lon": 8.6279, "name": "Uri"},
    "SZ": {"lat": 47.0003, "lon": 8.6524, "name": "Schwyz"},
    "OW": {"lat": 46.8219, "lon": 8.2517, "name": "Obwalden"},
    "NW": {"lat": 46.9264, "lon": 8.3859, "name": "Nidwalden"},
    "GL": {"lat": 47.0404, "lon": 9.0680, "name": "Glarus"},
    "ZG": {"lat": 47.1660, "lon": 8.5155, "name": "Zug"},
    "FR": {"lat": 46.8058, "lon": 7.1623, "name": "Freiburg"},
    "SO": {"lat": 47.2079, "lon": 7.5374, "name": "Solothurn"},
    "BS": {"lat": 47.5596, "lon": 7.5886, "name": "Basel-Stadt"},
    "BL": {"lat": 47.4814, "lon": 7.7302, "name": "Basel-Landschaft"},
    "SH": {"lat": 47.6972, "lon": 8.6344, "name": "Schaffhausen"},
    "AR": {"lat": 47.3667, "lon": 9.2833, "name": "Appenzell Ausserrhoden"},
    "AI": {"lat": 47.3167, "lon": 9.4167, "name": "Appenzell Innerrhoden"},
    "SG": {"lat": 47.4245, "lon": 9.3767, "name": "St. Gallen"},
    "GR": {"lat": 46.8480, "lon": 9.4722, "name": "Graubünden"},
    "AG": {"lat": 47.3919, "lon": 8.2476, "name": "Aargau"},
    "TG": {"lat": 47.5515, "lon": 9.0554, "name": "Thurgau"},
    "TI": {"lat": 46.3317, "lon": 8.8003, "name": "Tessin"},
    "VD": {"lat": 46.5197, "lon": 6.6323, "name": "Waadt"},
    "VS": {"lat": 46.2333, "lon": 7.5333, "name": "Wallis"},
    "NE": {"lat": 47.0000, "lon": 6.9333, "name": "Neuenburg"},
    "GE": {"lat": 46.2044, "lon": 6.1432, "name": "Genf"},
    "JU": {"lat": 47.3500, "lon": 7.1500, "name": "Jura"}
}

# BFS accident data direct download URLs (when available)
# Note: BFS requires manual download from PX-Web for full dataset
BFS_DOWNLOAD_URLS = {
    'pxweb': 'https://www.pxweb.bfs.admin.ch/pxweb/de/px-x-1106010100_103/',
    'opendata': 'https://opendata.swiss/de/dataset/verkehrsunfalle'
}


class RealDataDownloader:
    """Download real Swiss accident and weather data."""
    
    def __init__(self, base_dir: Optional[Path] = None):
        self.base_dir = base_dir or Path(__file__).parent.parent.parent
        self.raw_dir = self.base_dir / "data" / "raw"
        self.processed_dir = self.base_dir / "data" / "processed"
        
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)
    
    def download_bfs_accident_data_manual(self) -> bool:
        """
        Guide user through manual BFS data download.
        
        Returns:
            True if data found, False if manual download needed
        """
        print("\n🇨🇭 Swiss BFS Accident Data Download")
        print("="*60)
        
        # Check if manual download exists
        manual_file = self.raw_dir / "accidents_bfs_manual.csv"
        
        if manual_file.exists():
            print(f"✅ Found existing BFS data: {manual_file}")
            return True
        
        print("\n⚠️  BFS data requires manual download (no direct API)")
        print("\n📋 Step-by-step instructions:")
        print("\n1. Go to BFS PX-Web:")
        print("   https://www.pxweb.bfs.admin.ch/pxweb/de/px-x-1106010100_103/")
        print("\n2. Select variables:")
        print("   - Strassenart (Road type): Alle")
        print("   - Unfallschwere (Severity): Alle")
        print("   - Kanton (Canton): Alle 26 Kantone")
        print("   - Jahr (Year): 2020, 2021, 2022, 2023, 2024")
        print("\n3. Click 'Tabelle anzeigen' (Show table)")
        print("\n4. Download:")
        print("   - Click 'Download' button")
        print("   - Select 'CSV' format")
        print("   - Save as: accidents_bfs_manual.csv")
        print(f"\n5. Move file to: {self.raw_dir}/")
        print("\n💡 Alternative: Check opendata.swiss for pre-packaged datasets")
        print("   https://opendata.swiss/de/dataset/verkehrsunfalle-2021")
        
        return False
    
    def download_accident_data_from_opendata(self, years: List[int]) -> pd.DataFrame:
        """
        Try to download from opendata.swiss (if available).
        
        Args:
            years: Years to download
            
        Returns:
            DataFrame with accident data or empty DataFrame
        """
        print(f"\n🔍 Checking opendata.swiss for years {years}...")
        
        all_data = []
        
        for year in years:
            # Try opendata.swiss URL
            url = f"https://opendata.swiss/dataset/verkehrsunfalle-{year}/resource/download"
            
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    # Save to file
                    file_path = self.raw_dir / f"accidents_{year}.csv"
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    
                    print(f"✅ Downloaded {year}: {file_path}")
                    
                    # Load into DataFrame
                    df = pd.read_csv(file_path)
                    all_data.append(df)
                else:
                    print(f"⚠️  {year} not available on opendata.swiss")
                    
            except Exception as e:
                print(f"⚠️  Error downloading {year}: {e}")
        
        if all_data:
            return pd.concat(all_data, ignore_index=True)
        else:
            print("\n⚠️  No data available from opendata.swiss")
            return pd.DataFrame()
    
    def download_weather_data(self, cantons: List[str], years: List[int]) -> pd.DataFrame:
        """
        Download REAL weather data from Open-Meteo API.
        
        Args:
            cantons: Canton codes
            years: Years to download
            
        Returns:
            DataFrame with real weather data
        """
        print(f"\n🌤️  Downloading REAL weather data from Open-Meteo...")
        print(f"   Cantons: {len(cantons)}")
        print(f"   Years: {', '.join(map(str, years))}")
        
        all_weather = []
        
        for canton in cantons:
            coords = CANTON_COORDINATES[canton]
            print(f"\n   Processing {canton} ({coords['name']})...")
            
            for year in years:
                weather_df = self._fetch_weather_for_year(
                    coords['lat'], coords['lon'], canton, year
                )
                
                if len(weather_df) > 0:
                    all_weather.append(weather_df)
                
                # Be nice to API
                time.sleep(0.3)
        
        if all_weather:
            weather_df = pd.concat(all_weather, ignore_index=True)
            
            # Save to file
            weather_file = self.raw_dir / f"weather_real_{'-'.join(map(str, years))}.csv"
            weather_df.to_csv(weather_file, index=False)
            print(f"\n✅ Weather data saved: {weather_file}")
            print(f"   Total records: {len(weather_df):,}")
            
            return weather_df
        else:
            print("\n❌ Failed to download weather data")
            return pd.DataFrame()
    
    def _fetch_weather_for_year(self, lat: float, lon: float, 
                                 canton: str, year: int) -> pd.DataFrame:
        """Fetch weather for one canton and year."""
        
        # Use Open-Meteo API (different endpoint)
        url = "https://archive-api.open-meteo.com/v1/era5"
        
        params = {
            "latitude": lat,
            "longitude": lon,
            "start_date": f"{year}-01-01",
            "end_date": f"{year}-12-31",
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,"
                     "snowfall_sum,weather_code,wind_speed_10m_max",
            "timezone": "Europe/Zurich"
        }
        
        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            # Convert to DataFrame
            df = pd.DataFrame({
                'date': pd.to_datetime(data['daily']['time']),
                'canton': canton,
                'temp_max': data['daily']['temperature_2m_max'],
                'temp_min': data['daily']['temperature_2m_min'],
                'precipitation': data['daily']['precipitation_sum'],
                'snowfall': data['daily']['snowfall_sum'],
                'weather_code': data['daily']['weather_code'],
                'wind_speed': data['daily']['wind_speed_10m_max']
            })
            
            # Add weather description
            weather_codes = {
                0: "Clear sky",
                1: "Mainly clear",
                2: "Partly cloudy",
                3: "Overcast",
                61: "Rain",
                71: "Snow",
                95: "Thunderstorm"
            }
            df['weather_condition'] = df['weather_code'].map(weather_codes)
            
            return df
            
        except Exception as e:
            print(f"      ⚠️  Error: {e}")
            return pd.DataFrame()
    
    def create_aggregated_dataset(self, accidents: pd.DataFrame, 
                                   weather: pd.DataFrame) -> pd.DataFrame:
        """Merge accident and weather data by week and canton."""
        
        print("\n📊 Aggregating data by week and canton...")
        
        # Add week column to weather
        weather['week'] = pd.to_datetime(weather['date']).dt.isocalendar().week
        weather['year'] = pd.to_datetime(weather['date']).dt.year
        
        # Aggregate accidents by week/canton
        if 'date' in accidents.columns:
            accidents['week'] = pd.to_datetime(accidents['date']).dt.isocalendar().week
            accidents['year'] = pd.to_datetime(accidents['date']).dt.year
            
            accident_agg = accidents.groupby(['year', 'week', 'canton']).agg({
                'date': 'count'
            }).reset_index()
            accident_agg.columns = ['year', 'week', 'canton', 'total_accidents']
        else:
            print("⚠️  Accident data missing date column")
            return pd.DataFrame()
        
        # Aggregate weather
        weather_agg = weather.groupby(['year', 'week', 'canton']).agg({
            'temp_max': 'mean',
            'temp_min': 'mean',
            'precipitation': 'sum',
            'snowfall': 'sum',
            'weather_code': lambda x: x.mode().iloc[0] if len(x) > 0 else 0,
            'wind_speed': 'mean'
        }).reset_index()
        
        weather_agg.columns = ['year', 'week', 'canton',
                               'avg_temp_max', 'avg_temp_min', 
                               'total_precipitation', 'total_snowfall',
                               'dominant_weather', 'avg_wind_speed']
        
        # Merge
        merged = accident_agg.merge(weather_agg, on=['year', 'week', 'canton'], 
                                   how='inner')
        
        # Add target variable
        merged['high_accident_week'] = (
            merged['total_accidents'] > merged['total_accidents'].median()
        ).astype(int)
        
        # Save
        processed_file = self.processed_dir / "accidents_weather_real_aggregated.csv"
        merged.to_csv(processed_file, index=False)
        print(f"✅ Aggregated data saved: {processed_file}")
        print(f"   Records: {len(merged):,}")
        
        return merged


def main():
    """Main download pipeline."""
    print("🇨🇭 Swiss Real Data Downloader")
    print("="*60)
    
    downloader = RealDataDownloader()
    
    years = [2020, 2021, 2022, 2023, 2024]
    cantons = list(CANTON_COORDINATES.keys())
    
    # Step 1: Try to download accident data
    print("\n" + "="*60)
    print("Step 1: Accident Data")
    print("="*60)
    
    accidents = pd.DataFrame()
    
    # Try opendata.swiss first
    accidents = downloader.download_accident_data_from_opendata(years)
    
    if accidents.empty:
        # Fall back to manual download instructions
        if not downloader.download_bfs_accident_data_manual():
            print("\n⚠️  Using sample data temporarily")
            print("   Please download real BFS data when ready!")
            return
    
    # Step 2: Download weather data
    print("\n" + "="*60)
    print("Step 2: Weather Data")
    print("="*60)
    
    weather = downloader.download_weather_data(cantons, years)
    
    if weather.empty:
        print("\n❌ Weather download failed")
        return
    
    # Step 3: Aggregate
    print("\n" + "="*60)
    print("Step 3: Merge & Aggregate")
    print("="*60)
    
    if len(accidents) > 0 and len(weather) > 0:
        merged = downloader.create_aggregated_dataset(accidents, weather)
        
        print("\n" + "="*60)
        print("✅ REAL DATA DOWNLOAD COMPLETE!")
        print("="*60)
        print(f"\n📊 Dataset Summary:")
        print(f"   Accident records: {len(accidents):,}")
        print(f"   Weather records: {len(weather):,}")
        print(f"   Aggregated (week×canton): {len(merged):,}")
        print(f"\n📁 Files:")
        print(f"   Raw: {downloader.raw_dir}")
        print(f"   Processed: {downloader.processed_dir}")
        print(f"\n🚀 Ready for ML training!")
    else:
        print("\n⚠️  Incomplete data - check errors above")


if __name__ == "__main__":
    main()
