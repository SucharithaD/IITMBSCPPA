x = float(input("Enter x-coordinate:"))
y = float(input("Enter y-coordinate:"))
if x == 0.0 and y == 0.0:
    quadrant = "origin"
elif x == 0.0:
    quadrant = "y-axis"
elif y == 0.0:
    quadrant = "x-axis"
elif x>0 and y>0:
    quadrant = "first"
elif x < 0 and y> 0:
    quadrant = "second"
elif x < 0 and y < 0:
    quadrant = "third"
elif x > 0 and y < 0:
    quadrant = "fourth"
    
print(quadrant)