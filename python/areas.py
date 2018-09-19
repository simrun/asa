import math

def circle(radius):
    return math.pi * radius**2

def sector(radius, angle):
    return angle / (2*math.pi) * circle(radius)

def segment(radius, angle):
    triangle = 0.5 * radius**2 * math.sin(angle)
    return sector(radius, angle) - triangle

def cylinder(radius, length):
    return circle(radius) * length

# Finds the area of a cylinder with radius 2 and length 2
print(cylinder(2, 2))