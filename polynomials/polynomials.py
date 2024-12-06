"""This file contains the class Polynomial for Ex 3.3-5 of OOP4Maths."""

from numbers import Number
import numpy as np


class Polynomial:
    """
    The Polynomial class represents a polynomial function.

    :param coefs: tuple containing the polynomial coefficients
                  i-th coefficient represents the coefficient x^i  
    """

    def __init__(self, coefs):
        """Polynomial class constructor method."""
        self.coefficients = coefs

    def degree(self):
        """Returns the degree of the polynomial."""
        return len(self.coefficients) - 1

    def __str__(self):
        """Called by print() and returns a string representation of Polynomial."""
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        """Called by repr() and returns a string representation of Polynomial."""
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):
        """Vecks if Polynomials self and other are equal."""
        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):
        """Adds Polynomial self to Polynomial or Number other."""
        if isinstance(other, Polynomial):
            # Work out how many coefficient places
            # the two polynomials have in common.
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            # Append the high degree coefficients
            # from the higher degree summand.
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        """Adds Polynomial other to Number self."""
        return self + other

    def __sub__(self, other):
        """Subtracts Polynomial or Number other from Polynomial self."""
        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1

            coefs = tuple(a - b for a, b in zip(self.coefficients,
                                                other.coefficients))
            res = tuple(map(lambda i, j: i - j, self.coefficients[common:], other.coefficients[common:]))
            coefs += self.coefficients[common:]
            other_coefs = tuple(-i for i in other.coefficients[common:])
            coefs += other_coefs
            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __rsub__(self, other):
        """Subtracts Polynomial other from Number self."""
        return Polynomial(tuple(-i for i in self.coefficients)) + other

    def __mul__(self, other):
        """Multipliess Polynomial self with Polynomial or Number other."""
        if isinstance(other, Polynomial):
            result_poly=Polynomial((0,))
            for count, value in enumerate(self.coefficients):
                # build tuple
                temp_tup = tuple(i for i in np.zeros(count, dtype=int))
                result_tup = temp_tup + \
                             tuple(value * j for j in other.coefficients)
                # build associated Polynomial
                result_poly += Polynomial(result_tup)

            return result_poly

        elif isinstance(other, Number):
            return Polynomial(tuple(a * other for a in self.coefficients))

        else:
            return NotImplemented

    def __rmul__(self, other):
        """Multipliess Polynomial other with Number self."""
        return self * other

    def __pow__(self, power):
        """Raises Polynomial self to the power of other."""
        result = self
        for i in np.arange(power - 1):
            result *= self
        return result

    def __call__(self, x):
        """Returns the evaluation of a Polynomial self at a scalar value x."""
        result = 0
        for power, value in enumerate(self.coefficients):
            result += value * x ** power
        return result

    def dx(self):
        """Returns the derivative of a Polynomial self as a Polynomial."""
        # check for a single integer
        if self.degree() == 0:
            return Polynomial((0,))
        # differentiate polynomial of degree 1 or higher
        result_list = []
        for power, value in enumerate(self.coefficients):
            if power != 0:  
                result_list.append(power * value)
        return Polynomial(tuple(result_list)) 
        
def derivative(f):
    """Function returns the derivative of a Polynomial f as a polynomial."""
    return f.dx()

