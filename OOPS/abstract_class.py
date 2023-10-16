# Abstract class


from abc import ABC, abstractmethod


class Vehicle(ABC):
	@abstractmethod
	def start(self):
		pass

	@abstractmethod
	def stop(self):
		pass


class Bike(Vehicle):  # concrete class
	color = None
	def start(self):
		print('You are riding a bike...')

	def stop(self):	#all methods inside the abstract class must be used inside concrete class
		pass



class Car(Vehicle):	#concrete class
    
    color=None
    def start(self):
        print('You are driving a car...')

    def stop():
     	pass


# # creating instances
# # v1 = Vehicle()
# b1 = Bike()
# c1 = Car()

# b1.start()
# c1.start()


# passing objects as args

def set_color(car,color):
	car.color = color

c1 = Car()
b1 = Bike()

set_color(c1,'White')
set_color(b1,'Black')

print(c1.color)
print(b1.color)
