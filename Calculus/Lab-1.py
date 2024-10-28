import sympy as sp

x = sp.Symbol('x')
y = sp.Symbol('y')
z = sp.Symbol('z')

fx = 2*x**3-5**2-7*x+4
sp.diff(fx, x)