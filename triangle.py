# In this task I have added some validation rules:
# 1 - all sides should be >0
# 2 - the triangle should exist
import re
from math import sqrt


class Triangle(object):
    def __init__(self, data):
        self.name = data[0]
        self.a = data[1]
        self.b = data[2]
        self.c = data[3]
        self.s = self.area()

    def area(self):
        p = (self.a + self.b + self.c)/2
        return sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))


def input_triangle():
    data = raw_input('Enter Triangle (name, a, b, c): ').split(',')
    try:
        name = re.sub(r'\s+', ' ', data[0])
        if name[0] == ' ':
            name = name[1:]
        a = float(data[1])
        b = float(data[2])
        c = float(data[3])
        # Sides should be positive
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError
    except IndexError:
        print "Oops! The triangle's name is required"
    except ValueError:
        print "Ooops! The length of sides must be real positive number!"
    else:
        # Check that triangle exists
        if a < b + c and b < a + c and c < a + b:
            return name, a, b, c
        else:
            print "Ooops! Such triangle doesn't exist!"
            return None

def print_triangles(triangles):
    print("=======TRIANGLES:================")
    triangles.sort(key=lambda triangle: triangle.s, reverse = True)
    for triangle in triangles:
        print "[%s]: %.2f cm**2" % (triangle.name, triangle.s)

triangles = []
while True:
    data = input_triangle()
    if data is not None:
        triangles.append(Triangle(data))
    is_continue = raw_input("Do you want to add another triangle? ").lower()
    if is_continue != "y" and is_continue != "yes":
        break
print_triangles(triangles)


