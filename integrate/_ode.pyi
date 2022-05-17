"""
This type stub file was generated by pyright.
"""

from . import _dop, lsoda as _lsoda, vode as _vode

"""
First-order ODE integrators.

U"""
__all__ = ['ode', 'complex_ode']
__version__ = ...
__docformat__ = ...
_dop_int_dtype = _dop.types.intvar.dtype
_vode_int_dtype = _vode.types.intvar.dtype
_lsoda_int_dtype = _lsoda.types.intvar.dtype
class ode:
    """
    A generic interface class t"""
    def __init__(self, f, jac=...) -> None:
        ...
    
    @property
    def y(self): # -> ndarray[Unknown, Unknown] | list[Unknown]:
        ...
    
    def set_initial_value(self, y, t=...): # -> Self@ode:
        """Set initial conditions y(t) = y."""
        ...
    
    def set_integrator(self, name, **integrator_params): # -> Self@ode:
        """
        Set integrator by name."""
        ...
    
    def integrate(self, t, step=..., relax=...):
        """Find y=y(t), set y as an initial"""
        ...
    
    def successful(self):
        """Check if integration was success"""
        ...
    
    def get_return_code(self):
        """Extracts the return code for the"""
        ...
    
    def set_f_params(self, *args): # -> Self@ode:
        """Set extra parameters for user-su"""
        ...
    
    def set_jac_params(self, *args): # -> Self@ode:
        """Set extra parameters for user-su"""
        ...
    
    def set_solout(self, solout): # -> None:
        """
        Set callable to be call"""
        ...
    


class complex_ode(ode):
    """
    A wrapper of ode for comple"""
    def __init__(self, f, jac=...) -> None:
        ...
    
    @property
    def y(self):
        ...
    
    def set_integrator(self, name, **integrator_params): # -> ode:
        """
        Set integrator by name."""
        ...
    
    def set_initial_value(self, y, t=...): # -> ode:
        """Set initial conditions y(t) = y."""
        ...
    
    def integrate(self, t, step=..., relax=...):
        """Find y=y(t), set y as an initial"""
        ...
    
    def set_solout(self, solout): # -> None:
        """
        Set callable to be call"""
        ...
    


def find_integrator(name): # -> None:
    ...

class IntegratorConcurrencyError(RuntimeError):
    """
    Failure due to concurrent u"""
    def __init__(self, name) -> None:
        ...
    


class IntegratorBase:
    runner = ...
    success = ...
    istate = ...
    supports_run_relax = ...
    supports_step = ...
    supports_solout = ...
    integrator_classes = ...
    scalar = float
    def acquire_new_handle(self): # -> None:
        ...
    
    def check_handle(self): # -> None:
        ...
    
    def reset(self, n, has_jac): # -> None:
        """Prepare integrator for call: all"""
        ...
    
    def run(self, f, jac, y0, t0, t1, f_params, jac_params):
        """Integrate from t=t0 to t=t1 usin"""
        ...
    
    def step(self, f, jac, y0, t0, t1, f_params, jac_params):
        """Make one integration step and re"""
        ...
    
    def run_relax(self, f, jac, y0, t0, t1, f_params, jac_params):
        """Integrate from t=t0 to t>=t1 and"""
        ...
    


class vode(IntegratorBase):
    runner = ...
    messages = ...
    supports_run_relax = ...
    supports_step = ...
    active_global_handle = ...
    def __init__(self, method=..., with_jacobian=..., rtol=..., atol=..., lband=..., uband=..., order=..., nsteps=..., max_step=..., min_step=..., first_step=...) -> None:
        ...
    
    def reset(self, n, has_jac):
        ...
    
    def run(self, f, jac, y0, t0, t1, f_params, jac_params): # -> tuple[Any, Any]:
        ...
    
    def step(self, *args): # -> tuple[Any, Any]:
        ...
    
    def run_relax(self, *args): # -> tuple[Any, Any]:
        ...
    


if vode.runner is not None:
    ...
class zvode(vode):
    runner = ...
    supports_run_relax = ...
    supports_step = ...
    scalar = complex
    active_global_handle = ...
    def reset(self, n, has_jac):
        ...
    


if zvode.runner is not None:
    ...
class dopri5(IntegratorBase):
    runner = ...
    name = ...
    supports_solout = ...
    messages = ...
    def __init__(self, rtol=..., atol=..., nsteps=..., max_step=..., first_step=..., safety=..., ifactor=..., dfactor=..., beta=..., method=..., verbosity=...) -> None:
        ...
    
    def set_solout(self, solout, complex=...): # -> None:
        ...
    
    def reset(self, n, has_jac): # -> None:
        ...
    
    def run(self, f, jac, y0, t0, t1, f_params, jac_params): # -> tuple[Any, Any]:
        ...
    


if dopri5.runner is not None:
    ...
class dop853(dopri5):
    runner = ...
    name = ...
    def __init__(self, rtol=..., atol=..., nsteps=..., max_step=..., first_step=..., safety=..., ifactor=..., dfactor=..., beta=..., method=..., verbosity=...) -> None:
        ...
    
    def reset(self, n, has_jac): # -> None:
        ...
    


if dop853.runner is not None:
    ...
class lsoda(IntegratorBase):
    runner = ...
    active_global_handle = ...
    messages = ...
    def __init__(self, with_jacobian=..., rtol=..., atol=..., lband=..., uband=..., nsteps=..., max_step=..., min_step=..., first_step=..., ixpr=..., max_hnil=..., max_order_ns=..., max_order_s=..., method=...) -> None:
        ...
    
    def reset(self, n, has_jac):
        ...
    
    def run(self, f, jac, y0, t0, t1, f_params, jac_params): # -> tuple[Any, Any]:
        ...
    
    def step(self, *args): # -> tuple[Any, Any]:
        ...
    
    def run_relax(self, *args): # -> tuple[Any, Any]:
        ...
    


if lsoda.runner:
    ...