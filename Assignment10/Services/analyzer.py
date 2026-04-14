import numpy as np
from Assignment10.Domain.analysis_result import AnalysisResult

class Analyzer:
    def analyze(self, records):
        elevations = [r.elevation for r in records]
        temp_ranges = [r.temp_range() for r in records]

        # Correlation coefficient
        correlation = np.corrcoef(elevations, temp_ranges)[0, 1]

        # Interpretation
        if correlation > 0.5:
            conclusion = "thesis supported."
        elif correlation > 0:
            conclusion = "partial thesis support."
        else:
            conclusion = "thesis not supported."

        return AnalysisResult(correlation, conclusion)