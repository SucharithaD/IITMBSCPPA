x1 = float(input('Enter x1:'))
y1 = float(input('Enter y1:'))
x2 = float(input('Enter x2:'))
y2 = float(input('Enter y2:'))
x3 = float(input('Enter x3:'))
m = None
if x1!=x2:
    m = (y2 - y1)/ (x2 - x1)
    y3 = m *( x3 - x1) + y1
    print(y3)
    
    if m == 0:
        print("Horizontal Line")
    elif m>0:
        print("Positive Slope")
    elif m < 0 : 
        print("Negative Slope")
else:
    print('Vertical Line')
    
