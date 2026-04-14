from domain.records import Record

class Cleaner:
    def clean(self, raw_data: dict, elevation: float):
        temps = [t for t in raw_data["temperatures"] if t is not None]

        record = Record(
            city=raw_data["city"],
            elevation=float(elevation),
            temperature=temps
        )

        return [record]