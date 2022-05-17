"""
This type stub file was generated by pyright.
"""

import numpy as np
from typing import Optional, Union

"""
Created on Fri Apr  2 09:06:05 """
__all__ = ['entropy', 'differential_entropy']
def entropy(pk, qk=..., base=..., axis=...): # -> Any:
    """Calculate the entropy of a distr"""
    ...

def differential_entropy(values: np.typing.ArrayLike, *, window_length: Optional[int] = ..., base: Optional[float] = ..., axis: int = ..., method: str = ...) -> Union[np.number, np.ndarray]:
    r"""Given a sample of a distribution"""
    ...
