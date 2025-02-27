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
# Citations: https://www.w3schools.com/python/gloss_python_elif.asp, https://stackoverflow.com/questions/55319189/assign-value-of-1-to-positive-and-0-to-negative-numbers-in-a-list, https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr, 
# Anything else that's relevant: None

class DrinkOrder (object):
    # Constructor, initializing name, size and price attributes
    """
    Models a drink item in a fast-food order.
    """

    Price_List = {
        "Soft Drink": {"Small": 1.00, "Medium": 2.00, "Large": 3.00},
        "Milk shake": {"Small": 2.00, "Medium": 3.00, "Large": 4.00},
    }

    def __init__(self, drink, size, quantity):
        """
        Assign values to the drink, size, and quantity of the drink order.
        @param drink String: The type of drink (Soft drinks, Milk shake)
        @param size String: The size of the side (Small, Medium, Large)
        @param quantity int: Number of items ordered (Can be zero or more)
        """
        self.set_drink(drink)
        self.set_size(size)
        self.set_quantity(quantity)
        
    @property
    def price(self):
        """ 
        Retrieve the price of the drink order placed by the customer
        @return float: Price per drink based on the name and size.
        """
        return self.Price_List[self.get_name()][self.get_size()]

    def get_drink(self):
        """ 
        Retrieve the name of the drink(s) ordered by the custoemr.
        @return String: The name of the drink ordered by the customer.
        """
        return self.__drink

    def set_drink(self, drink):
        """ 
        Assign a value to the drink name, and ensure it's valid.
        @param name String: Must be a valid drink menu item.
        @raises ValueError: If the drink ordered is not on the drink order.
        """
        if drink not in self.Price_List:
            raise Exception("Invalid drink. Please choose from Soft drink, or Milk shake.")
        self.__drink = drink

    def get_size(self):
        """ 
        @return String: The size of the drink ordered by the customer.
        """
        return self.__size

    def set_size(self, size):
        """
        Assign a value to the drink size, ensuring it's valid.
        @param size String: Must be Small, Medium, or Large.
        """
        if size not in ["Small", "Medium", "Large"]:
            raise Exception("Invalid size. Please choose Small, Medium, or Large.")
        self.__size = size

    def get_quantity(self):
        """ 
        @return int: The quantity of the drink ordered.
        """
        return self.__quantity

    def set_quantity(self, quantity):
        """
        Assigning a value to the drink quantity, can be a positive integer, or customers can choose not to order a drink.
        @param quantity int: The drink quantity can be a positive integer or zero.
        @raises ValueError: If quantity ordered is less than zero.
        """
        while True:
            try:
                if quantity >= 0:
                    return quantity
                else:
                    print("Quantity must be zero or a positive integer.")
            except ValueError: print ("Invalid input. Please enter an integer that is positive or zero.")
        self.__quantity = quantity

    def calculate_total(self):
        """
        @return float: The total cost of the drink order.
        """
        return self.price * self.get_quantity()

    def __str__(self):
        """
        @return String: A formatted description of the drink item.
        """
        return f"{self.get_quantity()}x {self.get_size()} {self.get_name()} - ${self.calculate_total():.2f}"

    
    

    



