listsum = []
sum =0 
i = 1
n = int(input("Enter a number: "))

while(i<=n):
    sum = sum + i
    listsum.append(i)
    i = i + 1
print ("List sum is: ", listsum)
print ("Sum is: ", sum)