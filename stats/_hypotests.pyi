"""
This type stub file was generated by pyright.
"""

__all__ = ['epps_singleton_2samp', 'cramervonmises', 'somersd', 'barnard_exact', 'boschloo_exact', 'cramervonmises_2samp']
Epps_Singleton_2sampResult = ...
def epps_singleton_2samp(x, y, t=...): # -> Epps_Singleton_2sampResult:
    """Compute the Epps-Singleton (ES) """
    ...

class CramerVonMisesResult:
    def __init__(self, statistic, pvalue) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    


def cramervonmises(rvs, cdf, args=...): # -> CramerVonMisesResult:
    """Perform the one-sample Cramér-vo"""
    ...

SomersDResult = ...
def somersd(x, y=...): # -> Any:
    r"""Calculates Somers' D, an asymmet"""
    ...

BarnardExactResult = ...
def barnard_exact(table, alternative=..., pooled=..., n=...): # -> Any:
    r"""Perform a Barnard exact test on """
    ...

BoschlooExactResult = ...
def boschloo_exact(table, alternative=..., n=...): # -> Any:
    r"""Perform Boschloo's exact test on"""
    ...

def cramervonmises_2samp(x, y, method=...): # -> CramerVonMisesResult:
    """Perform the two-sample Cramér-vo"""
    ...

