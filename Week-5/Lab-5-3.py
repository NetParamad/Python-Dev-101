# 3.	โจทย์/ปัญหาที่ นศ. วิเคราะห์ ออกแบบ เขียน โปรแกรมแก้ปัญหาได้อย่างเข้าใจ

# โจทย์เก็บค่าใน list ที่รับจากผู้ใช้งานและคำนวนค่า bmi แล้วเพิ่มค่า bmi

dataUser = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    height = float(input("Enter height: "))
    weight = float(input("Enter weight: "))
    bmi = weight / (height * height)
    dataUser.append((name, height, weight, bmi))
    print(dataUser)
    

