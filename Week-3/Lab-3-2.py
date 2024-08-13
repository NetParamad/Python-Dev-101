# รับตัวเลข 3 จำนวน แสดงจำนวนที่มากที่สุด จำนวนที่น้อยที่สุด และค่าเฉลี่ย

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
average = (num1 + num2 + num3) / 3

if(num1 >= num2 and num1 >= num3):
    print("The largest number is: ", num1)
elif(num2 >= num1 and num2 >= num3):
    print("The largest number is: ", num2)
else:
    print("The largest number is: ", num3)
print("The average is: ", average)