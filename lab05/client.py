from customer import Customer
from cars import Car
from location import Location
from car_rental_system import CarRentalSystem
from booking import Booking

# instantiate booking system
booking_system = CarRentalSystem()

# add customers
booking_system.add_customer(Customer("Matt", "1"))
booking_system.add_customer(Customer("Issac", "2"))
booking_system.add_customer(Customer("Taylor","3"))

# print all customers added to the booking system
print("\n~~~ Print all customers ~~~")
for customer in booking_system.customers:
  print(customer)
  
# test get_customer method - find a particular customer using his/her licence number
print("\n~~~ Test get_customer() method ~~~")
print(booking_system.get_customer("1"))

# add cars to the car rentla system
booking_system.add_car(Car("Small","Toyota","Corolla","1","150"))
booking_system.add_car(Car("Small","Mazda","Mazda 2","2","150"))
booking_system.add_car(Car("Small","Honda","Jazz","3","150"))
booking_system.add_car(Car("Small","Hyundai","i20","4","150"))
booking_system.add_car(Car("Medium","Toyota","Camry","5","180"))
booking_system.add_car(Car("Medium","Hyundai","Sonata","6","180"))
booking_system.add_car(Car("Medium","Honda","Accord","7","180"))
booking_system.add_car(Car("Medium","VW","Passat","8","180"))
booking_system.add_car(Car("Large","Toyota","Highlander","9","210"))
booking_system.add_car(Car("Large","Mazda","CX9","10","210"))
booking_system.add_car(Car("Large","Holden","Commodore","11","210"))
booking_system.add_car(Car("Large","Ford","Falcon","12","210"))
booking_system.add_car(Car("Premium","Tesla","Model X","13","250"))
booking_system.add_car(Car("Premium","BMW","750","14","250"))
booking_system.add_car(Car("Premium","Mercedes","E350","15","250"))
booking_system.add_car(Car("Premium","Porsche","Cayenne","16","250"))

#test all the cars added in the previous step
print("\n~~~ Print all cars ~~~")
for car in booking_system.cars:
  print(car)

# test get_car method (find a car using its rego number)
print("\n~~~ Test get_car() method ~~~")
print(booking_system.get_car("8"))  


# Booking tests
print("\n~~~ Make first booking ~~~")
new_loc = Location("Sydney","Canberra")
booking_system.make_booking(booking_system.get_customer("1"), booking_system.get_car("8"), 12, new_loc)
print(booking_system)
print(booking_system.bookings[0])

print("\n~~~ Make second booking ~~~")
new_loc = Location("Melbourne","Brisbane")
booking_system.make_booking(booking_system.get_customer("2"), booking_system.get_car("16"), 6, new_loc)
print(booking_system)
print(booking_system.bookings[1])

print("\n~~~ Make third booking ~~~")
new_loc = Location("Perth","Brisbane")
booking_system.make_booking(booking_system.get_customer("3"), booking_system.get_car("9"), 31, new_loc)
print(booking_system)
print(booking_system.bookings[2])

print("\n~~~ Print all bookings ~~~")
for booking in booking_system.bookings:
    print(booking)
