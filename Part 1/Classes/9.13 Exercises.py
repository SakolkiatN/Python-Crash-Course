# Ice cream stand
class Restaurant_name():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.served = 0

    def describe(self):
        print("The name of this restaurant is " + self.name.title() + ", it's " + self.type.title() + ' cuisine.')

    def open_restaurant(self):
        print("The " + self.name.title() + " is now open!")

    def set_number_serve(self, set_serve):
        self.served = set_serve
        print("Set the number of customers served to " + str(self.served) )

    def increment_number(self, serve):
        self.served += serve
        print("The number of customers that have been served are " + str(self.served) )

SKK = Restaurant_name('skk', 'thai')
SKK.set_number_serve(100)
SKK.increment_number(50)


class IceCreamStand(Restaurant_name):
    def __init__(self,restaurant_name, cuisine_type='ice_cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available"""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())

big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe()
big_one.show_flavors()

