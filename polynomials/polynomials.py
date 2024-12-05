from numbers import Number
import numpy as np


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
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
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):

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
        return Polynomial(tuple(-i for i in self.coefficients)) + other

    def __mul__(self, other):

        if isinstance(other, Polynomial):
            result_poly=Polynomial((0,))
            for count, value in enumerate(self.coefficients):
                # build tuple
                temp_tup = tuple(i for i in np.zeros(count, dtype=int))
                result_tup = temp_tup + \
                             tuple(value * j for j in other.coefficients)
                result_poly += Polynomial(result_tup)

            return result_poly

        elif isinstance(other, Number):
            return Polynomial(tuple(a * other for a in self.coefficients))

        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __pow__(self, other):
        result = self
        for i in np.arange(other - 1):
            result *= self
        return result

    def __call__(self, other):
        x = other
        result_final = 0
        for power, value in enumerate(self.coefficients):
            result_final += value * x ** power
        return result_final




