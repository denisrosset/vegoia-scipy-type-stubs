"""
This type stub file was generated by pyright.
"""

import numpy as np
from ._trustregion import BaseQuadraticSubproblem

"""Nearly exact trust-region optimi"""
__all__ = ['_minimize_trustregion_exact', 'estimate_smallest_singular_value', 'singular_leading_submatrix', 'IterativeSubproblem']
def estimate_smallest_singular_value(U): # -> tuple[Unknown, Unknown]:
    """Given upper triangular matrix ``"""
    ...

def gershgorin_bounds(H): # -> tuple[Unknown, Unknown]:
    """
    Given a square matrix ``H``"""
    ...

def singular_leading_submatrix(A, U, k): # -> tuple[Unknown, ndarray[Unknown, Unknown]]:
    """
    Compute term that makes the"""
    ...

class IterativeSubproblem(BaseQuadraticSubproblem):
    """Quadratic subproblem solved by n"""
    UPDATE_COEFF = ...
    EPS = np.finfo(float).eps
    def __init__(self, x, fun, jac, hess, hessp=..., k_easy=..., k_hard=...) -> None:
        ...
    
    def solve(self, tr_radius):
        """Solve quadratic subproblem"""
        ...
    


