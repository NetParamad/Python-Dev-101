# Lab-1
n = int(input("Enter a number: "))
i = 1
while i <= 12:
    print("{:2} x {:^2} = {:>2}".format(n, i, n * i))
    i = i + 1
