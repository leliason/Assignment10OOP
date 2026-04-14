class Thesis:
    """
    Represents the hypothesis being tested.
    """

    def __init__(self, statement: str):
        self.statement = statement
        self.independent_variable = "Elevation"
        self.dependent_variable = "Temperature Range"

    def __str__(self):
        return f"Thesis: {self.statement}"