import pandas as pd
import requests
from io import StringIO
import os
import io


def download_nasa_power_global():
    """Fixed NASA POWER global download for EV analysis"""
    os.makedirs("data", exist_ok=True)

    # URL for daily global representative data
    url_daily = "https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,T2M_MAX,T2M_MIN,RH2M,WS10M,PRECTOTCORR&community=RE&longitude=0&latitude=0&start=19810101&end=20251231&format=CSV"

    print("📥 Downloading NASA POWER Global Daily Data...")
    response = requests.get(url_daily)
    response.raise_for_status()

    # Fix: Skip NASA metadata lines properly
    lines = response.text.splitlines()
    data_start = None

    # Find actual data start (after metadata)
    for i, line in enumerate(lines):
        if line.startswith('YEAR') and ',' in line:
            data_start = i
            break

    if data_start is None:
        raise ValueError("No data found in NASA response")

    # Parse only data lines
    csv_data = '\n'.join(lines[data_start:])
    df = pd.read_csv(StringIO(csv_data))

    # Clean and save
    df.columns = df.columns.str.strip()
    df['DATE'] = pd.to_datetime(df['YEAR'].astype(str) +
                                df['MO'].astype(str).str.zfill(2) +
                                df['DY'].astype(str).str.zfill(2), format='%Y%m%d')

    save_path = "data/nasa_power_global_daily.csv"
    df.to_csv(save_path, index=False)

    print(f"✅ SUCCESS! {len(df):,} days downloaded to {save_path}")
    print("\n📊 Sample data:")
    print(df[['DATE', 'T2M', 'T2M_MAX', 'T2M_MIN', 'RH2M']].tail())

    return df


if __name__ == "__main__":
    download_nasa_power_global()