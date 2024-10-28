import sympy as sy
x = sy.Symbol('x')
f = 2*x**2 + 3*x + 1
g = x + 1
h = f/g
h.simplify()
print(h)
