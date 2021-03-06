"""
This type stub file was generated by pyright.
"""

from .ckdtree import cKDTree

__all__ = ['minkowski_distance_p', 'minkowski_distance', 'distance_matrix', 'Rectangle', 'KDTree']
def minkowski_distance_p(x, y, p=...): # -> Any:
    """Compute the pth power of the L**"""
    ...

def minkowski_distance(x, y, p=...): # -> Any:
    """Compute the L**p distance betwee"""
    ...

class Rectangle:
    """Hyperrectangle class.

    Repre"""
    def __init__(self, maxes, mins) -> None:
        """Construct a hyperrectangle."""
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def volume(self): # -> Any:
        """Total volume."""
        ...
    
    def split(self, d, split): # -> tuple[Rectangle, Rectangle]:
        """Produce two hyperrectangles by s"""
        ...
    
    def min_distance_point(self, x, p=...): # -> Any:
        """
        Return the minimum dist"""
        ...
    
    def max_distance_point(self, x, p=...): # -> Any:
        """
        Return the maximum dist"""
        ...
    
    def min_distance_rectangle(self, other, p=...): # -> Any:
        """
        Compute the minimum dis"""
        ...
    
    def max_distance_rectangle(self, other, p=...): # -> Any:
        """
        Compute the maximum dis"""
        ...
    


class KDTree(cKDTree):
    """kd-tree for quick nearest-neighb"""
    class node:
        def __init__(self, ckdtree_node=...) -> None:
            ...
        
        def __lt__(self, other) -> bool:
            ...
        
        def __gt__(self, other) -> bool:
            ...
        
        def __le__(self, other) -> bool:
            ...
        
        def __ge__(self, other) -> bool:
            ...
        
        def __eq__(self, other) -> bool:
            ...
        
    
    
    class leafnode(node):
        @property
        def idx(self): # -> ndarray[Unknown, Unknown]:
            ...
        
        @property
        def children(self):
            ...
        
    
    
    class innernode(node):
        def __init__(self, ckdtreenode) -> None:
            ...
        
        @property
        def split_dim(self):
            ...
        
        @property
        def split(self):
            ...
        
        @property
        def children(self):
            ...
        
    
    
    @property
    def tree(self): # -> node | leafnode | innernode:
        ...
    
    def __init__(self, data, leafsize=..., compact_nodes=..., copy_data=..., balanced_tree=..., boxsize=...) -> None:
        ...
    
    def query(self, x, k=..., eps=..., p=..., distance_upper_bound=..., workers=...): # -> tuple[list[Any], list[Unknown]] | tuple[Unknown, Unknown] | tuple[Unknown, intp | Unknown]:
        r"""Query the kd-tree for nearest ne"""
        ...
    
    def query_ball_point(self, x, r, p=..., eps=..., workers=..., return_sorted=..., return_length=...):
        """Find all points within distance """
        ...
    
    def query_ball_tree(self, other, r, p=..., eps=...):
        """
        Find all pairs of point"""
        ...
    
    def query_pairs(self, r, p=..., eps=..., output_type=...):
        """Find all pairs of points in `sel"""
        ...
    
    def count_neighbors(self, other, r, p=..., weights=..., cumulative=...):
        """Count how many nearby pairs can """
        ...
    
    def sparse_distance_matrix(self, other, max_distance, p=..., output_type=...):
        """Compute a sparse distance matrix"""
        ...
    


def distance_matrix(x, y, p=..., threshold=...): # -> Any | ndarray[Unknown, Unknown]:
    """Compute the distance matrix.

  """
    ...

