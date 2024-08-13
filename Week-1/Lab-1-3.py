height = float(input('Enter your height: '))
radius = float(input('Enter your radius: '))
volume = 22/7 * radius**2 * height
surfaceArea = 2 * 22/7 * radius * (radius + height)
print("Area is: %.2f"%(volume))
print("Surface area is: %.2f"%(surfaceArea))