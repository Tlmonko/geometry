from sympy import Matrix
from itertools import combinations
from typing import List


def get_linearly_independent_vectors(matrix: List[List[int]]) -> List[List[int]]:
    rank = Matrix(matrix).rank()
    all_rank_size_matrices = combinations(matrix, rank)
    for lid_matrix in all_rank_size_matrices:
        if Matrix(lid_matrix).rank() == rank:
            return lid_matrix


if __name__ == '__main__':
    basis_L1 = [[0, -1, 0, 1, 0], [0, 1, 1, 0, 0], [1, 0, 0, 0, 1]]
    basis_L2 = [[-1, 4, 2, -1, -1], [4, 1, 2, 2, 4], [-6, 2, -1, -4, -6]]
    print(get_linearly_independent_vectors(basis_L1 + basis_L2))
