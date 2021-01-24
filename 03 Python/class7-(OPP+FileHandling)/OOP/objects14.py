class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.__odometer_reading = 5


    def get_descriptive_name(self):
        #long_name = str(self.year)+ ' '+self.make + ' ' + self.model + ' '+ str(self.__odometer_reading)
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def update_odometer(self, val):
        self.__odometer_reading = val

    def get_odometer(self):
        return self.__odometer_reading

    def __start(self):
        print("Car started")

class ElectricCar(Car):
    '''ElectricCar'''
    def __init__(self,make,model,year):
        #super().__init__(make,model,year)
        self.make = make
        self.model = model
        self.year = year


c = Car('audi', 'a4', 2016)
ec = ElectricCar('Tesla', 's4', 2016)
print(ec.get_descriptive_name())
