import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, b):
        return math.sqrt((self.x-b.x)**2 + (self.y - b.y)**2)

class Circle(Vector):
    """This operates on the assumption that the given (x,y) is the midpoint of the circle."""
    def __init__(self, x, y, radius=None):
        super().__init__(x, y)
        self.radius = radius

# create two new circles
circle1 = Circle(4, 4.25)
circle2 = Circle(53, -5.35)

distance = circle1.calculate_distance(circle2)
print('distance', distance)

vector1 = Vector(-36, 97)
vector2 = Vector(.34, .91)
length = vector1.calculate_distance(vector2)
print('length', length)
