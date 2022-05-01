from sympy import Matrix

from utils.get_basis import get_basis

n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]

basis = get_basis(Matrix(matrix))

conjugate = Matrix([basis[x] for x in basis.keys()])

print('Уравнение сопряженного пространства')
print(conjugate)

print('Базис сопряженного')
print(get_basis(conjugate))
