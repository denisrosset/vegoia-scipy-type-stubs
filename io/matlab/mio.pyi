"""
This type stub file was generated by pyright.
"""

from .miobase import docfiller

"""
Module for reading and writing """
__all__ = ['mat_reader_factory', 'loadmat', 'savemat', 'whosmat']
@docfiller
def mat_reader_factory(file_name, appendmat=..., **kwargs): # -> tuple[MatFile4Reader, bool] | tuple[MatFile5Reader, bool]:
    """
    Create reader for matlab .m"""
    ...

@docfiller
def loadmat(file_name, mdict=..., appendmat=..., **kwargs): # -> dict[Unknown, Unknown]:
    """
    Load MATLAB file.

    Para"""
    ...

@docfiller
def savemat(file_name, mdict, appendmat=..., format=..., long_field_names=..., do_compression=..., oned_as=...): # -> None:
    """
    Save a dictionary of names """
    ...

@docfiller
def whosmat(file_name, appendmat=..., **kwargs): # -> list[Unknown]:
    """
    List variables inside a MAT"""
    ...

