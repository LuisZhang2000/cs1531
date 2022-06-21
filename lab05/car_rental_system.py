from booking import Booking

class CarRentalSystem():

    def __init__(self):
        self._cars      = []
        self._customers = []
        self._bookings  = []

    def make_booking(self, customer, car, period, location):
        # implement this function
        fee = int(period) * int(car.rate)
        if car.size is "Premium" or "Large":
            #fee = fee + (0.05 * fee)
            if int(period) > 7:
                fee = fee + (0.05 * fee)
                if car.size is "Premium":
                    fee = fee + (0.15 * int(car.rate))
		
        new_booking = Booking(period, fee, customer, car, location)
        self._bookings.append(new_booking)

    def get_customer(self, licence):
        for customer in self._customers:
            if customer.licence is licence:
                return customer
        return None

    def get_car(self, rego):
        for car in self._cars:
            if car.rego is rego:
                return car
        return None

    def add_car(self, car):
        self._cars.append(car)

    def add_customer(self, customer):
        self._customers.append(customer)


    '''
    Properties
    '''
    @property
    def cars(self):
        return self._cars

    @property
    def customers(self):
        return self._customers

    @property
    def bookings(self):
        return self._bookings
        
    def __str__(self):
        return f"=== Booking Successful! ===\nBooking details:"
        
