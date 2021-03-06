"""
This type stub file was generated by pyright.
"""

"""
This module implements the Sequ"""
__all__ = ['approx_jacobian', 'fmin_slsqp']
__docformat__ = ...
_epsilon = ...
def approx_jacobian(x, func, epsilon, *args): # -> ndarray[Unknown, Unknown]:
    """
    Approximate the Jacobian ma"""
    ...

def fmin_slsqp(func, x0, eqcons=..., f_eqcons=..., ieqcons=..., f_ieqcons=..., bounds=..., fprime=..., fprime_eqcons=..., fprime_ieqcons=..., args=..., iter=..., acc=..., iprint=..., disp=..., full_output=..., epsilon=..., callback=...): # -> tuple[Unknown, Unknown, Unknown, Unknown, Unknown]:
    """
    Minimize a function using S"""
    ...

if __name__ == '__main__':
    def fun(x, r=...):
        """ Objective function """
        ...
    
    bnds = ...
    def feqcon(x, b=...): # -> ndarray[Unknown, Unknown]:
        """ Equality constraint """
        ...
    
    def jeqcon(x, b=...): # -> ndarray[Unknown, Unknown]:
        """ Jacobian of equality constraint"""
        ...
    
    def fieqcon(x, c=...): # -> ndarray[Unknown, Unknown]:
        """ Inequality constraint """
        ...
    
    def jieqcon(x, c=...): # -> ndarray[Unknown, Unknown]:
        """ Jacobian of inequality constrai"""
        ...
    
    cons = ...
    res = ...
    res = ...
