# Write a function called poly_sum that takes 2 arguments, n and s.
# This function should sum the area and square of the perimeter of the regular polygon.
# The function returns the sum, rounded to 4 decimal places.
from math import tan, pi


def poly_sum(n, s):
    area = (0.25*n*s**2) / tan(pi / n)
    perimeter = 0
    for i in range(0, n):
        perimeter += s
    return round(area + perimeter**2, 4)
