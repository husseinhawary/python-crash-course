user_name = input("Enter your name please:- ")
file_name = "guest.txt"

with open(file_name, "a") as file_object:
    file_object.write(user_name + "\n")
