def scaleMappingArea(coords, fromWidth, fromHeight, toWidth, toHeight):
    coordsArr = list(map(int, coords.split(",")))
    scaledCoords = []
    
    for index, coord in enumerate(coordsArr):
        #Even coords are x component
        if (index % 2 == 0):
            scaledCoords.append(int(coord * toWidth / fromWidth))
        #Odd coords are y component
        else:
            scaledCoords.append(int(coord * toHeight / fromHeight))
    
    return ",".join(map(str,scaledCoords))
dim1 = input("Original dimension: ")
x1, y1 = list(map(int, dim1.split("x")))
ratio = 1.0 * x1 / y1
dim2 = input("Target dimension: ")
x2, y2 = dim2.split("x")
if x2 == "" and y2 != "":
    y2 = int(y2)
    x2 = int(ratio * y2)
elif x2 != "" and y2 == "":
    x2 = int(x2)
    y2 = int(1.0 / ratio * x2)
else:
    x2 = int(x2)
    y2 = int(y2)
coordsInput = input("Coordinates: ")
print("-> ", scaleMappingArea(coordsInput, x1, y1, x2, y2))
