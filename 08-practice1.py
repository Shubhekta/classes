#wap to takes start_point and end_point from user input and print all number division by 2 and 3.

start_num = int(input("Enter your first number: "))
end_num = int(input("Enter your last number: "))

for i in range(start_num, end_num):
    if i%2 == 0 or i%3 == 0:
       print(f"divisible by 2 and 3: - {i}")

