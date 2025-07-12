import pandas as pd
import plotly.express as px
from pathlib import Path

# Load data
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
df = pd.read_csv(DATA_DIR / "uber_rides.csv", parse_dates=["timestamp"])

# Create time histogram
fig1 = px.histogram(df, x="timestamp", nbins=50, title="Ride Volume Over Time")

# Create scatter map of pickups
fig2 = px.scatter_mapbox(
    df, lat="pickup_lat", lon="pickup_lon", color="fare_amount",
    size="passengers", zoom=10, height=500,
    mapbox_style="carto-positron",
    title="Pickup Locations Colored by Fare"
)

# Create bar chart of average fare by passenger count
fig3 = px.bar(
    df.groupby("passengers")["fare_amount"].mean().reset_index(),
    x="passengers", y="fare_amount",
    title="Average Fare by Passenger Count"
)

# Save as HTML
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_DIR / "golden_image.html", "w") as f:
    f.write(fig1.to_html(full_html=False))
    f.write(fig2.to_html(full_html=False))
    f.write(fig3.to_html(full_html=False))

print("✓ Dashboard written to outputs/golden_image.html")
