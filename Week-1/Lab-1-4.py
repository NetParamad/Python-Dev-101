grade = float(input("Enter your grade: "))
def calculateGrade(grade):
    if grade >= 80:
        return "A"
    elif grade >= 70:
         return "B"
    elif grade >= 60:
        return "C"
    elif grade >= 50:
        return "D"
    else:
        return "F"
print("Your grade is:", calculateGrade(grade))