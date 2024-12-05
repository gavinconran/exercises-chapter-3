import math


class Circle:

    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def __contains__(self, point):
        return math.dist(self.centre, point) < self.radius



