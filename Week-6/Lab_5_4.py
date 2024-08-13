# 4.	regis(subjectsList) # แสดงรายละเอียดรายวิชาที่ลงทะเบียนเรียน และระดับคะแนนเฉลี่ย
# โดย subjectList คือ ลิสต์ของรายการวิชาที่ลงทะเบียน เช่น
# [[1,’Cal’,3,4.0],
# [2,’Eng’,2,2.0],
# [1,’AI’,3,3.0]]

def regis(dataSubjects):
    sumCredit = 0
    sumGrade = 0
    for i in dataSubjects:
        sumCredit += i[1]
        sumGrade += i[1] * i[2]
    print(f"Credit: {i[1]} Grade: {[i[2]]}")   
    return print(f"Average grade = {sumGrade/sumCredit:.2f}")


numSubjects = input("Enter number of subjects: ")
dataSubjects = []
for i in range(int(numSubjects)):
    print("Subject ", i+1)
    nameSubject = input("Enter subject name: ")
    creditSubject = float(input("Enter credit: "))
    gradeSubject = float(input("Enter grade: "))
    dataSubjects.append([nameSubject, creditSubject, gradeSubject])
print(regis(dataSubjects))
