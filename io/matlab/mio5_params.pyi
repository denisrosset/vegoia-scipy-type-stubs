"""
This type stub file was generated by pyright.
"""

import numpy as np

''' Constants and classes for matla'''
miINT8 = ...
miUINT8 = ...
miINT16 = ...
miUINT16 = ...
miINT32 = ...
miUINT32 = ...
miSINGLE = ...
miDOUBLE = ...
miINT64 = ...
miUINT64 = ...
miMATRIX = ...
miCOMPRESSED = ...
miUTF8 = ...
miUTF16 = ...
miUTF32 = ...
mxCELL_CLASS = ...
mxSTRUCT_CLASS = ...
mxOBJECT_CLASS = ...
mxCHAR_CLASS = ...
mxSPARSE_CLASS = ...
mxDOUBLE_CLASS = ...
mxSINGLE_CLASS = ...
mxINT8_CLASS = ...
mxUINT8_CLASS = ...
mxINT16_CLASS = ...
mxUINT16_CLASS = ...
mxINT32_CLASS = ...
mxUINT32_CLASS = ...
mxINT64_CLASS = ...
mxUINT64_CLASS = ...
mxFUNCTION_CLASS = ...
mxOPAQUE_CLASS = ...
mxOBJECT_CLASS_FROM_MATRIX_H = ...
mdtypes_template = ...
mclass_dtypes_template = ...
mclass_info = ...
NP_TO_MTYPES = ...
NP_TO_MXTYPES = ...
codecs_template = ...
MDTYPES = ...
class mat_struct:
    ''' Placeholder for holding read da'''
    ...


class MatlabObject(np.ndarray):
    ''' ndarray Subclass to contain mat'''
    def __new__(cls, input_array, classname=...): # -> Self@MatlabObject:
        ...
    
    def __array_finalize__(self, obj): # -> None:
        ...
    


class MatlabFunction(np.ndarray):
    ''' Subclass to signal this is a ma'''
    def __new__(cls, input_array): # -> Self@MatlabFunction:
        ...
    


class MatlabOpaque(np.ndarray):
    ''' Subclass to signal this is a ma'''
    def __new__(cls, input_array): # -> Self@MatlabOpaque:
        ...
    


OPAQUE_DTYPE = ...