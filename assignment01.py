#Basic calculator program
user_input1 = int(input("Enter your first number: "))
user_input2 = int(input("Enter your second number: "))
user_input3 = input("Enter a mathematical operator(-, *, +): ")

if user_input3 == "-":
    result = user_input1 - user_input2
if user_input3 == "*":
    result = user_input1 * user_input2
if user_input3 == "+":
    result = user_input1 + user_input2

print(f"The result of {user_input1} {user_input3} {user_input2} is {result}  ")


