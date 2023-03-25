class Rectangle:
    def __init__self(self, length, width):
        self.length = length
        self.width = width

        def area(self):
            return self.length * self.width

        def perimeter(self):
            return (self.length + self.width) * 2

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)