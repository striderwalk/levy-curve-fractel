import math
from point import Point
class Tortoise():
    """
    a turtle that doesn't draw
    cus turtle is slow
    """
    __slots__ = ["pos", "angle"]
    
    def __init__(self, pos = (0,0), angle = 0):
        self.pos = Point(*pos)
        self.angle = angle

    
    def fd(self, dis):
        angle = math.radians(self.angle)
        delta_x = dis*math.cos(angle)
        delta_y = dis*math.sin(angle)

        self.pos += (delta_x, delta_y)

    def left(self, angle):
        self.angle += angle

    def right(self, angle):
        self.angle -= angle


    def clone(self):
        return Tortoise(self.pos, self.angle)