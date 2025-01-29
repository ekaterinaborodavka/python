# Task 15.1
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        total_square = self.get_square() + other.get_square()
        return Rectangle(1, total_square)

    def __mul__(self, n):
        new_height = self.height*n
        return Rectangle(self.width, new_height)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

# Task 15.2
class Fraction:
    def __init__(self, a, b):
        self.numerator = a
        self.denominator = b
        if b == 0:
            raise ValueError("The denominator cannot be zero")

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise ValueError("Illegal type of the argument")

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_denominator = self.denominator * other.denominator
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise ValueError("Illegal type of the argument")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_denominator = self.denominator * other.denominator
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise ValueError("Illegal type of the argument")

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == self.denominator * other.numerator
        else:
            raise ValueError("Illegal type of the argument")

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > self.denominator * other.numerator
        else:
            raise ValueError("Illegal type of the argument")

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < self.denominator * other.numerator
        else:
            raise ValueError("Illegal type of the argument")

    def __str__(self):
        return f"Fraction: {self.numerator}, {self.denominator}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
