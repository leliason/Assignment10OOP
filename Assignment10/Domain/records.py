class Record:
    def __init__(self, city: str, elevation: float, temperature: float):
        self.city = city
        self.elevation = elevation
        self.temperatures = temperature
    def temp_range(self) -> float:
        if not self.temperatures:
            return 0
        return max(self.temperatures) - min(self.temperatures)