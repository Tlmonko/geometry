import sympy

matrix = sympy.Matrix([[-3, -2, 2, 1, -1], [5, 4, -2, -3, 1], [-7, -5, 4, 3, -2]]).rref()[0]
shape = sympy.shape(matrix)

vars = [sympy.Symbol(f'x{i}') for i in range(1, shape[1] + 1)]
solved_system = sympy.linsolve((matrix, sympy.Matrix([0, 0, 0])), *vars)

basis = {
    x: [sympy.Poly(i, *vars).coeff_monomial(x) for i in solved_system.args[0]] for x in solved_system.free_symbols
}

print(basis)