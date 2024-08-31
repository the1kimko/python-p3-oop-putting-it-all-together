#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"  # Default condition to 'New'

    # Size property with validation
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")
            self._size = 0  # Default to 0 or any safe value

    # Method to simulate cobbling the shoe
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"