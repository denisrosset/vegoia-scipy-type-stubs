"""
This type stub file was generated by pyright.
"""

from .interpnd import NDInterpolatorBase

"""
Convenience interface to N-D in"""
__all__ = ['griddata', 'NearestNDInterpolator', 'LinearNDInterpolator', 'CloughTocher2DInterpolator']
class NearestNDInterpolator(NDInterpolatorBase):
    """NearestNDInterpolator(x, y).

  """
    def __init__(self, x, y, rescale=..., tree_options=...) -> None:
        ...
    
    def __call__(self, *args): # -> Any:
        """
        Evaluate interpolator a"""
        ...
    


def griddata(points, values, xi, method=..., fill_value=..., rescale=...):
    """
    Interpolate unstructured D-"""
    ...
