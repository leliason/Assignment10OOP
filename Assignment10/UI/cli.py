from persistence.api_client import ApiClient
from persistence.repository import Repository
from services.cleaner import Cleaner
from services.analyzer import Analyzer

class CLI:
    def __init__(self, api_client, repository, cleaner, analyzer):
        self.api_client = api_client
        self.repository = repository
        self.cleaner = cleaner
        self.analyzer = analyzer
    def run(self):
        print("#### Temperature v Elevation Analysis ####\n")
        cities= [
            #lower elevation cities (not in order)
            ('New York, USA', 40.7128, -74.0060, 10),
            ("Tokyo, Japan", 35.6762, 139.6503, 40),
            ("Miami, USA", 25.7617, -80.1918, 2),
            ("London, England", 51.5074, -0.1278, 11),
            ("Los Angeles, USA", 34.0522, -118.2437, 71),
            #mid elevation
            ("Madrid, Spain", 40.4168, -3.7038, 667),
            ("Addis Ababa, Ethiopia", 8.9806, 38.7578, 2355),
            ("Nairobi, Kenya", -1.2921, 36.8219, 1795),
            #high elevation
            ("Quito, Ecuador", -0.1807, -78.4678, 2850),
            ("Kathmandu, Nepal", 27.7172, 85.3240, 1400),
            ("Denver, USA", 39.7392, -104.9903, 1609),
            ("Mexico City, Mexico", 19.4326, -99.1332, 2250),
            ("La Paz, Bolivia", -16.4897, -68.1193, 3640),
        ]
        for city, lat, lon, elevation in cities:
            raw = self.api_client.fetch_city_data(city, lat, lon)
            cleaned_records = self.cleaner.clean(raw, elevation)

            for record in cleaned_records:
                self.repository.save(record)

        records = self.repository.get_all()
        result = self.analyzer.analyze(records)

        print("THESIS:\nHigher elevation is associated with more drastic changes in temperature")
        print("SOURCE: Open-Meteo Weather Api\nLINK:https: //api.open-meteo.com/v1/forecast")
        print(f"Total amount of records gathered: {len(records)}\n")

        print("METHOD:\nCollected daily temperature data from different cities with differing elevation")
        print("Computed the correlation to prove/disprove thesis")

        print("Sample data:\n")
        print(f"{'city':<18}{"elevation(m)":<15}{"temperature":<12}")
        sample = records[:12]
        for i in sample:
            print(f"{i.city:<18}{i.elevation:<15}{i.temperature:<12}")

        print("\nCorrelation coeficcient:")
        print(f"{result.correlation:.4f}\n")

        print(f"CONCLUSION:\n{result.conclusion}")
        