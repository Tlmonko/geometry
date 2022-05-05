from sympy import Matrix

from utils.get_basis import get_basis
from utils.get_linearly_independent_vectors import get_linearly_independent_vectors
from utils.express_linearly_dependent_vector import express_linearly_dependent_vector

n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]

n = int(input())
basis_L2 = [list(map(int, input().split())) for x in range(n)]

basis_L1 = list(get_basis(Matrix(matrix)).values())

print('L1 basis:', basis_L1)
print('L2 basis:', basis_L2)
print()

lid_vectors = get_linearly_independent_vectors(basis_L1 + basis_L2)

print('Basis of sum:', lid_vectors)

ld_vectors = [x for x in basis_L1 + basis_L2 if x not in lid_vectors]

basis_unite = []
for ld_vector in ld_vectors:
    coeffs = express_linearly_dependent_vector(lid_vectors, ld_vector)
    basis_to_summarise = basis_L1 if ld_vector in basis_L2 else basis_L2
    basis = Matrix([0] * len(ld_vector))
    for i, coeff in enumerate(coeffs):
        if lid_vectors[i] in basis_to_summarise:
            basis += coeff * Matrix(lid_vectors[i])
    basis_unite.append(basis)

print(basis_unite)
