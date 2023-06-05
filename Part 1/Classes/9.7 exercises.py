#Number served
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

#Login attempt
class User():
    def __init__(self, first_name, last_name, mbti, height):
        self.first = first_name
        self.last = last_name
        self.mbti = mbti
        self.height = height
        self.attempt = 0

    def describe_user(self):
        print(self.first.title() + ' ' + self.last.title() + "'s info:")
        print("- MBTI: " + self.mbti.upper())
        print("- Height: " + str(self.height) + " cm.")

    def greet_user(self):
        print("Hello, " + self.first.title() + ' ' + self.last.title() + ' !')

    def increment_login_attempts(self):
        self.attempt += 1
        print("Login attemps: " + str(self.attempt))

    def reset_login_attempts(self):
        self.attempt = 0
        print("Reset login attempts to 0")




sakol = User('sakolkiat', 'noirak', 'intj', 185)
sakol.describe_user()
sakol.greet_user()
sakol.increment_login_attempts()
sakol.increment_login_attempts()
sakol.increment_login_attempts()
sakol.reset_login_attempts()






