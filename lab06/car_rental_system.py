from booking import Booking
from location import Location
from errors import BookingError, check_booking_error
from datetime import datetime

class CarRentalSystem():

    def __init__(self):
        self._cars      = []
        self._customers = []
        self._bookings  = []

    '''
    Query Processing Services
    '''
    def car_search(self, name=None, model=None):
        '''
        Task 1
        Return all cars if no search condition provided
	    Return same make/model if search criteria provided
        Return none if no cars found matching search criteria 
        '''
        srch_results = []
		
        if name is None and model is None:
             srch_results = self._cars
        else:
            if name is not None and model is not None:
                for car in self._cars:
                    if name.lower() == car.name.lower() or model.lower() == car.model.lower():
                       srch_results.append(car)            
            elif name is not None and model is None:
                for car in self._cars:
                    if name.lower() == car.name.lower():
                       srch_results.append(car)
            elif name is None and model is not None:
                for car in self._cars:
                    if model.lower() == car.model.lower():
                       srch_results.append(car)

        if len(srch_results) > 0:
             return srch_results
        else:
             return None

    def get_customer(self, licence):
        for customer in self._customers:
            if customer.licence is licence:
                return customer
        return None

    def get_car(self, rego):
        for car in self._cars:
            if car.rego is rego:
                return car
       
   
    #Booking Services
    def make_booking(self, customer, car, start_date,end_date,start_location,end_location):

        # Task 3.2 - error handling
        try:
            check_booking_error(start_date,end_date,start_location,end_location)
        except BookingError as err:
            print("Booking information error...")
            print(err.message)
        else: 
            # Input validated, calculate difference between start and end dates
            s_date = datetime(*[int(item) for item in start_date.split('-')])
            e_date = datetime(*[int(item) for item in end_date.split('-')])
            booking_period = (e_date - s_date).days + 1

            new_loc = Location(start_location, end_location)
             
            # create new book record
            new_booking = Booking(customer, car, booking_period, new_loc)
            self._bookings.append(new_booking)
            
            #car.add_booking(new_booking)
            return self._bookings
            
    
    def check_fee(self, customer, car, date1, date2, location1, location2):
        '''
        Task 4
        '''
        try:
            check_booking_error(date1,date2,location1,location2)
        except BookingError as err:
            print("Fee input error...")
            print(err.message)
        else:
            # Input validated, calculate difference between start and end dates
            s_date = datetime(*[int(item) for item in date1.split('-')])
            e_date = datetime(*[int(item) for item in date2.split('-')])
            booking_period = (e_date - s_date).days + 1
            
            print(car.calc_fee(booking_period))
    
    ''' 
        Registration Services
    '''
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


