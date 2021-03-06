"""
This type stub file was generated by pyright.
"""

"""Matrix equation solver routines"""
__all__ = ['solve_sylvester', 'solve_continuous_lyapunov', 'solve_discrete_lyapunov', 'solve_lyapunov', 'solve_continuous_are', 'solve_discrete_are']
def solve_sylvester(a, b, q):
    """
    Computes a solution (X) to """
    ...

def solve_continuous_lyapunov(a, q):
    """
    Solves the continuous Lyapu"""
    ...

solve_lyapunov = ...
def solve_discrete_lyapunov(a, q, method=...): # -> ndarray[Unknown, Unknown]:
    """
    Solves the discrete Lyapuno"""
    ...

def solve_continuous_are(a, b, q, r, e=..., s=..., balanced=...):
    r"""
    Solves the continuous-time """
    ...

def solve_discrete_are(a, b, q, r, e=..., s=..., balanced=...):
    r"""
    Solves the discrete-time al"""
    ...

