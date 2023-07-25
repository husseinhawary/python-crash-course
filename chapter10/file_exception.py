file_name = "alice.txt"
try:
    with open(file_name, encoding="utf-8") as file_object:
        file_object.read()
except FileNotFoundError:
    print(f"{file_name} File doesn't exist")