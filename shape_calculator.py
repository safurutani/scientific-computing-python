class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.height * self.width
    def get_perimeter(self):
        return (2 * self.height) + (2 * self.width)
    def get_diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** 0.5
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        w = "*" * self.width
        pic = ""
        #adds a "*" new line of the appropriate width until it's the right height
        for x in range(self.height):
            if x != self.height:
                pic += w + "\n"
        return pic
    def get_amount_inside(self, Rectangle):
        fit_h = int(self.height / Rectangle.height)
        fit_w = int(self.width / Rectangle.width)
        return fit_w * fit_h

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
        #super().__init__(self, side)
    def set_side(self, num):
        self.width = num
        self.height = num
    def __repr__(self):
        return f"Square(side={self.width})"
    def set_width(self, width):
        self.width = width
        self.height = width
    def set_height(self, height):
        self.width = height
        self.height = height