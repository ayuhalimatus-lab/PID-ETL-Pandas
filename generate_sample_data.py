import pandas as pd
import numpy as np
import os

os.makedirs("data", exist_ok=True)
np.random.seed(42)
dates = pd.date_range(start="2026-01-01", periods=100, freq="h")

# 1. CSV Main
df_main = pd.DataFrame({
    "timestamp": dates,
    "sensor_id": "S101",
    "location": " Lab Utama ",
    "temperature_celsius": np.random.uniform(20, 35, 100),
    "humidity_percent": np.random.uniform(40, 80, 100),
    "pressure_hpa": np.random.uniform(1000, 1020, 100),
    "air_quality_aqi": np.random.randint(20, 150, 100),
    "status": "ACTIVE"
})
df_main.loc[5, "temperature_celsius"] = 99.9
df_main.to_csv("data/sensor_data_main.csv", index=False)

# 2. CSV Semicolon
df_semi = pd.DataFrame({
    "timestamp": dates,
    "sensor_id": "S102",
    "location": "ruang server",
    "temperature_celsius": np.random.uniform(18, 28, 100),
    "humidity_percent": np.random.uniform(30, 60, 100),
    "pressure_hpa": np.random.uniform(1000, 1020, 100),
    "air_quality_aqi": np.random.randint(10, 80, 100),
    "status": "active"
})
df_semi.to_csv("data/sensor_data_semicolon.csv", sep=";", index=False)

# 3. Excel Multi-sheet
with pd.ExcelWriter("data/sensor_data_monthly.xlsx") as writer:
    df_main.to_excel(writer, sheet_name="Jan2026", index=False)
    df_semi.to_excel(writer, sheet_name="Feb2026", index=False)

print("Data sampel berhasil dibuat di folder data/")
