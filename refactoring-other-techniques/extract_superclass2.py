import math

class Vector:
    def __init__(self, x, y, visible=True):
        self.x = x
        self.y = y
        self.visible = visible

    def set_visible(self,is_visible):
        self.visible = is_visible

    def hide(self):
        self.visible = False

class Circle(Vector):
    """This operates on the assumption that the given (x,y) is the midpoint of the circle."""
    def __init__(self, x, y, radius, visible = True):
        super().__init__(x, y)
        self.radius = radius

    def display(self):
        print('drew the circle.')

    def get_center(self):
        return self.x, self.y

class Rectangle(Vector):
    def __init__(self, x, y, width, height, visible = True):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def display(self):
        if self.visible:
            print('drew the rectangle.')

    def make_visible(self):
        self.set_visible(True)

    def get_center(self):
        return self.x + self.width/2, \
               self.y + self.height/2



if __name__ == "__main__":
    circle = Circle(0,0,10, False)
    circle.set_visible(True)
    circle.display()
    print('center point',circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.hide()
    rect.display() # does not display because it's hidden.
    rect.make_visible()
    rect.display()
    print('center point',rect.get_center())
