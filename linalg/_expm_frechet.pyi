"""
This type stub file was generated by pyright.
"""

"""Frechet derivative of the matrix"""
__all__ = ['expm_frechet', 'expm_cond']
def expm_frechet(A, E, method=..., compute_expm=..., check_finite=...): # -> tuple[Unknown, Unknown]:
    """
    Frechet derivative of the m"""
    ...

def expm_frechet_block_enlarge(A, E): # -> tuple[Unknown, Unknown]:
    """
    This is a helper function, """
    ...

ell_table_61 = ...
def expm_frechet_algo_64(A, E): # -> tuple[Unknown, Unknown]:
    ...

def vec(M):
    """
    Stack columns of M to const"""
    ...

def expm_frechet_kronform(A, method=..., check_finite=...): # -> ndarray[Unknown, Unknown]:
    """
    Construct the Kronecker for"""
    ...

def expm_cond(A, check_finite=...):
    """
    Relative condition number o"""
    ...
