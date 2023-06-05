from car import Car
from electirc_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive())