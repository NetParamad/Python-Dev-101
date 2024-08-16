# 1. factorial(n)  #คำนวนและคืนค่า n!1
n = int(input("Enter a number: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(n))

def factorialV2(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(factorialV2(n))

def factorialV3(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact
print(factorialV3(n))


