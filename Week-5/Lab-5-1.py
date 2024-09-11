# 1.	รับคะแนนสอบ(เต็ม 100 คะแนน) ของนักศึกษา n คน ให้แสดงคะแนนเฉลี่ย, คะแนนสูงสุด และคะแนนต่ำสุด  และแสดงจำนวน นศ. และรายชื่อ นศ.  ที่ได้คะแนนมากกว่าคะแนนเฉลี่ย

score = []
name = []
n = int(input("Enter number of students: "))
i = 1
while i <= n:
    name.append(input(f"Enter name ({i}) : "))
    score.append(int(input("Enter score ({i}) : ")))
    i += 1
average = sum(score)/n
print("Average score = ", average)
print("Max score = ", max(score))
print("Min score = ", min(score))
for i in range(n):
    if score[i] >= average:
        print(f"student : name =  {name[i]} , score = {score[i]}")

