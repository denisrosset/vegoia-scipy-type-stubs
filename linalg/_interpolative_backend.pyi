"""
This type stub file was generated by pyright.
"""

"""
Direct wrappers for Fortran `id"""
_RETCODE_ERROR = ...
def id_srand(n): # -> Any:
    """
    Generate standard uniform p"""
    ...

def id_srandi(t): # -> None:
    """
    Initialize seed values for """
    ...

def id_srando(): # -> None:
    """
    Reset seed values to their """
    ...

def idd_frm(n, w, x): # -> Any:
    """
    Transform real vector via a"""
    ...

def idd_sfrm(l, n, w, x): # -> Any:
    """
    Transform real vector via a"""
    ...

def idd_frmi(m): # -> Any:
    """
    Initialize data for :func:`"""
    ...

def idd_sfrmi(l, m): # -> Any:
    """
    Initialize data for :func:`"""
    ...

def iddp_id(eps, A): # -> tuple[Any, Any, Any]:
    """
    Compute ID of a real matrix"""
    ...

def iddr_id(A, k): # -> tuple[Any, Any]:
    """
    Compute ID of a real matrix"""
    ...

def idd_reconid(B, idx, proj): # -> Any:
    """
    Reconstruct matrix from rea"""
    ...

def idd_reconint(idx, proj): # -> Any:
    """
    Reconstruct interpolation m"""
    ...

def idd_copycols(A, k, idx): # -> Any:
    """
    Reconstruct skeleton matrix"""
    ...

def idd_id2svd(B, idx, proj): # -> tuple[Any, Any, Any]:
    """
    Convert real ID to SVD.

  """
    ...

def idd_snorm(m, n, matvect, matvec, its=...): # -> Any:
    """
    Estimate spectral norm of a"""
    ...

def idd_diffsnorm(m, n, matvect, matvect2, matvec, matvec2, its=...): # -> Any:
    """
    Estimate spectral norm of t"""
    ...

def iddr_svd(A, k): # -> tuple[Any, Any, Any]:
    """
    Compute SVD of a real matri"""
    ...

def iddp_svd(eps, A): # -> tuple[Any, Any, Any]:
    """
    Compute SVD of a real matri"""
    ...

def iddp_aid(eps, A): # -> tuple[Any, Any, Any]:
    """
    Compute ID of a real matrix"""
    ...

def idd_estrank(eps, A): # -> Any:
    """
    Estimate rank of a real mat"""
    ...

def iddp_asvd(eps, A): # -> tuple[Any, Any, Any]:
    """
    Compute SVD of a real matri"""
    ...

def iddp_rid(eps, m, n, matvect): # -> tuple[Any, Any, Any]:
    """
    Compute ID of a real matrix"""
    ...

def idd_findrank(eps, m, n, matvect): # -> Any:
    """
    Estimate rank of a real mat"""
    ...

def iddp_rsvd(eps, m, n, matvect, matvec): # -> tuple[Any, Any, Any]:
    """
    Compute SVD of a real matri"""
    ...

def iddr_aid(A, k): # -> tuple[Any, ndarray[Unknown, Unknown] | Any]:
    """
    Compute ID of a real matrix"""
    ...

def iddr_aidi(m, n, k): # -> Any:
    """
    Initialize array for :func:"""
    ...

def iddr_asvd(A, k): # -> tuple[Any, Any, Any]:
    """
    Compute SVD of a real matri"""
    ...

def iddr_rid(m, n, matvect, k): # -> tuple[Any, Any]:
    """
    Compute ID of a real matrix"""
    ...

def iddr_rsvd(m, n, matvect, matvec, k): # -> tuple[Any, Any, Any]:
    """
    Compute SVD of a real matri"""
    ...

def idz_frm(n, w, x): # -> Any:
    """
    Transform complex vector vi"""
    ...

def idz_sfrm(l, n, w, x): # -> Any:
    """
    Transform complex vector vi"""
    ...

def idz_frmi(m): # -> Any:
    """
    Initialize data for :func:`"""
    ...

def idz_sfrmi(l, m): # -> Any:
    """
    Initialize data for :func:`"""
    ...

def idzp_id(eps, A): # -> tuple[Any, Any, Any]:
    """
    Compute ID of a complex mat"""
    ...

def idzr_id(A, k): # -> tuple[Any, Any]:
    """
    Compute ID of a complex mat"""
    ...

def idz_reconid(B, idx, proj): # -> Any:
    """
    Reconstruct matrix from com"""
    ...

def idz_reconint(idx, proj): # -> Any:
    """
    Reconstruct interpolation m"""
    ...

def idz_copycols(A, k, idx): # -> Any:
    """
    Reconstruct skeleton matrix"""
    ...

def idz_id2svd(B, idx, proj): # -> tuple[Any, Any, Any]:
    """
    Convert complex ID to SVD.
"""
    ...

def idz_snorm(m, n, matveca, matvec, its=...): # -> Any:
    """
    Estimate spectral norm of a"""
    ...

def idz_diffsnorm(m, n, matveca, matveca2, matvec, matvec2, its=...): # -> Any:
    """
    Estimate spectral norm of t"""
    ...

def idzr_svd(A, k): # -> tuple[Any, Any, Any]:
    """
    Compute SVD of a complex ma"""
    ...

def idzp_svd(eps, A): # -> tuple[Any, Any, Any]:
    """
    Compute SVD of a complex ma"""
    ...

def idzp_aid(eps, A): # -> tuple[Any, Any, Any]:
    """
    Compute ID of a complex mat"""
    ...

def idz_estrank(eps, A): # -> Any:
    """
    Estimate rank of a complex """
    ...

def idzp_asvd(eps, A): # -> tuple[Any, Any, Any]:
    """
    Compute SVD of a complex ma"""
    ...

def idzp_rid(eps, m, n, matveca): # -> tuple[Any, Any, Any]:
    """
    Compute ID of a complex mat"""
    ...

def idz_findrank(eps, m, n, matveca): # -> Any:
    """
    Estimate rank of a complex """
    ...

def idzp_rsvd(eps, m, n, matveca, matvec): # -> tuple[Any, Any, Any]:
    """
    Compute SVD of a complex ma"""
    ...

def idzr_aid(A, k): # -> tuple[Any, ndarray[Unknown, Unknown] | Any]:
    """
    Compute ID of a complex mat"""
    ...

def idzr_aidi(m, n, k): # -> Any:
    """
    Initialize array for :func:"""
    ...

def idzr_asvd(A, k): # -> tuple[Any, Any, Any]:
    """
    Compute SVD of a complex ma"""
    ...

def idzr_rid(m, n, matveca, k): # -> tuple[Any, Any]:
    """
    Compute ID of a complex mat"""
    ...

def idzr_rsvd(m, n, matveca, matvec, k): # -> tuple[Any, Any, Any]:
    """
    Compute SVD of a complex ma"""
    ...

