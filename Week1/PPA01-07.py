number = input("Enter a 5 digit number: ")
i=0
total = 0
while(i<5):
    total = total + int(number[i])
    i+=1
print(total)
total2 = 0
value = int(number)
while(value>0):
    total2 = total2 + value%10
    value = value//10
print(total2)