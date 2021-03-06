"""
This type stub file was generated by pyright.
"""

from .data import _data_matrix, _minmax_mixin
from ._index import IndexMixin

"""Base class for sparse matrix for"""
__all__ = []
class _cs_matrix(_data_matrix, _minmax_mixin, IndexMixin):
    """base matrix class for compressed"""
    def __init__(self, arg1, shape=..., dtype=..., copy=...) -> None:
        ...
    
    def getnnz(self, axis=...): # -> int | tuple[Unknown, Unknown | None]:
        ...
    
    def check_format(self, full_check=...): # -> None:
        """check whether the matrix format """
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def multiply(self, other):
        """Point-wise multiplication by ano"""
        ...
    
    def diagonal(self, k=...): # -> ndarray[Unknown, Unknown]:
        ...
    
    def maximum(self, other): # -> Self@_cs_matrix | NDArray[Any]:
        ...
    
    def minimum(self, other): # -> Self@_cs_matrix | NDArray[Any]:
        ...
    
    def sum(self, axis=..., dtype=..., out=...):
        """Sum the matrix over the given ax"""
        ...
    
    def tocoo(self, copy=...): # -> coo_matrix:
        ...
    
    def toarray(self, order=..., out=...): # -> ndarray[Unknown, Unknown]:
        ...
    
    def eliminate_zeros(self): # -> None:
        """Remove zero entries from the mat"""
        ...
    
    has_canonical_format = ...
    def sum_duplicates(self): # -> None:
        """Eliminate duplicate matrix entri"""
        ...
    
    has_sorted_indices = ...
    def sorted_indices(self):
        """Return a copy of this matrix wit"""
        ...
    
    def sort_indices(self): # -> None:
        """Sort the indices of this matrix """
        ...
    
    def prune(self): # -> None:
        """Remove empty space after all non"""
        ...
    
    def resize(self, *shape): # -> None:
        ...
    


