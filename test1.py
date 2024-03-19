
length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))

area = (length * width) #calculating area of rectangle

if area <= 0:
    print("Invalid inputs")
    
else:
    print("Area of the rectangle is " + str(area))
