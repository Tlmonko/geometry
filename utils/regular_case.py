from sympy.parsing.sympy_parser import parse_expr
from sympy import Poly, Add, Mul, Integer
from sympy import solve_rational_inequalities
from typing import List


def get_nodes(inequalities: List[str]) -> List[List[int]]:
    pass


def solve_linear_inequalities(inequalities: List[str]):
    parsed_inequalities = [parse_expr(x) for x in inequalities]
    res = solve_rational_inequalities([
        (
            Poly(
                Add(x.lhs, Mul(x.rhs, Integer(-1)))
            )
        ) for x in parsed_inequalities
    ])
    print(res)


if __name__ == '__main__':
    inequalities = ['x1 - x2 = 1', 'x1 + x2 = 1', 'x2 >= 0']
    print(solve_linear_inequalities(inequalities))
