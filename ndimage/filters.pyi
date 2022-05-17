"""
This type stub file was generated by pyright.
"""

from . import _ni_docstrings

__all__ = ['correlate1d', 'convolve1d', 'gaussian_filter1d', 'gaussian_filter', 'prewitt', 'sobel', 'generic_laplace', 'laplace', 'gaussian_laplace', 'generic_gradient_magnitude', 'gaussian_gradient_magnitude', 'correlate', 'convolve', 'uniform_filter1d', 'uniform_filter', 'minimum_filter1d', 'maximum_filter1d', 'minimum_filter', 'maximum_filter', 'rank_filter', 'median_filter', 'percentile_filter', 'generic_filter1d', 'generic_filter']
@_ni_docstrings.docfiller
def correlate1d(input, weights, axis=..., output=..., mode=..., cval=..., origin=...):
    """Calculate a 1-D correlation alon"""
    ...

@_ni_docstrings.docfiller
def convolve1d(input, weights, axis=..., output=..., mode=..., cval=..., origin=...):
    """Calculate a 1-D convolution alon"""
    ...

@_ni_docstrings.docfiller
def gaussian_filter1d(input, sigma, axis=..., order=..., output=..., mode=..., cval=..., truncate=...):
    """1-D Gaussian filter.

    Parame"""
    ...

@_ni_docstrings.docfiller
def gaussian_filter(input, sigma, order=..., output=..., mode=..., cval=..., truncate=...):
    """Multidimensional Gaussian filter"""
    ...

@_ni_docstrings.docfiller
def prewitt(input, axis=..., output=..., mode=..., cval=...):
    """Calculate a Prewitt filter.

   """
    ...

@_ni_docstrings.docfiller
def sobel(input, axis=..., output=..., mode=..., cval=...):
    """Calculate a Sobel filter.

    P"""
    ...

@_ni_docstrings.docfiller
def generic_laplace(input, derivative2, output=..., mode=..., cval=..., extra_arguments=..., extra_keywords=...):
    """
    N-D Laplace filter using a """
    ...

@_ni_docstrings.docfiller
def laplace(input, output=..., mode=..., cval=...):
    """N-D Laplace filter based on appr"""
    ...

@_ni_docstrings.docfiller
def gaussian_laplace(input, sigma, output=..., mode=..., cval=..., **kwargs):
    """Multidimensional Laplace filter """
    ...

@_ni_docstrings.docfiller
def generic_gradient_magnitude(input, derivative, output=..., mode=..., cval=..., extra_arguments=..., extra_keywords=...):
    """Gradient magnitude using a provi"""
    ...

@_ni_docstrings.docfiller
def gaussian_gradient_magnitude(input, sigma, output=..., mode=..., cval=..., **kwargs):
    """Multidimensional gradient magnit"""
    ...

@_ni_docstrings.docfiller
def correlate(input, weights, output=..., mode=..., cval=..., origin=...):
    """
    Multidimensional correlatio"""
    ...

@_ni_docstrings.docfiller
def convolve(input, weights, output=..., mode=..., cval=..., origin=...):
    """
    Multidimensional convolutio"""
    ...

@_ni_docstrings.docfiller
def uniform_filter1d(input, size, axis=..., output=..., mode=..., cval=..., origin=...):
    """Calculate a 1-D uniform filter a"""
    ...

@_ni_docstrings.docfiller
def uniform_filter(input, size=..., output=..., mode=..., cval=..., origin=...):
    """Multidimensional uniform filter."""
    ...

@_ni_docstrings.docfiller
def minimum_filter1d(input, size, axis=..., output=..., mode=..., cval=..., origin=...):
    """Calculate a 1-D minimum filter a"""
    ...

@_ni_docstrings.docfiller
def maximum_filter1d(input, size, axis=..., output=..., mode=..., cval=..., origin=...):
    """Calculate a 1-D maximum filter a"""
    ...

@_ni_docstrings.docfiller
def minimum_filter(input, size=..., footprint=..., output=..., mode=..., cval=..., origin=...):
    """Calculate a multidimensional min"""
    ...

@_ni_docstrings.docfiller
def maximum_filter(input, size=..., footprint=..., output=..., mode=..., cval=..., origin=...):
    """Calculate a multidimensional max"""
    ...

@_ni_docstrings.docfiller
def rank_filter(input, rank, size=..., footprint=..., output=..., mode=..., cval=..., origin=...):
    """Calculate a multidimensional ran"""
    ...

@_ni_docstrings.docfiller
def median_filter(input, size=..., footprint=..., output=..., mode=..., cval=..., origin=...):
    """
    Calculate a multidimensiona"""
    ...

@_ni_docstrings.docfiller
def percentile_filter(input, percentile, size=..., footprint=..., output=..., mode=..., cval=..., origin=...):
    """Calculate a multidimensional per"""
    ...

@_ni_docstrings.docfiller
def generic_filter1d(input, function, filter_size, axis=..., output=..., mode=..., cval=..., origin=..., extra_arguments=..., extra_keywords=...):
    """Calculate a 1-D filter along the"""
    ...

@_ni_docstrings.docfiller
def generic_filter(input, function, size=..., footprint=..., output=..., mode=..., cval=..., origin=..., extra_arguments=..., extra_keywords=...):
    """Calculate a multidimensional fil"""
    ...
