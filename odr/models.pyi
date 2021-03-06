"""
This type stub file was generated by pyright.
"""

from scipy.odr.odrpack import Model

""" Collection of Model instances f"""
__all__ = ['Model', 'exponential', 'multilinear', 'unilinear', 'quadratic', 'polynomial']
class _MultilinearModel(Model):
    r"""
    Arbitrary-dimensional linea"""
    def __init__(self) -> None:
        ...
    


multilinear = ...
def polynomial(order): # -> Model:
    """
    Factory function for a gene"""
    ...

class _ExponentialModel(Model):
    r"""
    Exponential model

    This"""
    def __init__(self) -> None:
        ...
    


exponential = ...
class _UnilinearModel(Model):
    r"""
    Univariate linear model

  """
    def __init__(self) -> None:
        ...
    


unilinear = ...
class _QuadraticModel(Model):
    r"""
    Quadratic model

    This m"""
    def __init__(self) -> None:
        ...
    


quadratic = ...
