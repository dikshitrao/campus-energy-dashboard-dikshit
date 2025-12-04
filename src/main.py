from ingestion import read_and_combine
from aggregation import *
from visualize import create_dashboard
from models import MeterReading, BuildingManager
import pandas as pd

def main():

    df = read_and_combine("data")
    if df.empty:
        print("No data available.")
        return

    daily = calculate_daily_totals(df)
    weekly = calculate_weekly_aggregates(df)
    summary = building_wise_summary(df)

    summary.to_csv("output/building_summary.csv")
    df.to_csv("output/cleaned_energy_data.csv")

    manager = BuildingManager()
    for _, row in df.iterrows():
        manager.add_reading(row['building'], MeterReading(row['timestamp'], row['kwh']))

    with open("output/summary.txt", "w") as f:
        f.write("TOTAL CAMPUS CONSUMPTION: " + str(df['kwh'].sum()) + "\n")
        f.write("HIGHEST CONSUMPTION BUILDING: " + df.groupby('building')['kwh'].sum().idxmax() + "\n")
        f.write("PEAK LOAD TIME: " + str(df.loc[df['kwh'].idxmax(), 'timestamp']) + "\n")

    create_dashboard(daily, weekly, df)

    print("ALL DONE! Check output folder.")

if __name__ == "__main__":
    main()
