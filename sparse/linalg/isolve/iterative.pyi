"""
This type stub file was generated by pyright.
"""

from scipy._lib._threadsafety import non_reentrant

"""Iterative methods for solving li"""
__all__ = ['bicg', 'bicgstab', 'cg', 'cgs', 'gmres', 'qmr']
_type_conv = ...
common_doc1 = ...
common_doc2 = ...
def set_docstring(header, Ainfo, footer=..., atol_default=...): # -> (fn: Unknown) -> Unknown:
    ...

@set_docstring('Use BIConjugate Gradient iterati', 'The real or complex N-by-N matri' 'Alternatively, ``A`` can be a li' 'produce ``Ax`` and ``A^T x`` usi' '``scipy.sparse.linalg.LinearOper', footer="""
               
               """)
@non_reentrant()
def bicg(A, b, x0=..., tol=..., maxiter=..., M=..., callback=..., atol=...):
    ...

@set_docstring('Use BIConjugate Gradient STABili' '``Ax = b``.', 'The real or complex N-by-N matri' 'Alternatively, ``A`` can be a li' 'produce ``Ax`` using, e.g.,\n' '``scipy.sparse.linalg.LinearOper')
@non_reentrant()
def bicgstab(A, b, x0=..., tol=..., maxiter=..., M=..., callback=..., atol=...):
    ...

@set_docstring('Use Conjugate Gradient iteration', 'The real or complex N-by-N matri' '``A`` must represent a hermitian' 'Alternatively, ``A`` can be a li' 'produce ``Ax`` using, e.g.,\n' '``scipy.sparse.linalg.LinearOper')
@non_reentrant()
def cg(A, b, x0=..., tol=..., maxiter=..., M=..., callback=..., atol=...):
    ...

@set_docstring('Use Conjugate Gradient Squared i', 'The real-valued N-by-N matrix of' 'Alternatively, ``A`` can be a li' 'produce ``Ax`` using, e.g.,\n' '``scipy.sparse.linalg.LinearOper')
@non_reentrant()
def cgs(A, b, x0=..., tol=..., maxiter=..., M=..., callback=..., atol=...):
    ...

@non_reentrant()
def gmres(A, b, x0=..., tol=..., restart=..., maxiter=..., M=..., callback=..., restrt=..., atol=..., callback_type=...):
    """
    Use Generalized Minimal RES"""
    ...

@non_reentrant()
def qmr(A, b, x0=..., tol=..., maxiter=..., M1=..., M2=..., callback=..., atol=...):
    """Use Quasi-Minimal Residual itera"""
    ...
