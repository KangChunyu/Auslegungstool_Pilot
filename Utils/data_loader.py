import pandas as pd
import os

def load_standard_profile(csv_path: str = "data\Standardlastprofil.csv") -> dict:
    """
    Load a single standard profile CSV file and split it into separate
    time series DataFrames for each column (excluding timestamp).
    
    Returns:
        {
            "L00 [kW]": DataFrame,
            "L00 [kWh]": DataFrame,
            ...
        }
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"File not found: {csv_path}")
    
    # Combine date and time into a single timestamp column
    df = pd.read_csv(csv_path, parse_dates=[[0, 1]], dayfirst=True)
    df.rename(columns={df.columns[0]: "timestamp"}, inplace=True)

    # Extract each time series separately
    return {
        col: df[["timestamp", col]].copy()
        for col in df.columns if col != "timestamp"
    }
