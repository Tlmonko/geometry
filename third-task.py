from sympy import Matrix

from utils.get_basis import get_basis

point = list(map(int, input().split()))

n = int(input())
basis = [list(map(int, input().split())) for x in range(n)]

equations = get_basis(Matrix(basis))

for equation in equations.values():
    coeff = sum([-point[i] * equation[i] for i in range(len(point))])
    print(equation)
    print(coeff)
    print()
