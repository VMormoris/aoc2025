from dataclasses import dataclass
import sympy.core.numbers
from sympy import sympify, solve, symbols, Eq
from sympy.solvers.inequalities import reduce_inequalities

@dataclass
class Input:
    desired_joltages: list[int]
    buttons: list[list[int]]

def parse_input() -> list[Input]: 
    with open('input.txt', 'r') as file:
        lines: list[str] = file.readlines()
    
    inputs: list[Input] = []
    for line in lines:
        if line[-1] == '\n':
            line = line[:-1]
        sections: list[str] = line.split(' ')
        joltages: list[str] = sections[-1][1:-1].split(',')
        joltages: list[int] = [int(joltage) for joltage in joltages]

        buttons: list[list[int]] = []
        for section in sections[1:-1]:
            string: str = section[1:-1] # Remove parenthesis
            nums = [int(num) for num in string.split(',')]
            buttons.append(nums)
        inputs.append(Input(joltages, buttons))

    return inputs

def find_all_solutions(input: Input) -> list[int]:
    constant: str = 'a'
    symbols_str: str = ''
    for _ in input.buttons:
        symbols_str += constant + ' '
        constant = chr(ord(constant) + 1)

    max_joltage = max(input.desired_joltages) + 1
    a, b, c, d, e, f, g, h, i, j, k, l, m, n = vars = symbols('a b c d e f g h i j k l m n', integer=True)
    locals = { 'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h, 'i': i, 'j': j, 'k': k, 'l': l, 'm': m, 'n': n }
    set_of_equations: list[Eq] = []
    for idx in range(0, len(input.desired_joltages)):
        constant: str = 'a'
        equation: str = ''
        for button in input.buttons:
            if idx in button:
                equation += constant + ' + '
            constant = chr(ord(constant) + 1)
        set_of_equations.append(Eq(sympify(equation[:-3], locals = locals), input.desired_joltages[idx]))

    sol_dict = solve(set_of_equations, vars)
    
    if all([isinstance(expr, sympy.core.numbers.Zero) or isinstance(expr, sympy.core.numbers.Integer) for expr in sol_dict.values()]):
        # Only one valid combination of buttons
        solution = [int(expr) for expr in sol_dict.values()]
        return [solution]
    
    all_vars = set(vars)
    vars_to_solve = set(sol_dict.keys())
    free_vars = list(set([symbol for expr in sol_dict.values() for symbol in expr.free_symbols]))

    constraints = [expr >= 0 for expr in sol_dict.values()] + [var >= 0 for var in free_vars]
    
    # print(set_of_equations)
    # print(sol_dict)
    # print('\t', all_vars)
    # print('\t', vars_to_solve)
    # print('\t', free_vars)
    # print('\t', constraints)
    # print()

    combinations = []
    active_constraints = [c for c in constraints if c is not sympy.true]
    lambdas = [sympy.lambdify(free_vars, c.lhs - c.rhs if hasattr(c, 'lhs') else c) for c in active_constraints]
    if len(free_vars) == 1:
        for val in range(max_joltage):
            point = (val,)
            if all(f(*point) >= 0 for f in lambdas):
                combinations.append(point)
    elif len(free_vars) == 2:
        for first in range(max_joltage):
            for second in range(max_joltage):
                point = (first, second)
                if all(f(*point) >= 0 for f in lambdas):
                    combinations.append(point)
    elif len(free_vars) == 3:
        for first in range(max_joltage):
            for second in range(max_joltage):
                for third in range(max_joltage):
                    point = (first, second, third)
                    if all(f(*point) >= 0 for f in lambdas):
                        combinations.append(point)
    
    solutions = []
    for combination in combinations:
        presses: dict = {}
        for symbol in locals.values():
            if symbol in sol_dict:
                if isinstance(sol_dict[symbol], sympy.core.numbers.Zero) or isinstance(sol_dict[symbol], sympy.core.numbers.Integer):
                    presses[symbol] = int(sol_dict[symbol])
                else:
                    func = sympy.lambdify(free_vars, sol_dict[symbol])
                    presses[symbol] = func(*combination)
            elif symbol in free_vars:
                presses[symbol] = combination[free_vars.index(symbol)]
        solutions.append([press for press in presses.values()])
    
    return solutions

def is_integer(s: float) -> bool:
    num = "{:.10f}".format(s)
    for i in range(0, len(num)):
        if num[i] == '.':
            if any([ch != '0' for ch in num[i+1:]]):
                return False
    return True

def find_min_solution(input: Input) -> int:
    solutions = find_all_solutions(input)
    solutions = [sol for sol in solutions if sum(sol).is_integer()]
    best_sol: list[int] = min(solutions, key = lambda sol: sum(sol))
    print(best_sol, '=>', sum(best_sol))
    return sum(best_sol)
    

inputs: list[Input] = parse_input()
# for input in inputs:
s = 0
for i in range(0, len(inputs)):
    s += find_min_solution(inputs[i])
print(s)

# 16145 Too low
# 16145 + 524 = 16669 Too high
# 16663 Correct
#print(sum([solve(input) for input in inputs]))