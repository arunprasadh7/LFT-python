# Abstract class

from abc import ABC, abstractmethod

class Vehicle(ABC):
	@abstractmethod
	def start(self):
		pass	

	@abstractmethod
	def stop(self):
		pass


class Bike(Vehicle): #concrete class
    def start(self):
        print('You are riding a bike...')

    def stop(self):
    	pass


class Car(Vehicle):
    def start(self):
        print('You are driving a car...')

    def stop():
     	pass


# creating instances
# v1 = Vehicle()
b1 = Bike()
c1 = Car()

b1.start()
c1.start()