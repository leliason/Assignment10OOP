from domain.records import Record

class Cleaner:
    def clean(self, raw_data: dict, elevation: float):

        temps = raw_data["daily"]["temperature_2m_max"]
        temps_min = raw_data["daily"]["temperature_2m_min"]
        times = raw_data["daily"]["time"]
        records = []

        for i in range(len(times)):
            daily_temps = [temps[i], temps_min[i]]
            records.append(
                Record(
                    city=raw_data["city"],
                    elevation=float(elevation),
                    temperatures=daily_temps
                )
            )
        return records