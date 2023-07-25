from pizza import make_pizza
# def describe_pet(animal_type, pet_name):
#     """
#     display information about a pet
#     :param animal_type:
#     :param pet_name:
#     :return:
#     """
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# # there is a positional argument and this leads to unrealistic output when you pass unordered arguments
# describe_pet("hamster", "harry")
#
# # Overcoming into positional argument by using keyword arguments by passing name-value pairs
# describe_pet(pet_name="harry", animal_type="hamster")
# describe_pet(animal_type="hamster", pet_name="harry")

# default value, the default value parameter should be the last one in the function definition
# def describe_pet(pet_name, animal_type="dog"):
#     """
#     display information about a pet
#     :param pet_name:
#     :param animal_type:
#     :return:
#     """
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet("willie")
# describe_pet("hamster", "harry")

# part 1 exercises

# def make_shirt(size, message):
#     """
#     print size and message of the shirt.
#     :param size:
#     :param message:
#     :return:
#     """
#     print(f"The shirt has size {size} and show the message {message}.")
#
#
# make_shirt(5, "Hello, there!")
# make_shirt(size=10, message="Hello, there!")


# return value
# def get_formatted_name(first_name, last_name):
#     """
#     return full name neatly formatted
#     :param first_name:
#     :param last_name:
#     :return: full name
#     """
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name("hussein", "elhawary")
# print(musician)

# pass the middle_name optionally
# def get_formatted_name(first_name, last_name, middle_name=""):
#     """
#     return full name neatly formatted
#     :param first_name:
#     :param middle_name:
#     :param last_name:
#     :return: full name
#     """
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name("hussein", "elhawary", "abdel-moamen")
# musician_2 = get_formatted_name("anas", "elhawary")
# print(musician)
# print(musician_2)


# return a dictionary
# def build_person(first_name, last_name, age=None):
#     """
#     :param first_name:
#     :param last_name:
#     :param age:
#     :return:
#     """
#     person = {"first": first_name, "last": last_name}
#     if age:
#         person["age"] = age
#     return person
#
#
# musician = build_person("hussein", "el-hawary", 31)
# print(musician)

# def get_formatted_name(first_name, last_name):
#     """
#     return full name neatly formatted
#     :param first_name:
#     :param last_name:
#     :return: full name
#     """
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# while True:
#     print("\nPlease tell me your name:")
#     print("Enter 'q' at anytime to quit!")
#     f_name = input("First name: ")
#     if f_name == "q":
#         break
#     l_name = input("Last name: ")
#     if l_name == "q":
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello {formatted_name}!")


# def make_album(artist, title, songs=None):
#     album = {"artist": artist, "title": title, "songs": songs}
#     return album
#
#
# print(make_album("Hussein", "Album1"))
# print(make_album("Anas", "Album2", 10))

# def make_album(artist, title, songs=None):
#     album = {"artist": artist, "title": title, "songs": songs}
#     return album
#
#
# while True:
#     print("\nPlease enter the artist and album name and number of songs:")
#     print("Enter 'q' at anytime to quit!")
#
#     artist_name = input("Enter artist name: ")
#     if artist_name == "q":
#         break
#     album_title = input("Enter album title: ")
#     if album_title == "q":
#         break
#     songs_number = input("Enter songs number: ")
#     if songs_number == "q":
#         break
#
#     album = make_album(artist_name, album_title, songs_number)
#     print(album)

# passing a list to a function

# def great_users(names):
#     """
#     pass a list of users
#     :param names:
#     :return:
#     """
#     for name in names:
#         msg = f"Hello, {name.title()}"
#         print(msg)
#
#
# great_users(["hussein", "anas", "shaimaa", "mohamed"])


# def print_models(unprinted_designs, completed_models):
#     """
#     :param unprinted_designs:
#     :param completed_models:
#     :return:
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Current model: {current_design}")
#         completed_models.append(current_design)


# def show_completed_model(completed_models):
#     """
#     :param completed_models:
#     :return:
#     """
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model.title())
#
#
# unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
# completed_models = []
#
# print_models(unprinted_designs, completed_models)
# show_completed_model(completed_models)
#
# print(unprinted_designs)
# print(completed_models)

# passing an arbitrary number of arguments to the function
# the default value for arbitrary number of arguments is *args
# def make_pizza(size, *toppings):
#     """
#     :param size:
#     :param toppings:
#     :return:
#     """
#     print(f"\nMaking a {size} inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
#
#
# make_pizza(17, "peperoni")
# make_pizza(15, "mushroom", "green peppers", "extra cheese")

# passing any key-value number of arguments by using **kwargs & this is an empty dict and append in it
# def build_profile(first, last, **user_info):
#     user_info["first_name"] = first
#     user_info["last_name"] = last
#     return user_info
#
#
# user_profile = build_profile("hussein", "elhawary", location="cairo", field="software testing")
# print(user_profile)

make_pizza(17, "peperoni")
make_pizza(15, "mushroom", "green peppers", "extra cheese")