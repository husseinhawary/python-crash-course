# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# height = input("How tall are you, in inches? ")
# height = int(height)
#
# if height >= 48:
#     print("You're tall enough to ride!")
# else:
#     print("You'll be able to ride when you are a little order.")

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
#
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

# while loops

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "\nHow old are you?"
# prompt += "\nType 'quit' to stop.)"
#
# active = True
# while active:
#     age = input(prompt)
#     if age == "quit":
#         active = False
#     else:
#         age = int(age)
#         if age < 3:
#             price = 0
#         elif age < 13:
#             price = 10
#         else:
#             price = 15
#         print(f"The ticket price is {price}.")

unconfirmed_users = ["hussein", "anas", "shiamaa"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print(confirmed_users)

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

print("\n----- Poll Result -----")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")