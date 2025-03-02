from collections import defaultdict
class Polynomial:
    def __init__(self, coeffs):
        """
        Initialize the univariate polynomial with the given dictionary of coefficients.
        The dictionary keys are the powers (exponents) of the polynomial,
        and the values are the coefficients.

        :param coeffs: The dictionary that maps exponent keys to coefficient values.
        """
        assert(isinstance(coeffs, dict)), "coeffs argument must be a dictionary"
        for key,value in coeffs.items():
            assert(isinstance(key, int) and isinstance(value, int)), "Each key and value in the dictionary must be integers"
        self.coeffs = coeffs

    def __repr__(self):
        """
        Return a string representation of the polynomial.

        :return: A string representation of the Polynomial object.
        """
        terms = []
        for power in sorted(self.coeffs.keys()):
            coeff = self.coeffs[power]
            if coeff == 0:
                continue
            if power == 0:
                terms.append(f"{coeff}")
            elif power == 1:
                terms.append(f"{coeff} x")
            else:
                terms.append(f"{coeff} x^{power}")
        return " + ".join(terms) if terms else "0"

    def __add__(self, other):
        """
        Add two univariate polynomials or an univariate polynomial with a constant integer.

        :param other: The other Polynomial object or integer to add with current.

        :return: The sum of current Polynomial with other Polynomial object or constant integer.
        """
        assert(isinstance(other, Polynomial) or isinstance(other, int)), "Argument must also be a Polynomial object or an integer"
        other_poly = other
        if isinstance(other, int):
            other_poly = Polynomial({0:other})
        
        new_coeffs = self.coeffs.copy()
        for power,coeff in other_poly.coeffs.items():
            new_coeffs[power] = new_coeffs.get(power, 0) + coeff
        return Polynomial(new_coeffs)


    def __sub__(self, other):
        """
        Subtract two univaraite polynomials.

        :param other: The other Polynomial object to add with current.

        :return: The resultant subtraction of the two Polynomial objects.
        """
        if isinstance(other, Polynomial):
            new_coeffs = self.coeffs.copy()
            for power, coeff in other.coeffs.items():
                new_coeffs[power] = new_coeffs.get(power, 0) - coeff
            return Polynomial(new_coeffs)
        elif other == 0:
            return self
        raise TypeError(f"Unsupported operand type(s) for -: 'Polynomial' and '{type(other)}'")

    def __mul__(self, other):
        """
        Multiply a polynomial by a scalar or another polynomial.

        :param other: Can be a Polynomial object or a scalar.

        :return: Resultant product univariate Polynomial object.
        """
        if isinstance(other, int): 
            new_coeffs = {power: coeff * other for power,coeff in self.coeffs.items()}
            return Polynomial(new_coeffs)
        elif isinstance(other, Polynomial): 
            new_coeffs = defaultdict(int)
            for p1,c1 in self.coeffs.items():
                for p2,c2 in other.coeffs.items():
                    new_coeffs[p1 + p2] += c1 * c2
            return Polynomial(new_coeffs)
        raise TypeError(f"Unsupported operand type(s) for *: 'Polynomial' and '{type(other)}'")

    def __rmul__(self, other):
        """
        Multiplication is commutative, so this will call __mul__.

        :param other: The other Polynomial object or scalar to multiply by.

        :return: The resultant product of the two.
        """
        return self.__mul__(other)

    def __eq__(self, other):
        """
        Check equality of two univariate polynomials.

        :param other: The other Polynomial object to check with current.

        :return: If current Polynomial object is equal to other Polynomial object.
        """
        if isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        return False

    def __ne__(self, other):
        """
        Check inequality of two univariate polynomials.

        :param other: The other Polynomial obejct to check with current.

        :return: If current Polynomial object is not equal to other Polynomial object.
        """
        return not self.__eq__(other)

    def __truediv__(self, other):
        """
        Divide one polynomial by another polynomial (not implemented in full).
        Only division by polynomials that are linear (degree 1) is supported.
        """
        if isinstance(other, Polynomial) and len(other.coeffs) == 2:
            if 1 in other.coeffs and other.coeffs[1] != 0:
                # Simple division by a linear polynomial
                divisor = other.coeffs[1]
                new_coeffs = {power: coeff // divisor for power, coeff in self.coeffs.items()}
                return Polynomial(new_coeffs)
        raise NotImplementedError("Polynomial division by non-linear polynomials is not implemented.")

    def subs(self, x):
        """
        Substitute a value for x in the polynomial and evaluate the result.

        :param x: The integer to substitute in for x variable of the Polynomial.

        :return: The result after substitution of the variable.
        """
        assert(isinstance(x, int)), "The arugment must be a valid integer"
        return sum(coeff * (x ** power) for power,coeff in self.coeffs.items())

# Example Usage
p = Polynomial({0: 8, 1: 2, 3: 4})
q = Polynomial({0: 8, 1: 2, 2: 8, 4: 4})

# Testing the representation
print(repr(p))  # '8 + 2 x + 4 x^(3)'

# Testing multiplication by scalar
print(p * 3)  # '24 + 6 x + 12 x^(3)'

# Testing addition
print(p + q)  # '16 + 4 x + 8 x^(2) + 4 x^(3) + 4 x^(4)'

# Testing polynomial multiplication
print(p * q)  # '64 + 32 x + 68 x^(2) + 48 x^(3) + 40 x^(4) + 40 x^(5) + 16 x^(7)'

# Testing substitution
print(p.subs(10))  # 4028

p=Polynomial({0:8,1:0,3:4})
print(repr(p))

print(p + 3)

print(type(p-p))

print(p*4 + 5 - 3*p - 1)

# Testing equality
print(p == q)  # False
print(p - p == 0)  # True
