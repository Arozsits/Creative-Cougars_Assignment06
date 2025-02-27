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
    # https://stackoverflow.com/questions/24739850/python-using-init-vs-just-defining-variables-in-class-any-difference
    # https://stackoverflow.com/questions/45883083/why-should-i-use-the-property-decorator-in-python
# Anything else that's relevant: 
    # Placed Price outside of the __init__ because it is shared across all instances because price is the same for all sides
    # Used @property for the price method to allow attribute-like access while ensuring it updates automatically and can't be changed directly.

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
        Assign values to the name, size, and quantity of the side order.
        @param name String: The type of side (French Fries, Waffle Fries, Chicken Nuggets)
        @param size String: The size of the side (Small, Medium, Large)
        @param quantity int: Number of items ordered
        """
        self.set_name(name)
        self.set_size(size)
        self.set_quantity(quantity)

    @property
    def price(self):
        """ 
        Calculates the price based on given parameters and saved information.
        @return float: Price per unit based on the name and size.
        """
        return self.Price_List[self.get_name()][self.get_size()]

    def get_name(self):
        """ 
        Retreives the item name from the class object
        @return String: The name of the side.
        """
        return self.__name

    def set_name(self, name):
        """ 
        Assign a value to the side name, ensuring it's valid.
        @param name String: Must be a valid menu item.
        """
        if name not in self.Price_List:
            raise Exception("Invalid side. Please choose from French Fries, Waffle Fries, or Chicken Nuggets.")
        self.__name = name

    def get_size(self):
        """
        Retreives the size from the class object
        @return String: The size of the side.
        """
        return self.__size

    def set_size(self, size):
        """
        Assign a value to the side size, ensuring it's valid.
        @param size String: Must be Small, Medium, or Large.
        """
        if size not in ["Small", "Medium", "Large"]:
            raise Exception("Invalid size. Please choose Small, Medium, or Large.")
        self.__size = size

    def get_quantity(self):
        """ 
        Retreives the quantity from the class object
        @return int: The quantity of the side ordered.
        """
        return self.__quantity

    def set_quantity(self, quantity):
        """
        Assign a value to the side quantity, ensuring it's a positive integer.
        @param quantity int: Must be greater than 0.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise Exception("Quantity must be a positive integer.")
        self.__quantity = quantity

    def calculate_total(self):
        """
        Calculates the total cost of the side order
        @return float: The total cost of the side order.
        """
        return self.price * self.get_quantity()

    def __str__(self):
        """
        Generate a string representation of the side order.
        @returns String: A formatted string showing the order details, including side name, size, quantity, and total price.
        """
        return f"Order: {self.get_quantity()} x {self.get_size()} {self.get_name()} - Total: ${self.calculate_total():.2f}"

