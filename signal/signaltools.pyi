"""
This type stub file was generated by pyright.
"""

__all__ = ['correlate', 'correlation_lags', 'correlate2d', 'convolve', 'convolve2d', 'fftconvolve', 'oaconvolve', 'order_filter', 'medfilt', 'medfilt2d', 'wiener', 'lfilter', 'lfiltic', 'sosfilt', 'deconvolve', 'hilbert', 'hilbert2', 'cmplx_sort', 'unique_roots', 'invres', 'invresz', 'residue', 'residuez', 'resample', 'resample_poly', 'detrend', 'lfilter_zi', 'sosfilt_zi', 'sosfiltfilt', 'choose_conv_method', 'filtfilt', 'decimate', 'vectorstrength']
_modedict = ...
_boundarydict = ...
def correlate(in1, in2, mode=..., method=...):
    r"""
    Cross-correlate two N-dimen"""
    ...

def correlation_lags(in1_len, in2_len, mode=...):
    r"""
    Calculates the lag / displa"""
    ...

def fftconvolve(in1, in2, mode=..., axes=...): # -> NDArray[bool_] | ndarray[Unknown, Unknown]:
    """Convolve two N-dimensional array"""
    ...

def oaconvolve(in1, in2, mode=..., axes=...):
    """Convolve two N-dimensional array"""
    ...

def choose_conv_method(in1, in2, mode=..., measure=...): # -> tuple[Literal['fft', 'direct'], dict[Unknown, Unknown]] | Literal['direct', 'fft']:
    """
    Find the fastest convolutio"""
    ...

def convolve(in1, in2, mode=..., method=...): # -> NDArray[bool_] | Any | NDArray[Unknown] | ndarray[Unknown, Unknown]:
    """
    Convolve two N-dimensional """
    ...

def order_filter(a, domain, rank): # -> Any:
    """
    Perform an order filter on """
    ...

def medfilt(volume, kernel_size=...): # -> Any:
    """
    Perform a median filter on """
    ...

def wiener(im, mysize=..., noise=...):
    """
    Perform a Wiener filter on """
    ...

def convolve2d(in1, in2, mode=..., boundary=..., fillvalue=...): # -> Any:
    """
    Convolve two 2-dimensional """
    ...

def correlate2d(in1, in2, mode=..., boundary=..., fillvalue=...): # -> Any:
    """
    Cross-correlate two 2-dimen"""
    ...

def medfilt2d(input, kernel_size=...): # -> Any:
    """
    Median filter a 2-dimension"""
    ...

def lfilter(b, a, x, axis=..., zi=...):
    """
    Filter data along one-dimen"""
    ...

def lfiltic(b, a, y, x=...): # -> ndarray[Unknown, Unknown]:
    """
    Construct initial condition"""
    ...

def deconvolve(signal, divisor): # -> tuple[Unknown | list[Unknown], ndarray[Unknown, Unknown] | Any | Unknown]:
    """Deconvolves ``divisor`` out of `"""
    ...

def hilbert(x, N=..., axis=...):
    """
    Compute the analytic signal"""
    ...

def hilbert2(x, N=...):
    """
    Compute the '2-D' analytic """
    ...

def cmplx_sort(p): # -> tuple[Any, ndarray[Unknown, Unknown]]:
    """Sort roots based on magnitude.

"""
    ...

def unique_roots(p, tol=..., rtype=...): # -> tuple[ndarray[Unknown, Unknown], ndarray[Unknown, Unknown]]:
    """Determine unique roots and their"""
    ...

def invres(r, p, k, tol=..., rtype=...): # -> tuple[Unknown | Literal[0], ndarray[Unknown, Unknown] | Unknown]:
    """Compute b(s) and a(s) from parti"""
    ...

def residue(b, a, tol=..., rtype=...): # -> tuple[ndarray[Unknown, Unknown], Any, ndarray[Unknown, Unknown]] | tuple[Unknown, Unknown, ndarray[Unknown, Unknown] | Unknown]:
    """Compute partial-fraction expansi"""
    ...

def residuez(b, a, tol=..., rtype=...): # -> tuple[ndarray[Unknown, Unknown], Any, ndarray[Unknown, Unknown]] | tuple[Unknown, Unknown, Any | Unknown]:
    """Compute partial-fraction expansi"""
    ...

def invresz(r, p, k, tol=..., rtype=...): # -> tuple[Unknown, ndarray[Unknown, Unknown] | Unknown]:
    """Compute b(z) and a(z) from parti"""
    ...

def resample(x, num, t=..., axis=..., window=..., domain=...):
    """
    Resample `x` to `num` sampl"""
    ...

def resample_poly(x, up, down, axis=..., window=..., padtype=..., cval=...):
    """
    Resample `x` along the give"""
    ...

def vectorstrength(events, period): # -> tuple[Any, Unknown]:
    '''
    Determine the vector streng'''
    ...

def detrend(data, axis=..., type=..., bp=..., overwrite_data=...): # -> Any | ndarray[Unknown, Unknown]:
    """
    Remove linear trend along a"""
    ...

def lfilter_zi(b, a):
    """
    Construct initial condition"""
    ...

def sosfilt_zi(sos): # -> ndarray[Unknown, Unknown]:
    """
    Construct initial condition"""
    ...

def filtfilt(b, a, x, axis=..., padtype=..., padlen=..., method=..., irlen=...):
    """
    Apply a digital filter forw"""
    ...

def sosfilt(sos, x, axis=..., zi=...): # -> tuple[ndarray[Unknown, Unknown], ndarray[Unknown, Unknown]] | ndarray[Unknown, Unknown]:
    """
    Filter data along one dimen"""
    ...

def sosfiltfilt(sos, x, axis=..., padtype=..., padlen=...):
    """
    A forward-backward digital """
    ...

def decimate(x, q, n=..., ftype=..., axis=..., zero_phase=...):
    """
    Downsample the signal after"""
    ...

