bicycle = ["trek", "cannondale", "redline", "specialized"]
print(bicycle[0].title())
message = f"My first bicycle was {bicycle[0].title()}."
print(message)

names = ["Ibrahim", "Khaled", "Amr", "Hassan"]
print(names[0])

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# replace list value
# motorcycles[0] = "ducati"
# print(motorcycles)

# add value to the end of the list
# motorcycles.append("ducati")
# print(motorcycles)

# insert method - Add item to a specific position in the list
# motorcycles.insert(0, "ducati")
# print(motorcycles)

# del method - delete item from a specific position in the list
# del motorcycles[0]
# print(motorcycles)

# pop method - remove the last item from the list & also you can pop from any position in the list
# last_motorcycle = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_motorcycle.title()}")
# first_motorcycle = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_motorcycle.title()}")

# remove method - remove element from the list by element value
# motorcycles.remove("yamaha")
# print(motorcycles)

# Organize the list elements
# sort method - sort the list alphabetically permanently and this change the original list
cars = ["bmw", "audi", "toyota", "subaru"]
# sort in a reversed way
# cars.sort(reverse=True)
# cars.sort()
# print(cars)

# sort the list temporary without changing the original list
# print(sorted(cars))
# print(cars)

# len method - return the list length
print(len(cars))
