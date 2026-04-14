class Record:
    def __init__(self, city: str, elevation: float, temperature: float):
        self.city = city
        self.elevation = elevation
        self.temperature = temperature
    def temp_range(self) -> float:
        if not self.temperature:
            return 0.0
        return self.temperature[0] - self.temperature[1]