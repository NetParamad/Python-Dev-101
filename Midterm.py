# ข้อ 1 อธิบาย  เกี่ยวกับ การประกาศตัวแปร ชนิดข้อมูล เครื่องหมาย คำสั่ง อินพุท เอาต์พุต และ flowchart     10 คะแนน

name  = "Example"
number = 15.102003

typeInt = type(number) 
typeFloat = type(number) 
typeStr = type(name)


num = input("Enter number : ")
print(f"Integer : {typeInt} String : {typeStr} Float :  {typeFloat}")
print(f"Number : {number} + {num} = {number + num}")


# ข้อ 2 เขียน flowchart และ program ทางเลือก 1 - 3 ทางเลือก (if ,if...else, if...elif...else)    15 คะแนน

if number > 10:
    print("Number is greater than 10")
elif number < 10:
    print("Number is less than 10")
else:
    print("Number is equal to 10")





# ข้อ 3 เรื่อง loop เขียนโปรแกรมรับชุดข้อมูลแล้วคำนวณค่าบางอย่าง เช่น ผลรวม ค่าสูงสุด หรือจำนวนเลขที่ติดลบ เป็นต้น    15 คะแนน

sum = 0
n = int(input("Enter number : "))
for i in range(n):
    num = int(input(f"Enter number position : {i} : "))
    sum += num
print(f"Sum : {sum}")

numList = []
minus = 0
n = int(input("Enter number length : "))
for i in range(n):
    num = int(input(f"Enter number position {i} : "))
    if(num < 0):
        minus += 1
    numList.append(num)
print(f"List : {numList} \nMax : {max(numList)} \nMin : {min(numList)} \nMinus : {minus}")

# ข้อ 4 เรื่อง function อีกเรื่อง 10 คะแนน

def add(x, y):
    return x + y

print(add(10, 20))
print(f"Add : {add(30, 40)}")