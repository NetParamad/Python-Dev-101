first = int(input("First: "))
second = int(input("Second: "))
third = int(input("Third: "))
if(first <= second and first <= third):
    min_value = first
elif(second <= first and second <= third):
    min_value = second
else:
    min_value = third
if(first >= second and first >= third):
    max_value = first
elif(second >= first and second >= third):
    max_value = second
else:
    max_value = third

print("Min: ", min_value)
print("Max: ", max_value)

