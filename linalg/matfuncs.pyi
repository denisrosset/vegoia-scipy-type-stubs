"""
This type stub file was generated by pyright.
"""

import numpy as np
from numpy import single

__all__ = ['expm', 'cosm', 'sinm', 'tanm', 'coshm', 'sinhm', 'tanhm', 'logm', 'funm', 'signm', 'sqrtm', 'expm_frechet', 'expm_cond', 'fractional_matrix_power', 'khatri_rao']
eps = np.finfo(float).eps
feps = np.finfo(single).eps
_array_precision = ...
def fractional_matrix_power(A, t):
    """
    Compute the fractional powe"""
    ...

def logm(A, disp=...): # -> Any | ndarray[Unknown, _dtype] | ndarray[Any, _dtype] | ndarray[Unknown, Unknown] | NDArray[Any] | tuple[Unknown | Any | ndarray[Unknown, _dtype] | ndarray[Any, _dtype] | ndarray[Unknown, Unknown] | NDArray[Any], Unknown]:
    """
    Compute matrix logarithm.

"""
    ...

def expm(A):
    """
    Compute the matrix exponent"""
    ...

def cosm(A):
    """
    Compute the matrix cosine.
"""
    ...

def sinm(A):
    """
    Compute the matrix sine.

 """
    ...

def tanm(A):
    """
    Compute the matrix tangent."""
    ...

def coshm(A):
    """
    Compute the hyperbolic matr"""
    ...

def sinhm(A):
    """
    Compute the hyperbolic matr"""
    ...

def tanhm(A):
    """
    Compute the hyperbolic matr"""
    ...

def funm(A, func, disp=...): # -> tuple[Unknown, float | int]:
    """
    Evaluate a matrix function """
    ...

def signm(A, disp=...): # -> Any | tuple[Unknown | Any, Unknown | float | int]:
    """
    Matrix sign function.

    """
    ...

def khatri_rao(a, b): # -> Any:
    r"""
    Khatri-rao product

    A c"""
    ...
