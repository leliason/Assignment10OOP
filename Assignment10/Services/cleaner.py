from domain.records import Record

class Cleaner:
    def clean(self, raw_data: dict, elevation: float):
        temps = raw_data["temperatures"]
        pairs = [(temps[i], temps[i+1]) for i in range(0, len(temps)-1, 2) if temps[i] is not None and temps[i+1] is not None]
        records = []
        for max_t, min_t in pairs:
            record = Record(
                city=raw_data["city"],
                elevation=float(elevation),
                temperature=(max_t, min_t)
            )
            records.append(record)
        return records