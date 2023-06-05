"""
or
"""
from car import Car, ElectricCar

from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

###

from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()