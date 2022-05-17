"""
This type stub file was generated by pyright.
"""

import sys

r"""
==============================="""
_DTYPE_ERROR = ...
_TYPE_ERROR = ...
_32BIT_ERROR = ...
_IS_32BIT = (sys.maxsize < 2 ** 32)
def seed(seed=...): # -> None:
    """
    Seed the internal random nu"""
    ...

def rand(*shape): # -> Any:
    """
    Generate standard uniform p"""
    ...

def interp_decomp(A, eps_or_k, rand=...):
    """
    Compute ID of a matrix.

  """
    ...

def reconstruct_matrix_from_id(B, idx, proj): # -> Any:
    """
    Reconstruct matrix from its"""
    ...

def reconstruct_interp_matrix(idx, proj): # -> Any:
    """
    Reconstruct interpolation m"""
    ...

def reconstruct_skel_matrix(A, k, idx): # -> Any:
    """
    Reconstruct skeleton matrix"""
    ...

def id_to_svd(B, idx, proj): # -> tuple[Any, Any, Any]:
    """
    Convert ID to SVD.

    The"""
    ...

def estimate_spectral_norm(A, its=...): # -> Any:
    """
    Estimate spectral norm of a"""
    ...

def estimate_spectral_norm_diff(A, B, its=...): # -> Any:
    """
    Estimate spectral norm of t"""
    ...

def svd(A, eps_or_k, rand=...):
    """
    Compute SVD of a matrix via"""
    ...

def estimate_rank(A, eps): # -> int | Any:
    """
    Estimate matrix rank to a s"""
    ...
