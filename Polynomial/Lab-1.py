# Import ไลบรารี
from sympy import symbols, Eq, solve

# กำหนดตัวแปร x
x = symbols('x')

# สร้างพหุนาม: P(x) = x^2 - 3x + 2
polynomial = x**2 - 3*x + 2

# สร้างสมการ
equation = Eq(polynomial, 0)

# แก้สมการ
roots = solve(equation, x)
print(roots)

# สร้างพหุนาม: P(x) = x^3 - 6x^2 + 11x - 6
polynomial = x**3 - 6*x**2 + 11*x - 6

# สร้างสมการ
equation = Eq(polynomial, 0)

# แก้สมการ
roots = solve(equation, x)
print(roots)

from sympy import limit, oo

# สร้างพหุนาม
polynomial = x**2 + 3*x + 2

# หาลิมิตเมื่อ x เข้าใกล้ oo (อนันต์)
limit_at_infinity = limit(polynomial, x, oo)
print(limit_at_infinity)