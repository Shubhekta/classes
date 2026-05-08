# 3.Wap to take a number from user input and print reversed formated table.
# format : 
# 3x10=30
# 3x2=6
# 3x1=3
user_input = int(input("Enter your number:"))
s = 0
for i in range(10,2,-1):
    s = user_input*i
    print(f"{user_input} * {i} = {s}")