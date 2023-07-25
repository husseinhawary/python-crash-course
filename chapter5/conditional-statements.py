# cars = ["audi", "bmw", "subaru", "toyota"]
# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())

# answer = 17
# if answer != 42:
#     print("That is not a correct answer.")

# age0 = 22
# age1 = 18
# print(age0 >= 21 and age1 >= 21)

# requested_topping = ["mushroom", "onions", "pineapple"]
# print("mushroom" in requested_topping)
#
# banned_users = ["andrew", "carolina", "david"]
# user = "marie"
# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish.")

# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40
#
# print(f"Your admission cost is ${price}.")

# requested_toppings = ["extra cheese"]
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         if requested_topping == "green peppers":
#             print("Sorry, we are out of green peppers right now.")
#         else:
#             print(f"Adding {requested_topping}.")
#
#     print("\nFinished making your pizza.")
# else:
#     print("Are you sure you want a plain pizza ?")

available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have a {requested_topping}.")
print("\nFinished making a pizza.")