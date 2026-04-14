class AnalysisResult:
    def __init__(self, correlation: float, conclusion: str):
        self.correlation = correlation
        self.conclusion = conclusion
    def __str__(self):
        return (
            f"Correlation: {self.correlation:.3f}\n"
            f"Conclusion: {self.conclusion}"
        )