import os
import numpy as np
import pandas as pd
from pathlib import Path

# Set up output folder
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Simulate ride data
np.random.seed(42)
n = 1000

df = pd.DataFrame({
    "ride_id": range(1, n+1),
    "pickup_lat": np.random.uniform(40.70, 40.85, n),
    "pickup_lon": np.random.uniform(-74.05, -73.85, n),
    "dropoff_lat": np.random.uniform(40.70, 40.85, n),
    "dropoff_lon": np.random.uniform(-74.05, -73.85, n),
    "timestamp": pd.date_range("2024-01-01", periods=n, freq="min"),
    "passengers": np.random.randint(1, 5, n),
    "fare_amount": np.round(np.random.uniform(5, 50, n), 2)
})

df.to_csv(DATA_DIR / "uber_rides.csv", index=False)
print("✓ uber_rides.csv saved in /data")
