import math
import time

print("Welcome to the code")

time.sleep(1)

shapeselector = int(input("Select a shape: \n2D Shapes: \n\t 1. Circle \n\t 2. Rectangle \n\t 3. Square \n3D Shapes: \n\t 4. Cuboid \n\t 5. Cube\n Enter : "))

if shapeselector == 1:
    radi = int(input("Enter radius of the circle: "))
    carea = math.pi * radi * radi
    ccircumference = 2 * math.pi * radi
    print(f"Circle (Radius {radi} Units)\nArea: {carea}\nCircumference: {ccircumference}")

elif shapeselector == 2:
    rlength = int(input("Enter Length of rectangle: "))
    rwidth = int(input("Enter Width of rectangle: "))
    rarea = rlength * rwidth
    rperi = 2 * (rlength + rwidth)
    print(f"Rectangle (Length: {rlength} Units, Width: {rwidth} Units)\nArea: {rarea}\nPerimeter: {rperi}")

elif shapeselector == 3:
    slength = int(input("Enter Length of the Square: "))
    sarea = slength * slength
    speri = 4 * slength
    print(f"Square (Length: {slength} Units)\nArea: {sarea}\nPerimeter: {speri}")

elif shapeselector == 4:
    culength = int(input("Enter length of the cuboid: "))
    cuwidth = int(input("Enter width of the cuboid: "))
    cuheight = int(input("Enter height of the cuboid: "))
    cuvolume = culength * cuwidth * cuheight
    cusarea = 2 * (culength * cuwidth + culength * cuheight + cuwidth * cuheight)
    print(f"Cuboid (Length: {culength} Units, Width: {cuwidth} Units, Height: {cuheight} Units)\nSurface Area: {cusarea}\nVolume: {cuvolume}")

elif shapeselector == 5:
    cubelength = int(input("Enter Length of side of cube: "))
    cubevol = cubelength * cubelength * cubelength
    cubesarea = 6 * cubelength * cubelength
    print(f"Cube (Length: {cubelength} Units)\nSurface Area: {cubesarea}\nVolume: {cubevol}")

else:
    print("Invalid Input")
