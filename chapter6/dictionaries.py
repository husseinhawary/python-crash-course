# alien_0 = {"color": "green", "points": 5}
# print(alien_0)
# print(alien_0["color"])
# print(alien_0["points"])
#
# alien_0["x_position"] = 0
# alien_0["y_position"] = 25
# print(alien_0)

# Empty dictionary
# alien_0 = {}
#
# alien_0["color"] = "green"
# alien_0["points"] = 5
# print(alien_0)

# alien_0 = {"color": "green", "points": 5}
# print(f"The alien is {alien_0['color']}")
# alien_0["color"] = "yellow"
# print(f"The alien is {alien_0['color']}")

# alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
# print(f"Original position: {alien_0['x_position']}")
#
# if alien_0["speed"] == "slow":
#     x_increment = 1
# elif alien_0["speed"] == "medium":
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0["x_position"] += x_increment

# print(f"New position: {alien_0['x_position']}")

# delete dictionary key by del method
# alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
# print(alien_0)
# del alien_0["speed"]
# print(alien_0)

# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "ruby",
#     "phil": "python"
# }
# language = favorite_languages["sarah"].title()
# print(language)
# # get dict key value by using get method and pass to it a message to be printed in case of the key not exists
# print(favorite_languages.get("hussein", "No such key"))

# user_0 = {
#     "username": "hhawary",
#     "first": "hussein",
#     "last": "elhawary"
# }
# for k, v in user_0.items():
#     print(f"Key is: {k} && Value: is {v}.")
#
# for key in user_0.keys():
#     print(f"Key is: {key.title()}")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")

print("*" * 50)

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("*" * 50)

for value in set(favorite_languages.values()):
    print(f"{value.title()}")