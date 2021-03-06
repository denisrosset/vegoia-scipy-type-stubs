"""
This type stub file was generated by pyright.
"""

"""Trust-region optimization."""
__all__ = []
class BaseQuadraticSubproblem:
    """
    Base/abstract class definin"""
    def __init__(self, x, fun, jac, hess=..., hessp=...) -> None:
        ...
    
    def __call__(self, p):
        ...
    
    @property
    def fun(self):
        """Value of objective function at c"""
        ...
    
    @property
    def jac(self):
        """Value of Jacobian of objective f"""
        ...
    
    @property
    def hess(self):
        """Value of Hessian of objective fu"""
        ...
    
    def hessp(self, p):
        ...
    
    @property
    def jac_mag(self):
        """Magnitude of jacobian of objecti"""
        ...
    
    def get_boundaries_intersections(self, z, d, trust_radius): # -> list[Unknown]:
        """
        Solve the scalar quadra"""
        ...
    
    def solve(self, trust_radius):
        ...
    


