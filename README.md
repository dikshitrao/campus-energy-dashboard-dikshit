campus-energy-dashboard-dikshit
Project Overview

Course: Programming for Problem Solving using Python
Assignment: End-to-End Energy Consumption Analysis and Visualization
Author: dikshit

This project builds a Campus Energy-Use Dashboard to help analyze electricity consumption across campus buildings. It ingests raw meter data, performs aggregation and analysis, generates visualizations, and outputs summary reports.

#Folder Structure
campus-energy-dashboard-dikshit/
├─ src/
│   ├─ ingestion.py
│   ├─ aggregation.py
│   ├─ models.py
│   ├─ visualize.py
│   └─ main.py
├─ data/
│   ├─ BuildingA_2025-01.csv
│   └─ BuildingB_2025-01.csv
├─ output/
│   ├─ cleaned_energy_data.csv
│   ├─ building_summary.csv
│   ├─ dashboard.png
│   └─ summary.txt
└─ README.md

Dataset

Source: Sample CSV files representing building electricity consumption per hour.

Files included:

BuildingA_2025-01.csv

BuildingB_2025-01.csv

Columns:

timestamp → Date and time of meter reading

kwh → Electricity consumption in kWh

How to Run

Make sure Python 3.x is installed.

Open terminal/PowerShell in the project folder.

Run:

python src/main.py


Outputs are generated in the output/ folder:

cleaned_energy_data.csv → merged data

building_summary.csv → summary statistics

dashboard.png → multi-chart visualization

summary.txt → campus consumption summary

Methodology

Data Ingestion

Reads all CSV files in /data/ folder.

Adds building metadata from filename.

Handles missing or corrupt files gracefully.

Aggregation

Calculates daily and weekly totals per building.

Generates summary stats (mean, min, max, total).

Object-Oriented Design

Building and MeterReading classes store readings.

BuildingManager manages multiple building objects.

Visualization

Trend line: daily consumption for each building.

Bar chart: weekly average comparison.

Scatter plot: consumption vs. time per building.

Summary and Export

Exports cleaned and summarized CSVs.

Generates summary.txt with total campus consumption, peak load, highest-consuming building, and insights.

Insights (Sample)

BuildingA consumes slightly less than BuildingB during certain hours.

Peak consumption occurs on 2025-01-01 00:00:00.

Total campus consumption: 90.1 kWh

Highest-consuming building: BuildingA



