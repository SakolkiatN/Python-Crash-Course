"""a set of clases that can be used to represent electric cars."""

from car import Car

class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approxiamtely " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 85:
            print("This car has a 85-kWh battery.")
        else:
            self.battery_size = 85
            print("This car has successfully upgraded to 85-kWh battery.")



class ElectricCar(Car): #<<< Child class [must include parent class in parenthesis]
    '''represent aspects of a car, specific to electric vehicles'''
    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class.
        then initialize attributes specific to an electric car.
        '''
        super().__init__(make, model, year)
##      ^^^^^ super() function helps python make connections between the parent and child class
        self.battery = Battery()








