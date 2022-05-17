"""
This type stub file was generated by pyright.
"""

"""
Fundamental Physical Constants
"""
__all__ = ['physical_constants', 'value', 'unit', 'precision', 'find', 'ConstantWarning']
txt2002 = ...
txt2006 = ...
txt2010 = ...
txt2014 = ...
txt2018 = ...
physical_constants = ...
def parse_constants_2002to2014(d): # -> dict[Unknown, Unknown]:
    ...

def parse_constants_2018toXXXX(d): # -> dict[Unknown, Unknown]:
    ...

_physical_constants_2002 = ...
_physical_constants_2006 = ...
_physical_constants_2010 = ...
_physical_constants_2014 = ...
_physical_constants_2018 = ...
_current_constants = ...
_current_codata = ...
_obsolete_constants = ...
_aliases = ...
class ConstantWarning(DeprecationWarning):
    """Accessing a constant no longer i"""
    ...


def value(key):
    """
    Value in physical_constants"""
    ...

def unit(key):
    """
    Unit in physical_constants """
    ...

def precision(key):
    """
    Relative precision in physi"""
    ...

def find(sub=..., disp=...): # -> list[Unknown] | None:
    """
    Return list of physical_con"""
    ...

c = ...
mu0 = ...
epsilon0 = ...
exact_values = ...
_tested_keys = ...
