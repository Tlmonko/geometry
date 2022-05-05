from typing import List, Tuple
from sympy import Matrix, linsolve


def express_linearly_dependent_vector(independent_vectors: List[List[int]], dependent_vector: List[int]) -> Tuple[int]:
    ans = linsolve((Matrix(independent_vectors).T, Matrix(dependent_vector)))
    return ans.args[0]


if __name__ == '__main__':
    independent_vectors = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 2, 0]]
    dependent_vector = [2, 1, 2, 1]
    basis_L1 = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]]
    ans = express_linearly_dependent_vector(independent_vectors, dependent_vector)
    result = Matrix([0] * len(independent_vectors[0]))
    for i, coeff in enumerate(ans):
        if independent_vectors[i] in basis_L1:
            result += coeff * Matrix(independent_vectors[i])

    print(result)
