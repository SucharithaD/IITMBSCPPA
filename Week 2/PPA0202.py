x = float(input("Enter a value:"))
def getXValue(x):
    if 0 < x < 10:
        return x + 2
    elif x >= 10:
        return x**2 + 2
    else:
        return 0.0
print(getXValue(x))


