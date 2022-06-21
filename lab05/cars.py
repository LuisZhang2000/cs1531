from car import Car

class Car(Car):
    def __init__(self, size, make, model, rego, rate):
        super().__init__(size)
        self._model = model
        self._make = make
        self._rego = rego
        self._rate = rate     

    @property
    def model(self):
        return self._model
        
    @property 
    def make(self):
        return self._make
        
    @property
    def rego(self):
        return self._rego 
        
    @property
    def rate(self):
        return self._rate

    def __str__(self):
        return f"{self._size} Car <{self._make}, {self._model}, rego: {self._rego}>"


        
        

