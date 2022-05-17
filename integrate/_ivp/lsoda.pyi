"""
This type stub file was generated by pyright.
"""

from .base import DenseOutput, OdeSolver

class LSODA(OdeSolver):
    """Adams/BDF method with automatic """
    def __init__(self, fun, t0, y0, t_bound, first_step=..., min_step=..., max_step=..., rtol=..., atol=..., jac=..., lband=..., uband=..., vectorized=..., **extraneous) -> None:
        ...
    


class LsodaDenseOutput(DenseOutput):
    def __init__(self, t_old, t, h, order, yh) -> None:
        ...
    

