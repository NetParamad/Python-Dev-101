# 2.	คำนวณเกรดเฉลี่ย โดยรับ จำนวนวิชา  ชื่อวิชา หน่วยกิต และเกรด แต่ละวิชา ให้คำนวณและแสดงเกรดเฉลี่ย

subjects = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    name = input("Enter subject name: ")
    credit = int(input("Enter credit: "))
    grade = float(input("Enter grade: "))
    subjects.append((name, credit, grade))

total_credit = sum(subject[1] for subject in subjects)
total_grade = sum(subject[2] * subject[1] for subject in subjects)
average_grade = total_grade / total_credit
print(f"Average grade = {average_grade:.2f}")
print(subjects)
print(total_credit)
print(total_grade)

