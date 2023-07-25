# open() function returns an object represents the file, so will assign this object to file_object
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
print(contents.strip())
