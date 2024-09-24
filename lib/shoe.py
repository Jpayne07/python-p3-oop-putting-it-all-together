#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
    def cobble(self):
        print('Your shoe is as good as new!')
        self.condition = "New"

    def get_condition(self):
        return self._condition  
    
    def set_condition(self, condition):
        self._condition = condition

    # Property for condition
    condition = property(get_condition, set_condition)
            
         

    size = property(get_size, set_size)

adidas = Shoe("Adidas", 11)