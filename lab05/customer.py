class Customer:
    def __init__(self, name, licence):
        self._name = name
        self._licence = licence
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, full_name):
        self._name = full_name
        
    @property
    def licence(self):
        return self._licence
        
    @licence.setter
    def licence(self, licence_no):
        self._licence = licence_no
        
    def __str__(self):
        return f"Customer <name: {self.name}, licence: {self.licence}>"
    

