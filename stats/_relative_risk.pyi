"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass

@dataclass
class RelativeRiskResult:
    """
    Result of `scipy.stats.cont"""
    relative_risk: float
    exposed_cases: int
    exposed_total: int
    control_cases: int
    control_total: int
    def confidence_interval(self, confidence_level=...): # -> ConfidenceInterval:
        """
        Compute the confidence """
        ...
    


def relative_risk(exposed_cases, exposed_total, control_cases, control_total): # -> RelativeRiskResult:
    """
    Compute the relative risk ("""
    ...

