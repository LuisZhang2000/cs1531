from datetime import datetime

class BookingError(Exception):
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return self.message
    
def check_booking_error(start_date, end_date, start_location, end_location):
        
        if start_location == "":
            raise BookingError("Specify a valid pick-up location")
        
        if end_location == "":
            raise BookingError("Specify a valid drop-off location")
            
        try:
            datetime.strptime(start_date, '%Y-%m-%d')
        except ValueError:
            raise BookingError("Specify a valid start date, format should be YYYY-MM-DD")
       
        try:
            datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            raise BookingError("Specify a valid end date, format should be YYYY-MM-DD")
        
        if (datetime(*[int(item) for item in end_date.split('-')]) - datetime(*[int(item) for item in start_date.split('-')])).days + 1 < 1:
            raise BookingError("Specify a valid booking period")


    
