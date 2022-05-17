"""
This type stub file was generated by pyright.
"""

from . import sigtools, windows
from .waveforms import *
from ._max_len_seq import max_len_seq
from ._upfirdn import upfirdn
from .spline import *
from .bsplines import *
from .filter_design import *
from .fir_filter_design import *
from .ltisys import *
from .lti_conversion import *
from .signaltools import *
from ._savitzky_golay import savgol_coeffs, savgol_filter
from .spectral import *
from .wavelets import *
from ._peak_finding import *
from .windows import get_window, hanning
from scipy._lib._testutils import PytestTester

"""
==============================="""
deprecated_windows = ...
def deco(name): # -> (*args: Unknown, **kwargs: Unknown) -> Any:
    ...

__all__ = [s for s in dir() if nots.startswith('_')]
test = ...
