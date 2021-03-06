"""
This type stub file was generated by pyright.
"""

"""Equality-constrained quadratic p"""
__all__ = ['eqp_kktfact', 'sphere_intersections', 'box_intersections', 'box_sphere_intersections', 'inside_box_boundaries', 'modified_dogleg', 'projected_cg']
def eqp_kktfact(H, c, A, b): # -> tuple[Unknown, Unknown]:
    """Solve equality-constrained quadr"""
    ...

def sphere_intersections(z, d, trust_radius, entire_line=...): # -> tuple[Literal[0], Literal[0], Literal[False]] | tuple[float | Literal[0], float | Literal[1], Literal[True]] | tuple[Unknown | int, Unknown | int, bool]:
    """Find the intersection between se"""
    ...

def box_intersections(z, d, lb, ub, entire_line=...): # -> tuple[Literal[0], Literal[0], Literal[False]] | tuple[int | Any, int | Any, bool]:
    """Find the intersection between se"""
    ...

def box_sphere_intersections(z, d, lb, ub, trust_radius, entire_line=..., extra_info=...): # -> tuple[Any, Any, bool, dict[str, float | Unknown | int | bool], dict[str, int | Any | bool]] | tuple[Any, Any, bool]:
    """Find the intersection between se"""
    ...

def inside_box_boundaries(x, lb, ub):
    """Check if lb <= x <= ub."""
    ...

def reinforce_box_boundaries(x, lb, ub): # -> Any:
    """Return clipped value of x"""
    ...

def modified_dogleg(A, Y, b, trust_radius, lb, ub):
    """Approximately  minimize ``1/2*||"""
    ...

def projected_cg(H, c, Z, Y, b, trust_radius=..., lb=..., ub=..., tol=..., max_iter=..., max_infeasible_iter=..., return_all=...):
    """Solve EQP problem with projected"""
    ...

