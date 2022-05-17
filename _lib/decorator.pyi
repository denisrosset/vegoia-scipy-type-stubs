"""
This type stub file was generated by pyright.
"""

"""
Decorator module, see https://p"""
__version__ = ...
def get_init(cls):
    ...

ArgSpec = ...
def getargspec(f): # -> ArgSpec:
    """A replacement for inspect.getarg"""
    ...

DEF = ...
class FunctionMaker:
    """
    An object with the ability """
    _compile_count = ...
    def __init__(self, func=..., name=..., signature=..., defaults=..., doc=..., module=..., funcdict=...) -> None:
        ...
    
    def update(self, func, **kw): # -> None:
        "Update the signature of func wit"
        ...
    
    def make(self, src_templ, evaldict=..., addsource=..., **attrs): # -> Any:
        "Make a new function from a given"
        ...
    
    @classmethod
    def create(cls, obj, body, evaldict, defaults=..., doc=..., module=..., addsource=..., **attrs): # -> Any:
        """
        Create a function from """
        ...
    


def decorate(func, caller): # -> Any:
    """
    decorate(func, caller) deco"""
    ...

def decorator(caller, _func=...): # -> Any:
    """decorator(caller) converts a cal"""
    ...

class ContextManager(_GeneratorContextManager):
    def __call__(self, func): # -> Any:
        """Context manager decorator"""
        ...
    


init = ...
n_args = ...
if n_args == 2 and notinit.varargs:
    def __init__(self, g, *a, **k) -> None:
        ...
    
else:
    ...
contextmanager = ...
def append(a, vancestors): # -> None:
    """
    Append ``a`` to the list of"""
    ...

def dispatch_on(*dispatch_args): # -> (func: Unknown) -> (Unknown | Any):
    """
    Factory of decorators turni"""
    ...
