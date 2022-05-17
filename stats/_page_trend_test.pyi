"""
This type stub file was generated by pyright.
"""

PageTrendTestResult = ...
def page_trend_test(data, ranked=..., predicted_ranks=..., method=...): # -> Any:
    r"""
    Perform Page's Test, a meas"""
    ...

class _PageL:
    '''Maintains state between `page_tr'''
    def __init__(self) -> None:
        '''Lightweight initialization'''
        ...
    
    def set_k(self, k): # -> None:
        '''Calculate lower and upper limits'''
        ...
    
    def sf(self, l, n): # -> Any:
        '''Survival function of Page's L st'''
        ...
    
    def p_l_k_1(self):
        '''Relative frequency of each L val'''
        ...
    
    def pmf(self, l, n): # -> Literal[0]:
        '''Recursive function to evaluate p'''
        ...
    


_pagel_state = ...