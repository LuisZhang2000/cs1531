from car import Car
from customer import Customer
from location import Location

class Booking:
    def __init__(self, duration, fee, customer, car, location):
        self._duration = duration
        self._fee = fee
        self.customer = customer
        self.car = car
        self.location = location
        
    @property
    def duration(self):
        return self._duration
        
    @property
    def fee(self):
        return self._fee
        
    def __str__(self):
        return f"Made by {self.customer}\n{self.car} for {self._duration} days\n{self.location}\nTotal fee: ${self._fee}"
    

