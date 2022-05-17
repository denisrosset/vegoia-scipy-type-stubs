"""
This type stub file was generated by pyright.
"""

"""
shgo: The simplicial homology g"""
__all__ = ['shgo']
def shgo(func, bounds, args=..., constraints=..., n=..., iters=..., callback=..., minimizer_kwargs=..., options=..., sampling_method=...): # -> OptimizeResult:
    """
    Finds the global minimum of"""
    ...

class SHGO:
    def __init__(self, func, bounds, args=..., constraints=..., n=..., iters=..., callback=..., minimizer_kwargs=..., options=..., sampling_method=...) -> None:
        ...
    
    def init_options(self, options): # -> None:
        """
        Initiates the options.
"""
        ...
    
    def construct_complex(self): # -> None:
        """
        Construct for `iters` i"""
        ...
    
    def find_minima(self): # -> None:
        """
        Construct the minimizer"""
        ...
    
    def find_lowest_vertex(self): # -> None:
        ...
    
    def finite_iterations(self): # -> bool:
        ...
    
    def finite_fev(self): # -> bool:
        ...
    
    def finite_ev(self): # -> None:
        ...
    
    def finite_time(self): # -> None:
        ...
    
    def finite_precision(self): # -> bool:
        """
        Stop the algorithm if t"""
        ...
    
    def finite_homology_growth(self): # -> bool | None:
        ...
    
    def stopping_criteria(self): # -> None:
        """
        Various stopping criter"""
        ...
    
    def iterate(self): # -> None:
        ...
    
    def iterate_hypercube(self): # -> None:
        """
        Iterate a subdivision o"""
        ...
    
    def iterate_delaunay(self): # -> None:
        """
        Build a complex of Dela"""
        ...
    
    def simplex_minimizers(self): # -> ndarray[Unknown, Unknown]:
        """
        Returns the indexes of """
        ...
    
    def minimise_pool(self, force_iter=...): # -> None:
        """
        This processing method """
        ...
    
    def sort_min_pool(self): # -> None:
        ...
    
    def trim_min_pool(self, trim_ind): # -> None:
        ...
    
    def g_topograph(self, x_min, X_min):
        """
        Returns the topographic"""
        ...
    
    def construct_lcb_simplicial(self, v_min): # -> list[list[Unknown | Any]]:
        """
        Construct locally (appr"""
        ...
    
    def construct_lcb_delaunay(self, v_min, ind=...): # -> list[list[Unknown | Any]]:
        """
        Construct locally (appr"""
        ...
    
    def minimize(self, x_min, ind=...):
        """
        This function is used t"""
        ...
    
    def sort_result(self): # -> OptimizeResult:
        """
        Sort results and build """
        ...
    
    def fail_routine(self, mes=...): # -> None:
        ...
    
    def sampled_surface(self, infty_cons_sampl=...): # -> None:
        """
        Sample the function sur"""
        ...
    
    def delaunay_complex_minimisers(self): # -> None:
        ...
    
    def sampling_custom(self, n, dim): # -> ndarray[Unknown, Unknown]:
        """
        Generates uniform sampl"""
        ...
    
    def sampling_subspace(self): # -> None:
        """Find subspace of feasible points"""
        ...
    
    def sorted_samples(self): # -> tuple[ndarray[Unknown, Unknown], Any | Unknown]:
        """Find indexes of the sorted sampl"""
        ...
    
    def ax_subspace(self): # -> None:
        """
        Finds the subspace vect"""
        ...
    
    def fun_ref(self): # -> ndarray[Unknown, Unknown]:
        """
        Find the objective func"""
        ...
    
    def surface_topo_ref(self): # -> None:
        """
        Find the BD and FD fini"""
        ...
    
    def sample_topo(self, ind): # -> bool_:
        ...
    
    def minimizers_1D(self): # -> Any | list[Unknown]:
        """
        Returns the indices of """
        ...
    
    def delaunay_triangulation(self, grow=..., n_prc=...): # -> Delaunay:
        ...
    
    @staticmethod
    def find_neighbors_delaunay(pindex, triang):
        """
        Returns the indices of """
        ...
    
    def sample_delaunay_topo(self, ind): # -> bool_:
        ...
    
    def delaunay_minimizers(self): # -> Any | list[Unknown]:
        """
        Returns the indices of """
        ...
    


class LMap:
    def __init__(self, v) -> None:
        ...
    


class LMapCache:
    def __init__(self) -> None:
        ...
    
    def __getitem__(self, v):
        ...
    
    def add_res(self, v, lres, bounds=...): # -> None:
        ...
    
    def sort_cache_result(self): # -> dict[Unknown, Unknown]:
        """
        Sort results and build """
        ...
    


