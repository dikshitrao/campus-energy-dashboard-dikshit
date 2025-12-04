class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh

class Building:
    def __init__(self, name):
        self.name = name
        self.meter_readings = []

    def add_reading(self, reading):
        self.meter_readings.append(reading)

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.meter_readings)

    def generate_report(self):
        total = self.calculate_total_consumption()
        return f"Building: {self.name}\nTotal Consumption: {total} kWh\n"

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def add_reading(self, building_name, reading):
        if building_name not in self.buildings:
            self.buildings[building_name] = Building(building_name)
        self.buildings[building_name].add_reading(reading)

    def generate_all_reports(self):
        reports = ""
        for b in self.buildings.values():
            reports += b.generate_report() + "\n"
        return reports
