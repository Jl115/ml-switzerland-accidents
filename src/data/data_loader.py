"""
Data Loader - Load and Manage Switzerland Accident & Weather Data

LEARNING GOALS:
- File I/O operations (CSV, JSON)
- Error handling with try/except
- Data validation basics
- Working with paths (pathlib)

TODO: Implement each function following the comments
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import json


class DataLoader:
    """
    Load accident and weather data from various sources.
    
    Attributes:
        raw_dir (Path): Directory for raw data files
        processed_dir (Path): Directory for processed data
        external_dir (Path): Directory for external data
    """
    
    def __init__(self, base_dir: Optional[Path] = None):
        """
        Initialize DataLoader with directory paths.
        
        Args:
            base_dir: Base project directory (default: current dir)
            
        TODO: Set up directory paths for raw, processed, external data
        TODO: Create directories if they don't exist
        """
        # TODO: Set self.base_dir = base_dir or Path('.')
        # TODO: Set self.raw_dir, self.processed_dir, self.external_dir
        # TODO: Create directories with mkdir(parents=True, exist_ok=True)
        pass
    
    def load_csv(self, filename: str, directory: str = 'raw') -> pd.DataFrame:
        """
        Load a CSV file into a pandas DataFrame.
        
        Args:
            filename: Name of CSV file
            directory: Subdirectory ('raw', 'processed', or 'external')
            
        Returns:
            DataFrame with loaded data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            
        TODO: Implement CSV loading with error handling
        TODO: Use appropriate pandas parameters (encoding, sep, etc.)
        
        Example:
            >>> loader = DataLoader()
            >>> df = loader.load_csv('accidents_2023.csv')
        """
        # TODO: Build full path: self.{directory}_dir / filename
        # TODO: Try to load with pd.read_csv()
        # TODO: Handle FileNotFoundError with clear message
        # TODO: Handle encoding errors (try utf-8, latin-1)
        # TODO: Print shape of loaded data
        pass
    
    def load_accident_data(self, year: int) -> pd.DataFrame:
        """
        Load accident data for a specific year.
        
        Args:
            year: Year to load (e.g., 2023)
            
        Returns:
            DataFrame with accident records
            
        TODO: Implement loading of Swiss accident data
        TODO: Expected columns: date, canton, location, severity, vehicle_type
        TODO: Validate that required columns exist
        
        Hint:
            Data might come from BFS (Bundesamt für Statistik)
        """
        # TODO: Construct filename: f'accidents_{year}.csv'
        # TODO: Load the CSV file
        # TODO: Check for required columns
        # TODO: Print number of records loaded
        pass
    
    def load_weather_data(self, canton: str, year: int) -> pd.DataFrame:
        """
        Load weather data for a specific canton and year.
        
        Args:
            canton: Canton code (e.g., 'ZH', 'BE', 'LU')
            year: Year to load
            
        Returns:
            DataFrame with weather records
            
        TODO: Implement loading of Swiss weather data
        TODO: Expected columns: date, temperature, precipitation, 
                snow_depth, wind_speed, weather_condition
        TODO: Validate canton code is valid
        
        Hint:
            Data might come from MeteoSwiss
        """
        # TODO: Validate canton code (see resources/swiss_cantons.json)
        # TODO: Construct filename: f'weather_{canton}_{year}.csv'
        # TODO: Load the CSV file
        # TODO: Check for required columns
        pass
    
    def merge_accident_weather(self, accidents: pd.DataFrame, 
                                weather: pd.DataFrame) -> pd.DataFrame:
        """
        Merge accident and weather data on date and canton.
        
        Args:
            accidents: Accident DataFrame
            weather: Weather DataFrame
            
        Returns:
            Merged DataFrame with both accident and weather data
            
        TODO: Implement merge operation
        TODO: Merge on date and canton columns
        TODO: Handle missing values (inner vs outer join)
        TODO: Check for duplicate rows after merge
        
        Example:
            >>> merged = loader.merge_accident_weather(accidents_df, weather_df)
            >>> print(merged.columns)
            ['date', 'canton', 'accidents', 'temperature', 'precipitation', ...]
        """
        # TODO: Use pd.merge() with appropriate 'on' parameter
        # TODO: Decide on join type (inner, outer, left, right)
        # TODO: Check for duplicates with duplicated().sum()
        # TODO: Print merge result shape
        pass
    
    def save_dataframe(self, df: pd.DataFrame, filename: str, 
                      directory: str = 'processed') -> None:
        """
        Save DataFrame to CSV file.
        
        Args:
            df: DataFrame to save
            filename: Output filename
            directory: Target subdirectory
            
        TODO: Implement saving with error handling
        TODO: Use index=False for CSV export
        TODO: Create directory if it doesn't exist
        """
        # TODO: Build full path
        # TODO: Create directory if needed
        # TODO: Save with df.to_csv(index=False)
        # TODO: Print confirmation message
        pass
    
    def get_data_info(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Get summary information about a DataFrame.
        
        Args:
            df: DataFrame to analyze
            
        Returns:
            Dictionary with shape, columns, dtypes, missing values
            
        TODO: Implement data summary
        TODO: Include: shape, columns, dtypes, null counts, memory usage
        
        Example:
            >>> info = loader.get_data_info(df)
            >>> print(f"Records: {info['n_records']}")
            >>> print(f"Missing values: {info['missing']}")
        """
        # TODO: Return dict with:
        #   - n_records: len(df)
        #   - n_columns: len(df.columns)
        #   - columns: list(df.columns)
        #   - dtypes: df.dtypes.to_dict()
        #   - missing: df.isnull().sum().to_dict()
        #   - memory: df.memory_usage(deep=True).sum()
        pass


# =============================================================================
# EXERCISES
# =============================================================================

"""
EXERCISE 1: Basic File Loading
-------------------------------
1. Create a sample CSV file with accident data (5-10 rows)
2. Load it using load_csv()
3. Print the shape and first few rows

EXERCISE 2: Data Validation
---------------------------
1. Add a method validate_columns(df, required_cols)
2. Check if all required columns exist
3. Raise ValueError with clear message if missing

EXERCISE 3: Multiple File Loading
----------------------------------
1. Create load_all_years(start_year, end_year)
2. Load data for multiple years
3. Concatenate into single DataFrame
4. Add 'year' column to track source

EXERCISE 4: Data Exploration
-----------------------------
1. Use get_data_info() on loaded data
2. Find which columns have missing values
3. Calculate percentage of missing data per column
"""
