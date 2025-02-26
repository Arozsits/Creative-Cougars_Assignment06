# File Name : main.py
# Student Name: Colton Ramsey
# email: ramseyc6@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 02/27/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Collaborate with a group to create a python solution that contains 3 different classes
# revolving around the same topic and a main that is used to call and insatiate all of the classes

# Brief Description of what this module does: The main will call and instatiate the classes created by the other group members
# Citations: None
# Anything else that's relevant: None

# Importing of all the packages / classes created by group members
from AR_package.mainCourse import *
# from RH_package. import *
from JP_package.sideDishes import *

# Entry point check that will contain all the code in main.py and ensure this is the entry point
if __name__ == "__main__":
    
    # Instantiation from RestaurantOrder class created by Andrew Rozsits
    main_order = RestaurantOrder("Burger", 2)
    print(main_order.__str__())

    # Instantiation from Side class created by Jay Powell
    side_order = Side("Waffle Fries", "Large", 3)
    print(side_order.__str__())

    # Instantiation from  class created by Ray Happel
    # drink_order = Drink() # Doesn't currently work

    meal_total = main_order.calculate_total() + side_order.calculate_total() #+drink_order.calculate_total()
    print("Cost of your Meal: ", meal_total)