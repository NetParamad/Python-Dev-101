# ลองฝึกข้อสอบหน่อย flowchart และ โปรแกรม ที่จะแสดงผลสูตรคูณแม่ x - y. แต่หาก y น้อยกว่า x พิมพ์แม่ y ถึง x

def mutilple(x):
    i = 1
    while (i <= 12):
        print(x, "x", i, "=", x * i)
        i += 1

# mutilple(10)

def ex(x,y):
    i = x
    while (i <= y):
        mutilple(i)
        i += 1

x = int(input("Enter x number: "))
y = int(input("Enter y number: "))

# if(x < y):
#    ex(x,y)
# else:
#     ex(y,x)


if (y < x):
    x,y = y,x
ex(x,y)




# def mutilpleToNum(x, y):
#     if (x < y):
#         while x <= y:
#             mutilple(x)
#             x += 1
#     else:
#         while y <= x:
#             mutilple(y)
#             y += 1

    

# mutilpleToNum(x, y)

# if(x < y):
#     while x <= y:
#         i = 1
#         while (i <= 12):
#             print(f"{x} x {i} = {x * i}")
#             i += 1
#         x += 1
# elif(x > y):
#     while y <= x:
#         i = 1
#         while (i <= 12):
#             print(f"{y} x {i} = {y * i}")
#             i += 1
#         y += 1
# else:
#     while x == y:
#         i = 1
#         while (i <= 12):
#             print(f"{x} x {i} = {x * i}")
#             i += 1
#         x += 1
