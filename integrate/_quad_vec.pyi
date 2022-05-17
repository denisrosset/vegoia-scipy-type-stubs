"""
This type stub file was generated by pyright.
"""

import collections

class LRUDict(collections.OrderedDict):
    def __init__(self, max_size) -> None:
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def update(self, other):
        ...
    


class SemiInfiniteFunc:
    """
    Argument transform from (st"""
    def __init__(self, func, start, infty) -> None:
        ...
    
    def get_t(self, x): # -> float:
        ...
    
    def __call__(self, t): # -> float:
        ...
    


class DoubleInfiniteFunc:
    """
    Argument transform from (-o"""
    def __init__(self, func) -> None:
        ...
    
    def get_t(self, x):
        ...
    
    def __call__(self, t): # -> float:
        ...
    


class _Bunch:
    def __init__(self, **kwargs) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    


def quad_vec(f, a, b, epsabs=..., epsrel=..., norm=..., cache_size=..., limit=..., workers=..., points=..., quadrature=..., full_output=...):
    r"""Adaptive integration of a vector"""
    ...
