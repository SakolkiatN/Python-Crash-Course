class Car():
    '''a simple attempt to represent a car.'''
    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #<<<<<<<initial value

    def get_descriptive(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        '''Print a statement showing the cat's mileage.'''
        print("This car has " + str(self.odometer_reading) + ' miles on it.' )
#Variables and Simple Data Types.modifying an attribute's value through a method
    def update_odometer(self, mileage):
        '''
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometerback
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive())

#1.modifying an attribute's value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#Variables and Simple Data Types.modifying an attribute's value through a method
my_new_car.update_odometer(24)
my_new_car.read_odometer()




