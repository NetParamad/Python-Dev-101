number = int(input("Enter a number: "))
listsum = []
sum = 0
if(number > 0):
    for i in range(1, number + 1):
        listsum.append(i)
        sum += i
        if(sum >= number):
            break
    print("List sum is: ", listsum)
    print("Sum is: ", sum)
else:
    print("Invalid number")
