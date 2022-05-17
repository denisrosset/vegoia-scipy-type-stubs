"""
This type stub file was generated by pyright.
"""

__all__ = ['daub', 'qmf', 'cascade', 'morlet', 'ricker', 'morlet2', 'cwt']
def daub(p): # -> ndarray[Unknown, Unknown] | Any:
    """
    The coefficients for the FI"""
    ...

def qmf(hk):
    """
    Return high-pass qmf filter"""
    ...

def cascade(hk, J=...): # -> tuple[Unknown, Unknown, Unknown]:
    """
    Return (x, phi, psi) at dya"""
    ...

def morlet(M, w=..., s=..., complete=...): # -> Any:
    """
    Complex Morlet wavelet.

  """
    ...

def ricker(points, a):
    """
    Return a Ricker wavelet, al"""
    ...

def morlet2(M, s, w=...): # -> Any:
    """
    Complex Morlet wavelet, des"""
    ...

def cwt(data, wavelet, widths, dtype=..., **kwargs): # -> ndarray[Unknown, Unknown]:
    """
    Continuous wavelet transfor"""
    ...
