# mainCourse.py



class RestaurantOrder:
    def __init__(self, main_course=None, quantity=1):
        self.menu = {
            "Burger": 10.99,
            "Chicken Sandwich": 9.99,
            "Sliders": 8.99
        }
        
        if main_course is None or main_course not in self.menu:
            raise ValueError("A valid main course must be selected.")
        
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        self._main_course = main_course
        self._quantity = quantity
    
    # Getter for main_course
    @property
    def main_course(self):
        return self._main_course
    
    # Setter for main_course
    @main_course.setter
    def main_course(self, value):
        if value not in self.menu:
            raise ValueError("Invalid main course selection.")
        self._main_course = value
    
    # Getter for quantity
    @property
    def quantity(self):
        return self._quantity
    
    # Setter for quantity
    @quantity.setter
    def quantity(self, value):
        if value < 1:
            raise ValueError("Quantity must be at least 1.")
        self._quantity = value
    
    # Method to calculate total price
    def calculate_total(self):
        return self.menu[self._main_course] * self._quantity
    
    def __str__(self):
        return f"Order: {self._quantity} x {self._main_course} - Total: ${self.calculate_total():.2f}"