"""
Swiss Accident Data Collector - WORKING VERSION

Creates sample accident and weather data for ML training.
Aggregates by week and canton for prediction tasks.

Usage:
    python src/data/collect_accident_data.py
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import List, Dict
import json


# Swiss canton coordinates
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

# Weather codes
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear", 
    2: "Partly cloudy",
    3: "Overcast",
    61: "Rain",
    71: "Snow",
    95: "Thunderstorm"
}


def create_sample_accident_data(years: List[int]) -> pd.DataFrame:
    """Create realistic synthetic accident data."""
    print(f"🧪 Creating sample accident data for {years}...")
    
    np.random.seed(42)
    all_data = []
    
    for year in years:
        n_accidents = 5000
        
        # Dates with seasonal pattern (more accidents in winter/summer)
        dates = pd.date_range(f"{year}-01-01", f"{year}-12-31", periods=n_accidents)
        
        # Canton weights (by population)
        canton_weights = np.array([
            15, 12, 8, 2, 3, 1, 1, 1, 3, 5, 5, 4, 5, 2, 1, 1, 5, 4, 8, 3, 6, 9, 5, 2, 4, 1
        ])
        canton_weights = canton_weights / canton_weights.sum()
        cantons = np.random.choice(list(CANTON_COORDINATES.keys()), 
                                   size=n_accidents, p=canton_weights)
        
        # Severity
        severities = np.random.choice(
            ['light', 'serious', 'fatal'], 
            size=n_accidents,
            p=[0.85, 0.13, 0.02]
        )
        
        # Road conditions (weather-correlated)
        months = pd.to_datetime(dates).month
        road_conditions = []
        for month in months:
            if month in [12, 1, 2]:  # Winter
                road_conditions.append(np.random.choice(['dry', 'wet', 'icy', 'snow'], p=[0.3, 0.2, 0.2, 0.3]))
            elif month in [6, 7, 8]:  # Summer
                road_conditions.append(np.random.choice(['dry', 'wet', 'icy', 'snow'], p=[0.7, 0.28, 0.01, 0.01]))
            else:
                road_conditions.append(np.random.choice(['dry', 'wet', 'icy', 'snow'], p=[0.5, 0.4, 0.05, 0.05]))
        
        df = pd.DataFrame({
            'date': dates,
            'canton': cantons,
            'severity': severities,
            'road_condition': road_conditions,
            'vehicle_type': np.random.choice(
                ['car', 'motorcycle', 'truck', 'bicycle'],
                size=n_accidents, p=[0.70, 0.10, 0.10, 0.10]
            ),
            'road_type': np.random.choice(
                ['highway', 'main_road', 'side_road'],
                size=n_accidents, p=[0.20, 0.40, 0.40]
            )
        })
        
        df['week'] = df['date'].dt.isocalendar().week
        df['year'] = df['date'].dt.year
        df['day_of_week'] = df['date'].dt.day_name()
        df['month'] = df['date'].dt.month
        
        all_data.append(df)
    
    result_df = pd.concat(all_data, ignore_index=True)
    print(f"✅ Created {len(result_df):,} accident records")
    
    return result_df


def create_sample_weather_data(cantons: List[str], years: List[int]) -> pd.DataFrame:
    """Create realistic synthetic weather data."""
    print(f"🌤️  Creating sample weather data for {len(cantons)} cantons...")
    
    np.random.seed(43)
    all_data = []
    
    for canton in cantons:
        coords = CANTON_COORDINATES[canton]
        
        for year in years:
            # Daily data for full year
            dates = pd.date_range(f"{year}-01-01", f"{year}-12-31", freq='D')
            n_days = len(dates)
            
            # Temperature (seasonal + canton variation)
            month = dates.month
            base_temp = 10 + 15 * np.sin(2 * np.pi * (month - 3) / 12)  # Seasonal
            if coords['lat'] > 47:  # Northern cantons cooler
                base_temp -= 2
            if canton in ['TI']:  # Tessin warmer
                base_temp += 3
            if canton in ['VS', 'GR', 'UR']:  # Alpine cantons
                base_temp -= 5
            
            temp_max = base_temp + np.random.normal(0, 3, n_days)
            temp_min = temp_max - 8 - np.random.normal(0, 2, n_days)
            
            # Precipitation
            precipitation = np.random.exponential(2, n_days)
            precipitation[precipitation > 50] = 50  # Cap extreme values
            
            # Snow (winter months, temperature dependent)
            snowfall = np.zeros(n_days)
            winter_mask = (month.isin([12, 1, 2])) & (temp_max < 2)
            snowfall[winter_mask] = np.random.exponential(5, winter_mask.sum())
            
            # Snow depth (accumulates)
            snow_depth = np.cumsum(snowfall) - np.cumsum(np.where(temp_max > 0, 2, 0))
            snow_depth = np.maximum(0, snow_depth)
            
            # Weather codes
            weather_code = np.zeros(n_days, dtype=int)
            rain_mask = precipitation > 1
            snow_mask = (precipitation > 0.5) & (temp_max < 0)
            weather_code[rain_mask] = 61
            weather_code[snow_mask] = 71
            
            df = pd.DataFrame({
                'date': dates,
                'canton': canton,
                'temp_max': temp_max.round(1),
                'temp_min': temp_min.round(1),
                'precipitation': precipitation.round(1),
                'snowfall': snowfall.round(1),
                'snow_depth': snow_depth.round(0),
                'weather_code': weather_code,
                'wind_speed': np.random.exponential(10, n_days).round(1),
            })
            
            df['weather_condition'] = df['weather_code'].map(WEATHER_CODES)
            df['week'] = df['date'].dt.isocalendar().week
            df['year'] = df['date'].dt.year
            
            all_data.append(df)
    
    result_df = pd.concat(all_data, ignore_index=True)
    print(f"✅ Created {len(result_df):,} weather records")
    
    return result_df


def aggregate_by_week_canton(accidents: pd.DataFrame, 
                              weather: pd.DataFrame) -> pd.DataFrame:
    """Aggregate data by week and canton for ML."""
    print("\n📊 Aggregating by week and canton...")
    
    # Aggregate accidents
    accident_agg = accidents.groupby(['year', 'week', 'canton']).agg({
        'date': 'count',
        'severity': lambda x: (x == 'fatal').sum(),
        'road_condition': lambda x: (x == 'wet').sum() + (x == 'icy').sum() + (x == 'snow').sum(),
    }).reset_index()
    
    accident_agg.columns = ['year', 'week', 'canton', 
                            'total_accidents', 'fatal_accidents', 'bad_road_accidents']
    
    # Aggregate weather
    weather_agg = weather.groupby(['year', 'week', 'canton']).agg({
        'temp_max': 'mean',
        'temp_min': 'mean',
        'precipitation': 'sum',
        'snowfall': 'sum',
        'snow_depth': 'mean',
        'weather_code': lambda x: x.mode().iloc[0] if len(x) > 0 else 0,
        'wind_speed': 'mean'
    }).reset_index()
    
    weather_agg.columns = ['year', 'week', 'canton',
                           'avg_temp_max', 'avg_temp_min', 'total_precipitation',
                           'total_snowfall', 'avg_snow_depth', 'dominant_weather',
                           'avg_wind_speed']
    
    # Merge
    merged = accident_agg.merge(weather_agg, on=['year', 'week', 'canton'], how='inner')
    
    # Target variable: high accident week?
    merged['high_accident_week'] = (
        merged['total_accidents'] > merged['total_accidents'].median()
    ).astype(int)
    
    print(f"✅ Aggregated dataset: {len(merged):,} records")
    print(f"   Features: {', '.join(merged.columns)}")
    
    return merged


def generate_report(df: pd.DataFrame, processed_dir: Path):
    """Generate dataset summary report."""
    print("\n" + "="*60)
    print("📊 DATASET SUMMARY")
    print("="*60)
    
    print(f"\n📅 Time Period: {df['year'].min()} - {df['year'].max()}")
    print(f"🇨🇭 Cantons: {df['canton'].nunique()}")
    print(f"📈 Total Records: {len(df):,}")
    
    print(f"\n🚗 Accident Stats:")
    print(f"   Total accidents: {df['total_accidents'].sum():,}")
    print(f"   Fatal accidents: {df['fatal_accidents'].sum():,}")
    print(f"   Avg per week/canton: {df['total_accidents'].mean():.1f}")
    
    print(f"\n🌤️  Weather Stats:")
    print(f"   Avg temp (max): {df['avg_temp_max'].mean():.1f}°C")
    print(f"   Avg temp (min): {df['avg_temp_min'].mean():.1f}°C")
    print(f"   Total precipitation: {df['total_precipitation'].sum():.0f}mm")
    print(f"   Total snowfall: {df['total_snowfall'].sum():.0f}cm")
    
    print(f"\n🎯 Target Distribution:")
    high_acc = (df['high_accident_week'] == 1).sum()
    low_acc = (df['high_accident_week'] == 0).sum()
    print(f"   High accident weeks: {high_acc} ({high_acc/len(df)*100:.1f}%)")
    print(f"   Low accident weeks: {low_acc} ({low_acc/len(df)*100:.1f}%)")
    
    print("\n" + "="*60)
    
    # Save report
    report_file = processed_dir / "dataset_summary.txt"
    with open(report_file, 'w') as f:
        f.write("DATASET SUMMARY\n")
        f.write("="*60 + "\n\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n\n")
        f.write(df.describe().to_string())
    
    print(f"📄 Report saved to: {report_file}")


def main():
    """Main data generation pipeline."""
    print("🇨🇭 Swiss Car Accident Data Generator")
    print("="*60)
    
    # Setup
    base_dir = Path(__file__).parent.parent.parent
    raw_dir = base_dir / "data" / "raw"
    processed_dir = base_dir / "data" / "processed"
    
    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"📁 Raw: {raw_dir}")
    print(f"📁 Processed: {processed_dir}")
    
    # Configuration
    years = [2020, 2021, 2022, 2023, 2024]
    cantons = list(CANTON_COORDINATES.keys())
    
    # Generate data
    accidents = create_sample_accident_data(years)
    weather = create_sample_weather_data(cantons, years)
    
    # Save raw data
    accidents_file = raw_dir / f"accidents_sample_{'-'.join(map(str, years))}.csv"
    accidents.to_csv(accidents_file, index=False)
    print(f"\n✅ Accidents saved: {accidents_file}")
    
    weather_file = raw_dir / f"weather_sample_{'-'.join(map(str, years))}.csv"
    weather.to_csv(weather_file, index=False)
    print(f"✅ Weather saved: {weather_file}")
    
    # Aggregate
    aggregated = aggregate_by_week_canton(accidents, weather)
    
    # Save processed data
    processed_file = processed_dir / "accidents_weather_aggregated.csv"
    aggregated.to_csv(processed_file, index=False)
    print(f"\n✅ Aggregated data saved: {processed_file}")
    
    # Generate report
    generate_report(aggregated, processed_dir)
    
    print("\n🚀 Next Steps:")
    print("   1. Open notebooks/01_data_exploration.ipynb")
    print("   2. Start EDA and feature engineering")
    print("   3. Build your first ML model!")
    
    print("\n✅ Data generation complete!")


if __name__ == "__main__":
    main()
