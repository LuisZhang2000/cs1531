from location import Location
from datetime import datetime
from errors import BookingError
from car import SmallCar, MediumCar, LargeCar, PremiumCar
from customer import Customer
from car_rental_system import CarRentalSystem

import pytest

class IdGenerator():

    def __init__(self):
        self._id = 0

    def next(self):
        self._id += 1
        return self._id

rego_generator = IdGenerator()
licence_generator = IdGenerator()

@pytest.fixture
def rental_fixture():
    system = CarRentalSystem()
    for name in ["Mazda", "Holden", "Ford"]:
        for model in ["Falcon", "Commodore"]:
            system.add_car(SmallCar(name, model, rego_generator.next()))
            system.add_car(MediumCar(name, model, rego_generator.next()))
            system.add_car(LargeCar(name, model, rego_generator.next()))

    for name in ["Tesla", "Audi"]:
        for model in ["model x", "A4", "S class"]:
            system.add_car(PremiumCar(name, model, rego_generator.next()))

    for name in ["Matt", "Isaac", "Taylor"]:
        system.add_customer(Customer(name, licence_generator.next()))
    
    return system


def test_success_search_cars_by_name_mazda(rental_fixture):
    print("test_success_search_cars_by_name_mazda")
   
    name = 'Mazda'
    cars = rental_fixture.car_search(name)
    assert len(cars) == 6

def test_success_search_cars_by_model_falcon(rental_fixture):
    print("test_success_search_cars_by_model_falcon")
   
    model = 'Falcon'
    cars = rental_fixture.car_search(None,model)
    assert len(cars) == 9
    
def test_success_search_all_cars(rental_fixture):
    print("test_success_search_all_cars")
   
    cars = rental_fixture.car_search()
    assert len(cars) == 24

def test_success_no_cars_found(rental_fixture):
    print("test_success_no_cars_found")
   
    name = "Alpha"
    model = "Romeo"
    cars = rental_fixture.car_search(name, model)
    assert cars is None
