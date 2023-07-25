import json


# numbers = [2, 3, 5, 7, 11, 13]
# file_name = "numbers.json"
# with open(file_name, "w") as file_object:
#     json.dump(numbers, file_object)

# user_name = input("What is your name? ")
# file_name = "username.json"
#
# with open(file_name, "w") as file_object:
#     json.dump(user_name, file_object)
#     print(f"We will remember when you come back, {user_name}!")

# file_name = "username.json"
# try:
#     with open(file_name) as file_object:
#         user_name = json.load(file_object)
# except FileNotFoundError:
#     user_name = input("What is your name? ")
#     with open(file_name, "w") as file_object:
#         json.dump(user_name, file_object)
#         print(f"We will remember when you come back, {user_name}!")
# else:
#     print(f"Welcome back {user_name}")


def get_stored_user_name():
    file_name = "username.json"
    try:
        with open(file_name) as file_object:
            user_name = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return user_name


def add_new_user():
    user_name = input("What is your name? ")
    file_name = "username.json"
    with open(file_name, "w") as file_object:
        json.dump(user_name, file_object)
    return user_name


def greet_user():
    user_name = get_stored_user_name()
    if user_name:
        answer = input(f"Hello, is this the correct {user_name} (y/n)? ")
        if answer.lower() == "y":
            print(f"Welcome back {user_name}")
        else:
            user_name = add_new_user()
            print(f"We will remember when you come back, {user_name}!")
    else:
        user_name = add_new_user()
        print(f"We will remember when you come back, {user_name}!")


greet_user()
