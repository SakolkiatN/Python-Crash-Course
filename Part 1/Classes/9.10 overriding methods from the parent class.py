#the __init__() method for a child class
class Car(): #<<< Parent class/superclass
    """a simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
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

    def increment_odometer(self, miles):
        '''Add the given amount to the odometer reading'''
        self.odometer_reading += miles
"""
 1
 1
vvv   this is inheritance
"""
class ElectricCar(Car): #<<< Child class [must include parent class in parenthesis]
    '''represent aspects of a car, specific to electric vehicles'''
    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class.
        then initialize attributes specific to an electric car.
        '''
        super().__init__(make, model, year)
##      ^^^^^ super() function helps python make connections between the parent and child class
        self.battery_size = 70

    def describe_battery(self):
        '''print a statement describing the battery size.'''
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        '''
        |
        |
        |
        V
        '''
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model', 2016)
print(my_tesla.get_descriptive())
my_tesla.describe_battery()



