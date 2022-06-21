from car import SmallCar, MediumCar, LargeCar, PremiumCar
from car_rental_system import CarRentalSystem
from customer import Customer
from location import Location

system = CarRentalSystem()

class IdGenerator():

    def __init__(self):
        self._id = 0

    def next(self):
        self._id += 1
        return self._id

rego_generator = IdGenerator()
licence_generator = IdGenerator()

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


print('~~~ Print all customers ~~~')
print('\n'.join(str(c) for c in system.customers))

print('\n~~~ Print all cars ~~~')
print('\n'.join(str(c) for c in system.cars))

# Car Search Start
print('\n~~~ Print Search Results ~~~')
name = "Mazda"
srch_results = system.car_search(name)
for x in srch_results:
   print (x)

print('\n~~~ Print Search Results ~~~')
name = "Alpha"
model = "Romeo"
srch_results = system.car_search(name, model)
if srch_results is None:
   print ("No cars found")
# Car Search End


print('\n\n~~~ Make first booking ~~~')
user = system.get_customer(3)
car  = system.get_car(5)

year1 = 2018
month1 = 12
day1 = 1

year2 = 2018
month2 = 12
day2 = 5

start_date      = f'{year1}-{month1}-{day1}'
end_date        = f'{year2}-{month2}-{day2}'

booking = system.make_booking(user, car, start_date, end_date,'Sydney', 'Canberra')

print('\n\n~~~ Make second booking ~~~')
user = system.get_customer(2)
car  = system.get_car(21)

system.make_booking(user, car, start_date, end_date, 'Earth', 'Moon')

print('\n\n~~~ Make third booking ~~~')
user = system.get_customer(1)
car  = system.get_car(5)

start_date      = '2019-02-15'
end_date        = '2019-02-25'

system.make_booking(user, car, start_date, end_date, 'Melbourne', 'Brisbane')


print('\n\n~~~ Make fourth booking ~~~')
user = system.get_customer(1)
car  = system.get_car(5)

start_date      = '2019-03-15'
end_date        = '2019-03-25'

booking = system.make_booking(user, car, start_date, end_date, 'Melbourne', 'Brisbane')
print("=========================")
print(booking[0].fee)
print("=========================")

print('\n\n~~~ Make an error booking ~~~')
user = system.get_customer(3)
car  = system.get_car(16)

start_date      = ''
end_date        = '2019-02-25'

system.make_booking(user, car, start_date, end_date, 'Perth', 'Darwin')

print('\n\n~~~ CCheck Fee for Car ~~~\n')
user = system.get_customer(18)
car  = system.get_car(16)

start_date      = '2019-02-05'
end_date        = '2019-02-25'

system.check_fee(user, car, start_date, end_date, 'Perth', 'Darwin')



print('\n\n~~~ Print all bookings ~~~\n')
print('\n\n'.join(str(b) for b in system.bookings))

# Get all details and associated bookings for car
print('\n~~~ Print All Booking for a Specific Car~~~')
for car_booking in system.get_car(5).bookings:
    print(car_booking)
    
for car_booking in system.get_car(21).bookings:
    print(car_booking)



