"""
This type stub file was generated by pyright.
"""

"""The adaptation of Trust Region R"""
def regularized_lsq_with_qr(m, n, R, QTb, perm, diag, copy_R=...): # -> ndarray[Unknown, Unknown]:
    """Solve regularized least squares """
    ...

def backtracking(A, g, x, p, theta, p_dot_g, lb, ub): # -> tuple[Unknown, Unknown, Unknown]:
    """Find an appropriate step size us"""
    ...

def select_step(x, A_h, g_h, c_h, p, p_h, d, lb, ub, theta):
    """Select the best step according t"""
    ...

def trf_linear(A, b, x_lsq, lb, ub, tol, lsq_solver, lsmr_tol, max_iter, verbose):
    ...

