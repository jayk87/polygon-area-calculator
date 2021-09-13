class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        pic = ""
        if max(self.height, self.width) > 50:
            return "Too big for picture."
        else:
            for i in range(self.height):
                pic += "*" * self.width + "\n"
            return pic

    def get_amount_inside(self, shape):
        max1 = max(self.width, self.height)
        max2 = max(shape.width, shape.height)
        min1 = min(self.width, self.height)
        min2 = min(shape.width, shape.height)
        fitnum = max((max1 // max2) * (min1 // min2), (min1 // max2) * (max1 // min2))
        return fitnum

    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width
        self.side = width

    def set_height(self, height):
        self.height = height
        self.width = height
        self.side = height

    def __str__(self):
        return 'Square(side={})'.format(self.side)
