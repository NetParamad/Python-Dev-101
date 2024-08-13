# รับวิชา หน่วยกิต และเกรด 3 วิชา ให้แสดง ผลการเรียน และระดับคะแนนเฉลี่ยสะสม (GPA)

subject1 = input("Enter subject 1: ")
subject2 = input("Enter subject 2: ")
subject3 = input("Enter subject 3: ")
credit1 = int(input("Enter credit 1: "))
credit2 = int(input("Enter credit 2: "))
credit3 = int(input("Enter credit 3: "))
grade1 = int(input("Enter grade 1: "))
grade2 = int(input("Enter grade 2: "))
grade3 = int(input("Enter grade 3: "))

GPA = (grade1 * credit1 + grade2 * credit2 + grade3 * credit3) / (credit1 + credit2 + credit3)
print(f"GPA is: {GPA}",)