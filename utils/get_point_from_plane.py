from typing import List, Tuple
from sympy import Matrix, linsolve


def get_point_from_plane(coeffs: List[List[int]], free_coeffs: List[int]) -> Tuple[int]:
    point = linsolve((Matrix(coeffs), Matrix(free_coeffs)))
    for var in list(point.free_symbols):
        point = point.replace(var, 0)
    return point.args[0]
