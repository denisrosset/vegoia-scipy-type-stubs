"""
This type stub file was generated by pyright.
"""

import numpy as _np
from .blas import _memoize_get_funcs
from scipy.linalg._flapack import *

"""
Low-level LAPACK functions (:mo"""
clapack = ...
flapack = ...
empty_module = ...
__all__ = ['get_lapack_funcs']
_dep_message = ...
cgegv = ...
dgegv = ...
sgegv = ...
zgegv = ...
_lapack_alias = ...
p1 = ...
p2 = ...
def backtickrepl(m): # -> str:
    ...

@_memoize_get_funcs
def get_lapack_funcs(names, arrays=..., dtype=..., ilp64=...): # -> list[Unknown]:
    """Return available LAPACK function"""
    ...

_int32_max = _np.iinfo(_np.int32).max
_int64_max = _np.iinfo(_np.int64).max
