# 2.	รับคะแนนสอบ(เต็ม 100 คะแนน) ของนักศึกษา n คน ให้แสดงคะแนนเฉลี่ย, คะแนนสูงสุด และคะแนนต่ำสุด

n = int(input("Enter number of students: "))
sum = 0
max = 0
min = 0
i = 1
while i <= n:
    score = int(input("Enter score: "))
    if(score >= 0 and score <= 100):
        sum += score
        if score > max:
            max = score
        if score < min:
            min = score
        i += 1
    else:
        print("Invalid score (0 - 100)")
print("Average score = ", sum / n)
print("Max score = ", max)
print("Min score = ", min)