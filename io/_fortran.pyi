"""
This type stub file was generated by pyright.
"""

"""
Module to read / write Fortran """
__all__ = ['FortranFile', 'FortranEOFError', 'FortranFormattingError']
class FortranEOFError(TypeError, IOError):
    """Indicates that the file ended pr"""
    ...


class FortranFormattingError(TypeError, IOError):
    """Indicates that the file ended mi"""
    ...


class FortranFile:
    """
    A file object for unformatt"""
    def __init__(self, filename, mode=..., header_dtype=...) -> None:
        ...
    
    def write_record(self, *items): # -> None:
        """
        Write a record (includi"""
        ...
    
    def read_record(self, *dtypes, **kwargs): # -> tuple[Unknown, ...]:
        """
        Reads a record of a giv"""
        ...
    
    def read_ints(self, dtype=...): # -> tuple[Unknown, ...]:
        """
        Reads a record of a giv"""
        ...
    
    def read_reals(self, dtype=...): # -> tuple[Unknown, ...]:
        """
        Reads a record of a giv"""
        ...
    
    def close(self): # -> None:
        """
        Closes the file. It is """
        ...
    
    def __enter__(self): # -> Self@FortranFile:
        ...
    
    def __exit__(self, type, value, tb): # -> None:
        ...
    


