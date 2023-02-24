#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand):
        self.brand = brand
        self.color = None
        self._size = None
        self.condition = None
    
    def set_size(self, new_size):
        if type(new_size) != int:
            print('idk')
        else:
            self._size = new_size
    
    def get_size(self):
        return self._size
    
    size = property(get_size, set_size)

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")



