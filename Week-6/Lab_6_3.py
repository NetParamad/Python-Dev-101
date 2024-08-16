# 3.	posNegZero(numberList) # คืนค่าจำนวนสมาชิกของ numberList ที่เป็นจำนวนเต็มบวก, 
#  	จำนวนสมาชิกของ numberList ที่เป็นจำนวนเต็มลบ, 
#  	จำนวนสมาชิกของ numberList ที่เป็นศูนย์

def posNegZero(numberList):
    positive = 0
    negative = 0
    zero = 0
    for i in numberList:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    return 'positive',positive,' negative',negative,' zero', zero

numberList = []
n = int(input("Enter number of element: "))
for i in range(n):
    numberList.append(int(input("Enter number: ")))
print(posNegZero(numberList))
