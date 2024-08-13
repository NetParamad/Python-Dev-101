# 1.	แสดงรายการและผลรวมของเลขจำนวนนับตั้งแต่ 1 ถึง 

n = int(input("Enter a number: "))
i = 1
sum = 0
while i <= n:
    sum += i
    print(i)
    i += 1
print("Sum =", sum)