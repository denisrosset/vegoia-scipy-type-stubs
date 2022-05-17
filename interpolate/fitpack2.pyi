"""
This type stub file was generated by pyright.
"""

from . import dfitpack

"""
fitpack --- curve and surface f"""
__all__ = ['UnivariateSpline', 'InterpolatedUnivariateSpline', 'LSQUnivariateSpline', 'BivariateSpline', 'LSQBivariateSpline', 'SmoothBivariateSpline', 'LSQSphereBivariateSpline', 'SmoothSphereBivariateSpline', 'RectBivariateSpline', 'RectSphereBivariateSpline']
dfitpack_int = dfitpack.types.intvar.dtype
_curfit_messages = ...
_extrap_modes = ...
class UnivariateSpline:
    """
    1-D smoothing spline fit to"""
    def __init__(self, x, y, w=..., bbox=..., k=..., s=..., ext=..., check_finite=...) -> None:
        ...
    
    @staticmethod
    def validate_input(x, y, w, bbox, k, s, ext, check_finite):
        ...
    
    def set_smoothing_factor(self, s): # -> None:
        """ Continue spline computation wit"""
        ...
    
    def __call__(self, x, nu=..., ext=...): # -> ndarray[Unknown, Unknown] | ndarray[Any, Unknown] | list[Unknown] | Any:
        """
        Evaluate spline (or its"""
        ...
    
    def get_knots(self): # -> Any:
        """ Return positions of interior kn"""
        ...
    
    def get_coeffs(self): # -> Any:
        """Return spline coefficients."""
        ...
    
    def get_residual(self): # -> Any:
        """Return weighted sum of squared r"""
        ...
    
    def integral(self, a, b): # -> Any:
        """ Return definite integral of the"""
        ...
    
    def derivatives(self, x): # -> Any:
        """ Return all derivatives of the s"""
        ...
    
    def roots(self): # -> Any:
        """ Return the zeros of the spline."""
        ...
    
    def derivative(self, n=...): # -> UnivariateSpline:
        """
        Construct a new spline """
        ...
    
    def antiderivative(self, n=...): # -> UnivariateSpline:
        """
        Construct a new spline """
        ...
    


class InterpolatedUnivariateSpline(UnivariateSpline):
    """
    1-D interpolating spline fo"""
    def __init__(self, x, y, w=..., bbox=..., k=..., ext=..., check_finite=...) -> None:
        ...
    


_fpchec_error_string = ...
class LSQUnivariateSpline(UnivariateSpline):
    """
    1-D spline with explicit in"""
    def __init__(self, x, y, t, w=..., bbox=..., k=..., ext=..., check_finite=...) -> None:
        ...
    


class _BivariateSplineBase:
    """ Base class for Bivariate spline"""
    def get_residual(self):
        """ Return weighted sum of squared """
        ...
    
    def get_knots(self):
        """ Return a tuple (tx,ty) where tx"""
        ...
    
    def get_coeffs(self):
        """ Return spline coefficients."""
        ...
    
    def __call__(self, x, y, dx=..., dy=..., grid=...):
        """
        Evaluate the spline or """
        ...
    


_surfit_messages = ...
class BivariateSpline(_BivariateSplineBase):
    """
    Base class for bivariate sp"""
    def ev(self, xi, yi, dx=..., dy=...):
        """
        Evaluate the spline at """
        ...
    
    def integral(self, xa, xb, ya, yb): # -> Any:
        """
        Evaluate the integral o"""
        ...
    


class SmoothBivariateSpline(BivariateSpline):
    """
    Smooth bivariate spline app"""
    def __init__(self, x, y, z, w=..., bbox=..., kx=..., ky=..., s=..., eps=...) -> None:
        ...
    


class LSQBivariateSpline(BivariateSpline):
    """
    Weighted least-squares biva"""
    def __init__(self, x, y, z, tx, ty, w=..., bbox=..., kx=..., ky=..., eps=...) -> None:
        ...
    


class RectBivariateSpline(BivariateSpline):
    """
    Bivariate spline approximat"""
    def __init__(self, x, y, z, bbox=..., kx=..., ky=..., s=...) -> None:
        ...
    


_spherefit_messages = ...
class SphereBivariateSpline(_BivariateSplineBase):
    """
    Bivariate spline s(x,y) of """
    def __call__(self, theta, phi, dtheta=..., dphi=..., grid=...):
        """
        Evaluate the spline or """
        ...
    
    def ev(self, theta, phi, dtheta=..., dphi=...):
        """
        Evaluate the spline at """
        ...
    


class SmoothSphereBivariateSpline(SphereBivariateSpline):
    """
    Smooth bivariate spline app"""
    def __init__(self, theta, phi, r, w=..., s=..., eps=...) -> None:
        ...
    
    def __call__(self, theta, phi, dtheta=..., dphi=..., grid=...):
        ...
    


class LSQSphereBivariateSpline(SphereBivariateSpline):
    """
    Weighted least-squares biva"""
    def __init__(self, theta, phi, r, tt, tp, w=..., eps=...) -> None:
        ...
    
    def __call__(self, theta, phi, dtheta=..., dphi=..., grid=...):
        ...
    


_spfit_messages = ...
class RectSphereBivariateSpline(SphereBivariateSpline):
    """
    Bivariate spline approximat"""
    def __init__(self, u, v, r, s=..., pole_continuity=..., pole_values=..., pole_exact=..., pole_flat=...) -> None:
        ...
    
    def __call__(self, theta, phi, dtheta=..., dphi=..., grid=...):
        ...
    

