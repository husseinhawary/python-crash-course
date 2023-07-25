# magicians = ["alice", "david", "carolina"]
# for magician in magicians:
#     print(f"{magician.title()} that was a great trick.")
#
# print("\nThank you, everyone. That was a great magic show")

# Exercises
# pizzas = ["chicken ranch", "six cheese", "peperoni"]
# for pizza in pizzas:
#     print(f"I like {pizza.title()} pizza.")
#
# print("\nI really love pizza")

# Making numeric list
# range function takes two integers and execlude the last one from the list
# in the below example 6 value will be excluded
# for value in range(1, 6):
#     print(value)

# numbers = list(range(1, 6))
# print(numbers)
#
# for num in [1, 2, 3, 4, 5, 6]:
#     print(num)
#
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# exponential from 1 to 10
# squares = []
# for value in range(1, 11):
#     # square = value * value
#     square = value ** 2
#     squares.append(square)
#
# print(squares)
#
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# list comprehension
# squares = [value ** 2 for value in range(1, 11)]
# print(squares)

# numbers = list(range(1, 100001))
# for num in numbers:
#     print(num)
#
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# odd numbers
# for number in range(1, 21, 2):
#     print(number)

# multiplies of 3 from 3 to 30 numbers
#  = list(range(3, 31, 3))
# print(numbers)

# for cube in range(1, 11):
#     print(cube ** 3)

# cube by list comprehension
# cubes = [cube ** 3 for cube in range(1, 11)]
# print(cubes)


# Part from the list
# players = ["charles", "martina", "michael", "florence", "eli"]
# # taking a slice from the list from 0 to 3 but the last index not included, so "florence" will be excluded
# print(players[0:3])
# for player in players[:3]:
#     print(player.title())
# # print(players[:-1])

# slice is useful in taking a copy from the original list
# my_foods = ["pizza", "falafel", "carrot cake"]
# friend_foods = my_foods[:]
# print("My favorite foods are: ")
# print(my_foods)
#
# print("\nMy friend's favorite foods are: ")
# print(friend_foods)

# Tuple is an immutable list, it can not be changed but the list is mutable, it changeable
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for v in dimensions:
    print(v)
