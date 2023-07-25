from restaurant import Restaurant
from random import randint

restaurant = Restaurant("Papa Jons", "Italiano")
print(f"Restaurant name is {restaurant.restaurant_name}.")
print(f"Restaurant cuisine is {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(randint(1, 6))