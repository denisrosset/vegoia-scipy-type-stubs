"""
This type stub file was generated by pyright.
"""

import numpy as np
from typing import Optional, TYPE_CHECKING, TypeVar, Union

IntNumber = Union[int, np.integer]
DecimalNumber = Union[float, np.floating, np.integer]
if TYPE_CHECKING:
    SeedType = Optional[Union[IntNumber, np.random.Generator, np.random.RandomState]]
    GeneratorType = TypeVar("GeneratorType", bound=Union[np.random.Generator, np.random.RandomState])
def prod(iterable): # -> Literal[1]:
    """
    Product of a sequence of nu"""
    ...

def float_factorial(n: int) -> float:
    """Compute the factorial and return"""
    ...

class DeprecatedImport:
    """
    Deprecated import with redi"""
    def __init__(self, old_module_name, new_module_name) -> None:
        ...
    
    def __dir__(self): # -> list[str]:
        ...
    
    def __getattr__(self, name): # -> Any:
        ...
    


def check_random_state(seed): # -> RandomState | Generator:
    """Turn `seed` into a `np.random.Ra"""
    ...

FullArgSpec = ...
def getfullargspec_no_self(func): # -> FullArgSpec:
    """inspect.getfullargspec replaceme"""
    ...

class MapWrapper:
    """
    Parallelisation wrapper for"""
    def __init__(self, pool=...) -> None:
        ...
    
    def __enter__(self): # -> Self@MapWrapper:
        ...
    
    def terminate(self): # -> None:
        ...
    
    def join(self): # -> None:
        ...
    
    def close(self): # -> None:
        ...
    
    def __exit__(self, exc_type, exc_value, traceback): # -> None:
        ...
    
    def __call__(self, func, iterable): # -> map[Unknown] | list[Unknown]:
        ...
    


def rng_integers(gen, low, high=..., size=..., dtype=..., endpoint=...):
    """
    Return random integers from"""
    ...

