#Functions-12 Sandwiches

def make_sandwiches(*sandwiches):
    print("Summary of  the order:")
    for sandwich in sandwiches:
        print("- " + sandwich)

make_sandwiches('1', 'Variables and Simple Data Types', 'Introducing Lists')
make_sandwiches('Working with Lists', 'if Statements', 'Dictionaries', 'User Input and while Loops')

#Functions-13 user profile
def build_profile(first, last, **user_info):
    '''Build a dictionary containing everything we know about a user.'''
    # double asterisks before the parameter cause python to create an empty dictionary
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile

skk = build_profile('sakolkiat','noirak', age = '22', height = '185 cm', weight = '90 kg')
print(skk)

#Functions-14 Cars
def car_info(manufac,model_name,**car_info):
    car = {}
    car['manufacturer'] = manufac
    car['model_name'] = model_name
    for key,value in car_info.items():
        car[key] = value
    return car

car = car_info('subaru', 'outback', color = 'blue', tow_package = True)
print(car)