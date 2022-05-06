from sympy import Matrix
from utils.get_basis import get_basis
from utils.get_point_from_plane import get_point_from_plane

isParallel = False
isIntersect = False

n = int(input())
equations = [list(map(int, input().split())) for i in range(n)]

point_L2 = list(map(int, input().split()))
n = int(input())
basis_L2 = [list(map(int, input().split())) for x in range(n)]

point_L1 = get_point_from_plane([x[:-1] for x in equations], [x[-1] for x in equations])
basis_L1 = list(get_basis(Matrix([x[:-1] for x in equations])).values())

all_basis = Matrix(basis_L1 + basis_L2)

if all_basis.rank() == max(len(basis_L1), len(basis_L2)):
    isParallel = True

vector: Matrix = Matrix(point_L2) - Matrix(point_L1)

basis_with_vector = all_basis.row_insert(0, vector.T)
if basis_with_vector.rank() == all_basis.rank():
    isIntersect = True

print(isParallel, isIntersect)
