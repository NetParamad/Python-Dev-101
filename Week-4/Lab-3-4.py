# 4.	แสดงรายการและผลรวมของจำนวนเฉพาะทั้งหมดที่มีค่าน้อยกว่าหรือเท่ากับ n 

n = int(input("Enter a number: "))
i = 1
sum = 0
while i <= n:
    if i % 2 == 1:
        print(i)
        sum += i
    i += 1
print("Sum =", sum)