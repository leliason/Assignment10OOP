from domain.record import Record

class Cleaner:
    def clean(self, raw_data: dict, elevation: float) -> Record:
        temps = [t for t in raw_data["temperatures"] if t is not None]

        return Record(
            city=raw_data["city"],
            elevation=float(elevation),
            temperatures=temps
        )