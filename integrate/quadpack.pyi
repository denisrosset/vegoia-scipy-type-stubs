"""
This type stub file was generated by pyright.
"""

__all__ = ['quad', 'dblquad', 'tplquad', 'nquad', 'quad_explain', 'IntegrationWarning']
error = ...
class IntegrationWarning(UserWarning):
    """
    Warning on issues during in"""
    ...


def quad_explain(output=...): # -> None:
    """
    Print extra information abo"""
    ...

def quad(func, a, b, args=..., full_output=..., epsabs=..., epsrel=..., limit=..., points=..., weight=..., wvar=..., wopts=..., maxp1=..., limlst=...):
    """
    Compute a definite integral"""
    ...

def dblquad(func, a, b, gfun, hfun, args=..., epsabs=..., epsrel=...): # -> tuple[Unknown, int, dict[str, int]] | tuple[Unknown, int]:
    """
    Compute a double integral.
"""
    ...

def tplquad(func, a, b, gfun, hfun, qfun, rfun, args=..., epsabs=..., epsrel=...): # -> tuple[Unknown, int, dict[str, int]] | tuple[Unknown, int]:
    """
    Compute a triple (definite)"""
    ...

def nquad(func, ranges, args=..., opts=..., full_output=...): # -> tuple[Unknown, int, dict[str, int]] | tuple[Unknown, int]:
    """
    Integration over multiple v"""
    ...

class _RangeFunc:
    def __init__(self, range_) -> None:
        ...
    
    def __call__(self, *args): # -> Unknown:
        """Return stored value.

        *a"""
        ...
    


class _OptFunc:
    def __init__(self, opt) -> None:
        ...
    
    def __call__(self, *args): # -> Unknown:
        """Return stored dict."""
        ...
    


class _NQuad:
    def __init__(self, func, ranges, opts, full_output) -> None:
        ...
    
    def integrate(self, *args, **kwargs): # -> tuple[Unknown, int, dict[str, int]] | tuple[Unknown, int]:
        ...
    

