"""
This type stub file was generated by pyright.
"""

from scipy.sparse.linalg import LinearOperator

"""
Functions
---------
.. autosumm"""
__all__ = ['fmin_l_bfgs_b', 'LbfgsInvHessProduct']
def fmin_l_bfgs_b(func, x0, fprime=..., args=..., approx_grad=..., bounds=..., m=..., factr=..., pgtol=..., epsilon=..., iprint=..., maxfun=..., maxiter=..., disp=..., callback=..., maxls=...): # -> tuple[Unknown, Unknown, dict[str, Unknown]]:
    """
    Minimize a function func us"""
    ...

class LbfgsInvHessProduct(LinearOperator):
    """Linear operator for the L-BFGS a"""
    def __init__(self, sk, yk) -> None:
        """Construct the operator."""
        ...
    
    def todense(self): # -> ndarray[Any, Any]:
        """Return a dense array representat"""
        ...
    

