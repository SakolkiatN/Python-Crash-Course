#Restaurant
class Restaurant_name():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe(self):
        print("The name of this restaurant is " + self.name.title() + ", it's " + self.type.title() + ' cuisine.')

    def open_restaurant(self):
        print("The " + self.name.title() + " is now open!")

a = Restaurant_name('sakolkiat', 'thai')
a.describe()
a.open_restaurant()

#Three restaurant
intj = Restaurant_name('intj', 'thai')
enfp = Restaurant_name('enfp', 'german')
infj = Restaurant_name('infj', 'italian')

intj.describe()
enfp.describe()
infj.describe()

#Users
class User():
    def __init__(self, first_name, last_name, mbti, height):
        self.first = first_name
        self.last = last_name
        self.mbti = mbti
        self.height = height

    def describe_user(self):
        print(self.first.title() + ' ' + self.last.title() + "'s info:")
        print("- MBTI: " + self.mbti.upper())
        print("- Height: " + str(self.height) + " cm.")

    def greet_user(self):
        print("Hello, " + self.first.title() + ' ' + self.last.title() + ' !')

sakol = User('sakolkiat', 'noirak', 'intj', 185)
sakol.describe_user()
sakol.greet_user()



