import pandas as pd
from pathlib import Path

def read_and_combine(data_dir="data"):
    data_path = Path(data_dir)
    all_files = list(data_path.glob("*.csv"))

    if not all_files:
        print("No CSV files found in /data/")
        return pd.DataFrame()

    df_list = []

    for file in all_files:
        try:
            df = pd.read_csv(file, on_bad_lines='skip')
            df['building'] = file.stem.split('_')[0]
            df_list.append(df)
        except Exception as e:
            print(f"Error reading {file.name}: {e}")

    df_combined = pd.concat(df_list, ignore_index=True)

    df_combined['timestamp'] = pd.to_datetime(df_combined['timestamp'])
    df_combined.sort_values(by='timestamp', inplace=True)

    return df_combined
