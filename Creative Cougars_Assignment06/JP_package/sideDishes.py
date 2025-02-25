# File Name: sideDishes.py
# Student Name: Jay Powell
# email: powela9@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 2/27/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: 
   # This assignment develops a Python project to model a fast-food order with a main meal, side, and drink
# Brief Description of what this module does: 
   #The Side class models a side item in a fast-food order, storing its name, size, quantity, and calculating the total price based on a shared price list.
# Citations: 
    #Had to determine whether to put prices in the class itself or in the __init__
    #https://stackoverflow.com/questions/24739850/python-using-init-vs-just-defining-variables-in-class-any-difference
# Anything else that's relevant: Placed Price outside of the __init__ because it is shared across all instances because price is the same for all sides
    # Modeled prices off of Wendy's prices (aside from large chicken nugget)



class Side(object):
    """
    Models a side item in a fast-food order.
    """

    Price_List = {
        "French Fries": {"Small": 1.59, "Medium": 3.49, "Large": 3.79},
        "Waffle Fries": {"Small": 1.59, "Medium": 3.49, "Large": 3.79},
        "Chicken Nuggets": {"Small": 2.29, "Medium": 3.29, "Large": 3.59},
    }

    def __init__(self, name, size, quantity):
        """
        Constructor
        @param name: String - The type of side (French Fries, Waffle Fries, Chicken Nuggets)
        @param size: String - The size of the side (Small, Medium, Large)
        @param quantity: int - Number of items ordered
        """
        self.set_name(name)
        self.set_size(size)
        self.set_quantity(quantity)

    # Property for price
    @property
    def price(self):
        """ Returns the price per unit based on the name and size. """
        return self.Price_List[self.__name][self.__size]

    # Name of the side
    def get_name(self):
        """ Returns the name of the side. """
        return self.__name

    def set_name(self, name):
        """ 
        Sets the side name, ensuring it's valid.
        @param name: String - Must be a valid menu item.
        """
        if name not in self.Price_List:
            raise Exception("Invalid side. Please choose from French Fries, Waffle Fries, or Chicken Nuggets.")
        self.__name = name

    # Size of the side
    def get_size(self):
        """ Returns the size of the side. """
        return self.__size

    def set_size(self, size):
        """
        Sets the size, ensuring it's valid.
        @param size: String - Must be Small, Medium, or Large.
        """
        if size not in ["Small", "Medium", "Large"]:
            raise Exception("Invalid size. Please choose Small, Medium, or Large.")
        self.__size = size

    # How many did they order
    def get_quantity(self):
        """ Returns the quantity of the side ordered. """
        return self.__quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity, ensuring it's a positive integer.
        @param quantity: int - Must be greater than 0.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise Exception("Quantity must be a positive integer.")
        self.__quantity = quantity

    def __str__(self):
        """
        Returns a string representation of the side item.
        """
        return f"{self.__quantity}x {self.__size} {self.__name} - ${self.price * self.__quantity:.2f}"

    def __repr__(self):
        """
        Returns a string that can be used to recreate the object.
        """
        return f"Side('{self.__name}', '{self.__size}', {self.__quantity})"


