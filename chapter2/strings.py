name = "hussein elhawary"
# title() method convert the initial character for every word into uppercase
print(name.title())
print(name.lower())
print(name.upper())

first_name = "Hussein"
last_name = "Elhawary"
# f-strings introduced in python 3.6 and if u use 3.5 or earlier version you can use .format() method
print(f"Hello {first_name} {last_name}, Nice to meet you.")
print("Hello {} {}, Nice to meet you.".format(first_name, last_name))

# rstrip() remove the spaces from the string right side
favorite_language = "Python   "
print(favorite_language.rstrip())

# lstrip() remove the spaces from the string left side
other_language = "   Typescript"
print(other_language.lstrip())

# strip() remove the spaces from the string left & right sides
full_name = "   Anas Hussein   "
print(full_name.strip())

quote_person = "Albert Einstein"
quote_message = "A person who never made a mistake never tried anything new"
print(f"{quote_person} once said, \"{quote_message}\"")

MAX_NUMBER = 100
print(MAX_NUMBER)