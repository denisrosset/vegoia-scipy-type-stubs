"""
This type stub file was generated by pyright.
"""

from .base import spmatrix
from ._index import IndexMixin

"""List of Lists sparse matrix clas"""
__docformat__ = ...
__all__ = ['lil_matrix', 'isspmatrix_lil']
class lil_matrix(spmatrix, IndexMixin):
    """Row-based list of lists sparse m"""
    format = ...
    def __init__(self, arg1, shape=..., dtype=..., copy=...) -> None:
        ...
    
    def __iadd__(self, other): # -> Self@lil_matrix:
        ...
    
    def __isub__(self, other): # -> Self@lil_matrix:
        ...
    
    def __imul__(self, other): # -> Self@lil_matrix | _NotImplementedType:
        ...
    
    def __itruediv__(self, other): # -> Self@lil_matrix | _NotImplementedType:
        ...
    
    def getnnz(self, axis=...): # -> int | ndarray[Unknown, Unknown]:
        ...
    
    def count_nonzero(self): # -> int:
        ...
    
    def __str__(self) -> str:
        ...
    
    def getrowview(self, i): # -> lil_matrix:
        """Returns a view of the 'i'th row """
        ...
    
    def getrow(self, i): # -> lil_matrix:
        """Returns a copy of the 'i'th row."""
        ...
    
    def __getitem__(self, key):
        ...
    
    def __setitem__(self, key, x): # -> None:
        ...
    
    def __truediv__(self, other): # -> lil_matrix:
        ...
    
    def copy(self): # -> lil_matrix:
        ...
    
    def reshape(self, *args, **kwargs): # -> lil_matrix | Self@lil_matrix:
        ...
    
    def resize(self, *shape): # -> None:
        ...
    
    def toarray(self, order=..., out=...): # -> ndarray[Unknown, Unknown]:
        ...
    
    def transpose(self, axes=..., copy=...):
        ...
    
    def tolil(self, copy=...): # -> lil_matrix | Self@lil_matrix:
        ...
    
    def tocsr(self, copy=...): # -> csr_matrix:
        ...
    


def isspmatrix_lil(x): # -> bool:
    """Is x of lil_matrix type?

    Pa"""
    ...

