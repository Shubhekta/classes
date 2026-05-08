#wap to take a number from user input and print formated table.
#format:
#3x1=3
#3x2=6
# . . . .
#3x10=30
ekta= int(input("Enter your number:"))
s = 0
for i in range (1,11):
    s = ekta * i
    print(f"{ekta} x {i} = {s}")