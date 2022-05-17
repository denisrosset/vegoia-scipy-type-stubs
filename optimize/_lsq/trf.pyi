"""
This type stub file was generated by pyright.
"""

"""Trust Region Reflective algorith"""
def trf(fun, jac, x0, f0, J0, lb, ub, ftol, xtol, gtol, max_nfev, x_scale, loss_function, tr_solver, tr_options, verbose):
    ...

def select_step(x, J_h, diag_h, g_h, p, p_h, d, Delta, lb, ub, theta): # -> tuple[Unknown, Unknown, Unknown] | tuple[Unknown, Unknown, Unknown | float]:
    """Select the best step according t"""
    ...

def trf_bounds(fun, jac, x0, f0, J0, lb, ub, ftol, xtol, gtol, max_nfev, x_scale, loss_function, tr_solver, tr_options, verbose):
    ...

def trf_no_bounds(fun, jac, x0, f0, J0, ftol, xtol, gtol, max_nfev, x_scale, loss_function, tr_solver, tr_options, verbose):
    ...
