"""
This type stub file was generated by pyright.
"""

PyCFuncPtr = ...
ffi = ...
class CData:
    ...


class LowLevelCallable(tuple):
    """
    Low-level callback function"""
    __slots__ = ...
    def __new__(cls, function, user_data=..., signature=...): # -> Self@LowLevelCallable:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    @property
    def function(self): # -> _T_co@tuple:
        ...
    
    @property
    def user_data(self): # -> _T_co@tuple:
        ...
    
    @property
    def signature(self):
        ...
    
    def __getitem__(self, idx):
        ...
    
    @classmethod
    def from_cython(cls, module, name, user_data=..., signature=...): # -> Self@LowLevelCallable:
        """
        Create a low-level call"""
        ...
    

