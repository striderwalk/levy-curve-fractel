"""
https://en.wikipedia.org/wiki/L%C3%A9vy_C_curve
"""

import turtle,time
from tortoise import Tortoise
from point import Point
from draw import Draw



def rule(construction):
    new = []
    for i in construction:
        if i == "f":
            new.extend(["-", "f", "+", "+", "f", "-"])
        else:
            new.append(str(i))
    return new


def fd(pen, dis): pen.fd(dis)
def right(pen, dis): pen.right(45)
def left(pen, dis): pen.left(45)

def make(construction, dis):
    pen = Tortoise((-175,-100))
    rules = {"f": fd, "+": right, "-": left}
    points = [pen.pos]
    for i in construction:
        rules[i](pen, dis)
        points.append(pen.pos)

    return points

construction = ["f"]
dis = 350
for i in range(20):
    new_dis = dis/ 2**(i/2)

    points = make(construction, new_dis)
    Draw.draw(points, HOLD=False, wait=30)
    construction = rule(construction)
Draw.draw(points)


