def mutilple(m):
    i = 1
    while i <= 12:
        print(m, "x", i, "=", m * i)
        i += 1

def mutilpleToNum(m, n):
    while m <= n:
        mutilple(m)
        m += 1

def max(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2
def min(n1,n2):
    if n1 < n2:
        return n1
    else:
        return n2

mutilpleToNum(1, 2)
x = max(10, 20)
y = min(10, 20)
print(x, y)



