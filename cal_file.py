import sympy as sp

def compute_derivative(input_string):
    # Split the input string to get the equation and degree of derivative
    equation_str, degree_str = input_string.split('/')
    degree = int(degree_str)

    # Parse the equation string using sympy
    x = sp.Symbol('x')
    equation_expr = sp.sympify(equation_str)

    # Compute the derivative
    derivative_expr = sp.diff(equation_expr, x, degree)

    # Convert the derivative expression to a string
    derivative_str = str(derivative_expr)

    return derivative_str

# Example usage:
input_string = "x*3 + 2*x*2 - 5*x + 7/2"  # Equation


