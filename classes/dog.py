class Dog:
    """ A simple attempt to model a dog"""
    def __init__(self, name, age):
        """Initialize name and age attributes.
        self keyword refers to the class itself
        """
        self.name = name
        self.age = age

    def set(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over")


my_dog = Dog("Willie", 6)
your_dog = Dog("Lucky", 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.set()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.set()