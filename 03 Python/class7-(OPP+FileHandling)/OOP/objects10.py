class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.__odometer_reading = 5


    def get_descriptive_name(self):
        long_name = str(self.year)+ ' '+self.make + ' ' + self.model + ' '+ str(self.__odometer_reading)
        return long_name

    def update_odometer(self, val):
        self.__odometer_reading = val

    def get_odometer(self):
        return self.__odometer_reading


c = Car('audi', 'a4', 2016)

print(c.get_odometer())
c.update_odometer(400000)
print(c.get_odometer())


