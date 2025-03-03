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
                terms.append(f"x")
            else:
                terms.append(f"{coeff} x^{power}")
        return " + ".join(terms) if terms else "0"

    def __add__(self, other):
        """
        Add two univariate polynomials or a univariate polynomial with a constant integer.

        :param other: The other Polynomial object or integer to add with current.

        :return: The sum of current Polynomial with other Polynomial object or constant integer.
        """
        assert(isinstance(other, Polynomial) or isinstance(other, int)), "Argument must also be a Polynomial object or an integer"
        if isinstance(other, int):
            other = Polynomial({0:other})
        
        new_coeffs = self.coeffs.copy()
        for power,coeff in other.coeffs.items():
            new_coeffs[power] = new_coeffs.get(power, 0) + coeff
        return Polynomial(new_coeffs)


    def __sub__(self, other):
        """
        Subtract two univaraite polynomials or a univariate polynomial and an integer.

        :param other: The other Polynomial object or integer to subtract with current.

        :return: The resultant subtraction of the two Polynomial objects or constant integer.
        """
        assert(isinstance(other, Polynomial) or isinstance(other, int)), "Argument must also be a Polynomial object or an integer"
        if isinstance(other, int):
            other = Polynomial({0:other})
        
        new_coeffs = self.coeffs.copy()
        for power,coeff in other.coeffs.items():
            new_coeffs[power] = new_coeffs.get(power, 0) - coeff
        return Polynomial(new_coeffs)

    def __mul__(self, other):
        """
        Multiply a polynomial by a scalar or another polynomial.

        :param other: Can be a Polynomial object or a scalar.

        :return: Resultant product univariate Polynomial object.
        """
        assert(isinstance(other, Polynomial) or isinstance(other, int)), "Argument must be Polynomial object or an integer"
        if isinstance(other, int): 
            new_coeffs = {power: coeff * other for power,coeff in self.coeffs.items()}
            return Polynomial(new_coeffs)
        if isinstance(other, Polynomial): 
            new_coeffs = defaultdict(int)
            for p1,c1 in self.coeffs.items():
                for p2,c2 in other.coeffs.items():
                    new_coeffs[p1 + p2] += c1 * c2
            return Polynomial(new_coeffs)

    def __rmul__(self, other):
        """
        Multiplication is commutative, so this will call __mul__.

        :param other: The other Polynomial object or scalar to multiply by.

        :return: The resultant product of the two.
        """
        return self.__mul__(other)

    def __eq__(self, other):
        """
        Check equality of two univariate polynomials or univariate polynomial with a constant integer.

        :param other: The other Polynomial object or integer to check with current.

        :return: True if current Polynomial object is equal to other Polynomial object or integer, False otherwise.
        """
        assert(isinstance(other, Polynomial) or isinstance(other, int)), "Argument must be a Polynomial or an integer"
        if isinstance(other, int):
            new_coeffs = self.coeffs.copy()
            for power,coeff in new_coeffs.items():
                if power == 0:
                    new_coeffs[power] = other
                else:
                    new_coeffs[power] = 0
            other = Polynomial(new_coeffs)
        return self.coeffs == other.coeffs

    def __ne__(self, other):
        """
        Check inequality of two univariate polynomials or univariate polynomial with a constant integer.

        :param other: The other Polynomial object or integer to check with current.

        :return: False if current Polynomial object is equal to other Polynomial object or integer, True otherwise.
        """
        return not self.__eq__(other)

    def __truediv__(self, other):
        """
        Perform polynomial division (long division) between
        this Polynomial and other Polynomial or an integer.
        
        :param other: A Polynomial object or a constant integer

        :return: The quotient result after division.
        """
        assert(isinstance(other, Polynomial) or isinstance(other, int)), "Argument must be a Polynomial or an integer"
        if isinstance(other, int):
            assert(other != 0), "Cannot divide by 0"
        if isinstance(other, int):
            for power,coeff in self.coeffs.items():
                self.coeffs[power] = coeff // other
            return self

        num = self.coeffs.copy()
        den = other.coeffs.copy()
        quotient = {}

        num_deg = max(num.keys()) if num else 0
        den_deg = max(den.keys())

        while num and num_deg >= den_deg:
            lead_coeff = num[num_deg] // den[den_deg]
            lead_power = num_deg - den_deg
            quotient[lead_power] = lead_coeff

            subtrahend = {p + lead_power: c * lead_coeff for p, c in den.items()}
            num = {p: num.get(p, 0) - subtrahend.get(p, 0) for p in set(num) | set(subtrahend)}

            num = {p: c for p, c in num.items() if c != 0}
            num_deg = max(num.keys()) if num else 0

        if num:
            raise NotImplementedError(f"Polynomial division is implemented for cases in which there is a remainder")
        return Polynomial(quotient)

    def subs(self, x):
        """
        Substitute a value for x in the polynomial and evaluate the result.

        :param x: The integer to substitute in for x variable of the Polynomial.

        :return: The result after substitution of the variable.
        """
        assert(isinstance(x, int)), "The arugment must be a valid integer"
        return sum(coeff * (x ** power) for power,coeff in self.coeffs.items())

if __name__ == "__main__":
    p=Polynomial({0:8,1:2,3:4}) # keys are powers, values are coefficients
    q=Polynomial({0:8,1:2,2:8,4:4})
    print(repr(p))
    print(p*3)
    print(3*p)
    print(p+q)
    print(p*4 + 5 - 3*p - 1)
    print(type(p-p)) # zero requires special handling but is still a Polynomial
    print(p*q)
    print(p.subs(10)) # substitute in integers and evaluate
    print((p-p) == 0)
    print(p == 0)
    print(p == q)
    p=Polynomial({0:8,1:0,3:4}) # keys are powers, values are coefficients
    print(repr(p))
    p = Polynomial({2:1,0:-1})
    q = Polynomial({1:1,0:-1})
    print(repr(p))
    print(repr(q))
    print(p/q)
    print(p  / Polynomial({1:1,0:-3})) # raises NotImplementedError
    p = Polynomial({2:3,0:-3})
    #print(p / 3)