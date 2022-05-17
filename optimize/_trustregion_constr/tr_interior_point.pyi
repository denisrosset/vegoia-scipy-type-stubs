"""
This type stub file was generated by pyright.
"""

"""Trust-region interior point meth"""
__all__ = ['tr_interior_point']
class BarrierSubproblem:
    """
    Barrier optimization proble"""
    def __init__(self, x0, s0, fun, grad, lagr_hess, n_vars, n_ineq, n_eq, constr, jac, barrier_parameter, tolerance, enforce_feasibility, global_stop_criteria, xtol, fun0, grad0, constr_ineq0, jac_ineq0, constr_eq0, jac_eq0) -> None:
        ...
    
    def update(self, barrier_parameter, tolerance): # -> None:
        ...
    
    def get_slack(self, z):
        ...
    
    def get_variables(self, z):
        ...
    
    def function_and_constraints(self, z): # -> tuple[Unknown, ndarray[Unknown, Unknown]]:
        """Returns barrier function and con"""
        ...
    
    def scaling(self, z): # -> LinearOperator:
        """Returns scaling vector.
        """
        ...
    
    def gradient_and_jacobian(self, z): # -> tuple[ndarray[Unknown, Unknown], Unknown | csr_matrix | ndarray[Unknown, Unknown]]:
        """Returns scaled gradient.

      """
        ...
    
    def lagrangian_hessian_x(self, z, v):
        """Returns Lagrangian Hessian (in r"""
        ...
    
    def lagrangian_hessian_s(self, z, v):
        """Returns scaled Lagrangian Hessia"""
        ...
    
    def lagrangian_hessian(self, z, v): # -> LinearOperator:
        """Returns scaled Lagrangian Hessia"""
        ...
    
    def stop_criteria(self, state, z, last_iteration_failed, optimality, constr_violation, trust_radius, penalty, cg_info): # -> Literal[True]:
        """Stop criteria to the barrier pro"""
        ...
    


def tr_interior_point(fun, grad, lagr_hess, n_vars, n_ineq, n_eq, constr, jac, x0, fun0, grad0, constr_ineq0, jac_ineq0, constr_eq0, jac_eq0, stop_criteria, enforce_feasibility, xtol, state, initial_barrier_parameter, initial_tolerance, initial_penalty, initial_trust_radius, factorization_method): # -> tuple[Unknown, Unknown]:
    """Trust-region interior points met"""
    ...

