# ask user input the length of the 3 sides of a traiangle 
x = float(input ("enter the first side\n"))
y = float(input("enter the second side\n"))
z = float(input("enter the third side\n"))
# if all sides are equal print equilateral 
if x == y == z:
    print("equilateral")
# if 2 sides are equal print isosceles 
elif x == y or x == z or z == y:
    print("isosceles")
# if no sides are equal print scalene
else:
    print("scelene")
