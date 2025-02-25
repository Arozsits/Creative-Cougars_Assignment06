# File Name : drink.py
# Student Name: Ray Happel
# email: happelrc@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 02/27/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Collaborate with a group to create a python solution that contains 3 different classes
# revolving around the same topic and a main that is used to call and insatiate all of the classes

# Brief Description of what this module does: The main will call and instatiate the classes created by the other group members
# Citations: https://www.w3schools.com/python/gloss_python_elif.asp, https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr, 
# Anything else that's relevant: None

class Drink:
    # Constructor, initializing name, size and price attributes
    def __init__(self, name, size):
        self._name = name
        self._size = size
        self._price = self._set_price(size)

    
    def name(self):
        return self._name

    # Specify name of drink the customer ordered
    def name(self, value):
        self._name = value

    # Define price attribute
    def price(self):
        return self._price

    # Allow prices to be assigned a value
    def price(self, value):
        self._price = value

    # Define sizes for all drinks
    def size(self):
        return self._size

    def size(self, value):
        self._size = value
        self._price = self._set_price(value)  # Update price based on size
    
    # Setting price based on the size the customer ordered
    def _set_price(self, size):
        if size == "Small":
            return 1.00
        elif size == "Medium":
            return 2.00
        elif size == "Large":
            return 3.00
        return 0  # Default if size is not recognized
       
    # String for showing name, size and price of drink ordered by customer
    def __str__(self):
        return "{self.name} ({self.size}) - ${self.price}"

    def __repr__(self):
        return "Drink ordered: (name={self.name}, size={self.size}, price={self.price})"


class SoftDrink(Drink):
    # List of available soft drinks
    available_drinks = ["Coke", "Diet Coke", "Dr Pepper", "Root Beer", "Sprite"]

    def __init__(self, name, size):
        if name not in SoftDrink.available_drinks:
            raise ValueError("Invalid soft drink selection. Choose from {(SoftDrink.available_drinks)}") # Returns if customer orders a soft drink not listed
        super().__init__(name, size)

    def __str__(self):
        return "{super().__str__()} (Soft Drink)"

    # Show name of soft drink, size and price specifically from customer order
    def __repr__(self):
        return "Soft drink ordered: (name={self.name}, size={self.size}, price={self.price})"


class MilkShake(Drink):
    # List of available milkshake flavors
    available_flavors = ["Vanilla", "Chocolate", "Strawberry"]

    def __init__(self, name, size, flavor):
        if flavor not in MilkShake.available_flavors:
            raise ValueError("Invalid milkshake flavor. Choose from {', '.join(MilkShake.available_flavors)}") # Returns if customer orders a flavor not listed
        super().__init__(name, size) 
        self._flavor = flavor
        self._price = self._set_milkshake_price(size)  # Milkshake has its own pricing

    def flavor(self):
        return self._flavor

    # Sets milkshake flavor
    def flavor(self, value):
        self._flavor = value
    
    # Setting milkshake price per size
    def _set_milkshake_price(self, size):
        if size == "Small":
            return 2.00
        elif size == "Medium":
            return 3.00
        elif size == "Large":
            return 4.00
        return 0  # Default if size is not recognized

    def change_flavor(self, new_flavor):
        if new_flavor not in MilkShake.available_flavors:
            raise ValueError("Invalid milkshake flavor. Choose from {(MilkShake.available_flavors)}") # Returns if customer orders a flavor not listed
        self.flavor = new_flavor
        print("Flavor of {self.name} changed to {self.flavor}.")

    def __str__(self):
        return "{super().__str__()} - Flavor: {self.flavor} (Milkshake)"

    # Show name of milk shake, size and price specifically from customer order
    def __repr__(self):
        return "Milk shake ordered: (name={self.name}, size={self.size}, price={self.price}, flavor={self.flavor})"



