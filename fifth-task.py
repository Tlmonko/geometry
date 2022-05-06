from sympy import Matrix

from utils.get_basis import get_basis
from utils.get_point_from_plane import get_point_from_plane

n = int(input())
equations = [list(map(int, input().split())) for i in range(n)]

point_L2 = list(map(int, input().split()))
n = int(input())
basis_L2 = [list(map(int, input().split())) for x in range(n)]

point_L1 = get_point_from_plane([x[:-1] for x in equations], [x[-1] for x in equations])
basis_L1 = list(get_basis(Matrix([x[:-1] for x in equations])).values())

full_matrix = Matrix(basis_L1 + basis_L2)
vector = Matrix(point_L2) - Matrix(point_L1)
full_matrix.row_insert(0, vector.T)

if full_matrix.rank() == len(basis_L1) + len(basis_L2):
    print('Все пространство')
    exit()

basis = list(get_basis(full_matrix).values())

for vector in basis:
    free_coeff = sum([x * point_L1[i] for i, x in enumerate(vector)])
    print(*vector, free_coeff)