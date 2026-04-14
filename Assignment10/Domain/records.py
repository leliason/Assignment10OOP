class Record:
    """
    Represents a single city's data.

    Attributes:
        city (str): Name of the city
        elevation (float): Elevation in meters
        temperatures (list[float]): List of temperature values
    """

    def __init__(self, city: str, elevation: float, temperatures: list[float]):
        self.city = city
        self.elevation = elevation
        self.temperatures = temperatures

    def temp_range(self) -> float:
        """
        Computes the temperature range (max - min).
        """
        if not self.temperatures:
            return 0
        return max(self.temperatures) - min(self.temperatures)