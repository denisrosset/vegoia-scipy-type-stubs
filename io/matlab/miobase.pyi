"""
This type stub file was generated by pyright.
"""

"""
Base classes for MATLAB file st"""
class MatReadError(Exception):
    ...


class MatWriteError(Exception):
    ...


class MatReadWarning(UserWarning):
    ...


doc_dict = ...
docfiller = ...
def convert_dtypes(dtype_template, order_code):
    ''' Convert dtypes in mapping to gi'''
    ...

def read_dtype(mat_stream, a_dtype): # -> ndarray[_ShapeType@ndarray, _DType_co@ndarray]:
    """
    Generic get of byte stream """
    ...

def get_matfile_version(fileobj): # -> tuple[Literal[0], Literal[0]] | tuple[int, int]:
    """
    Return major, minor tuple d"""
    ...

def matdims(arr, oned_as=...): # -> tuple[Literal[1], Literal[1]] | tuple[Literal[0], Literal[0]]:
    """
    Determine equivalent MATLAB"""
    ...

class MatVarReader:
    ''' Abstract class defining require'''
    def __init__(self, file_reader) -> None:
        ...
    
    def read_header(self): # -> None:
        ''' Returns header '''
        ...
    
    def array_from_header(self, header): # -> None:
        ''' Reads array given header '''
        ...
    


class MatFileReader:
    """ Base object for reading mat fil"""
    @docfiller
    def __init__(self, mat_stream, byte_order=..., mat_dtype=..., squeeze_me=..., chars_as_strings=..., matlab_compatible=..., struct_as_record=..., verify_compressed_data_integrity=..., simplify_cells=...) -> None:
        '''
        Initializer for mat fil'''
        ...
    
    def set_matlab_compatible(self): # -> None:
        ''' Sets options to return arrays a'''
        ...
    
    def guess_byte_order(self): # -> str:
        ''' As we do not know what file typ'''
        ...
    
    def end_of_stream(self): # -> bool:
        ...
    


def arr_dtype_number(arr, num): # -> dtype[Unknown]:
    ''' Return dtype for given number o'''
    ...

def arr_to_chars(arr): # -> ndarray[_ShapeType@ndarray, _DType_co@ndarray]:
    ''' Convert string array to char ar'''
    ...
