class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = str(self.year)+ ' '+self.make + ' ' + self.model
        return long_name


c = Car('audi', 'a4', 2016)
name = c.get_descriptive_name()
print(name)
