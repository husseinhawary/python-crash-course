# first_number = input("Enter first number: ")
# second_number = input("Enter second number: ")
#
# try:
#     result = int(first_number) + int(second_number)
#     print(f"The result is {result}")
# except ValueError:
#     print("Wrong value provided, Enter two numbers.")

print("Enter two numbers to add them.")
print("Enter 'q' to quit.")

while True:
    number1 = input("Enter first number: ")
    if number1 == 'q':
        break
    number2 = input("Enter second number: ")
    if number2 == 'q':
        break
    try:
        result = int(number1) + int(number2)
        print(f"The result is {result}")
    except ValueError:
        print("Wrong value provided, Enter two numbers.")