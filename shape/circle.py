"""This file contains the class Circle for Ex 3.6 of OOP4Maths."""

import math


class Circle:
    """
    The Circle class reprents a circle.

    :param centre: two-dimensional coordinates of the centre
    :param radius: radius of circle.
    """

    def __init__(self, centre, radius):
        """Circle class constructor method."""
        self.centre = centre
        self.radius = radius

    def __contains__(self, point):
        """Call by the keyword in."""
        return math.dist(self.centre, point) < self.radius

