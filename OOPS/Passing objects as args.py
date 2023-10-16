# Passing objects as arguments

class Car:
    color = None


class Bike:
    color = None


def change_color(vehicle, color):
    vehicle.color = color


c1 = Car()
c2 = Car()

change_color(c1, 'White')
change_color(c2, 'Red')

print(c1.color)
print(c2.color)

b1 = Bike()
b2 = Bike()

change_color(b1, 'Orange')
change_color(color='Purple', vehicle=b2)
print(b1.color)
print(b2.color)
