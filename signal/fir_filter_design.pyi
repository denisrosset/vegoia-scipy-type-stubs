"""
This type stub file was generated by pyright.
"""

"""Functions for FIR filter design."""
__all__ = ['kaiser_beta', 'kaiser_atten', 'kaiserord', 'firwin', 'firwin2', 'remez', 'firls', 'minimum_phase']
def kaiser_beta(a): # -> float:
    """Compute the Kaiser parameter `be"""
    ...

def kaiser_atten(numtaps, width):
    """Compute the attenuation of a Kai"""
    ...

def kaiserord(ripple, width): # -> tuple[int, Unknown | float]:
    """
    Determine the filter window"""
    ...

def firwin(numtaps, cutoff, width=..., window=..., pass_zero=..., scale=..., nyq=..., fs=...):
    """
    FIR filter design using the"""
    ...

def firwin2(numtaps, freq, gain, nfreqs=..., window=..., nyq=..., antisymmetric=..., fs=...):
    """
    FIR filter design using the"""
    ...

def remez(numtaps, bands, desired, weight=..., Hz=..., type=..., maxiter=..., grid_density=..., fs=...): # -> Any:
    """
    Calculate the minimax optim"""
    ...

def firls(numtaps, bands, desired, weight=..., nyq=..., fs=...):
    """
    FIR filter design using lea"""
    ...

def minimum_phase(h, method=..., n_fft=...):
    """Convert a linear-phase FIR filte"""
    ...

