people = {
    'arm' : {
        'firstname' : 'sakolkiat',
        'lastname' : 'noirak',
        'age' : '22',
        'city' : 'nonthaburi',
    },
    'khawpun' : {
        'firstname' : 'krittayos',
        'lastname' : 'poomthong',
        'age' : '22',
        'city' : 'chanthaburi',
    },


}

for person, data in people.items():
    print(person.title() + "'s detail")
    full_name = data['firstname'] + " " + data['lastname']
    age = data['age']
    city = data['city']
    print("Full name: " + full_name.title())
    print("Age: " + age)
    print("City: " + city.title())

for person,data in people.items():
    print(person.title() + "'s")
    print("Fullname: " + data['firstname'].title() + " " + data['lastname'].title())
    print("Age: " + data['age'])
    print("City: " + data['city'])

print('\n\n\n')

pets = {
    'abyssinian' : {
        'origin' : 'egypt',
        'charact' : 'regal appearance; lithe body with long slender legs',
        'owner' : 'arm',
    },
    'american shorthair' : {
        'origin' : 'united states',
        'charact' : 'broad muscular body; thick dense fur',
        'owner' : 'mar'
    }
}

for pet, info in pets.items():
    print(pet.title())
    print(info['origin'].title())
    print(info['charact'])
    print(info['owner'].title())

###
#fav places

fav_places = {
    'arm' : ['italy', 'france', 'thailand'],
    'kp' : ['germany', 'english', 'russia'],
    'warm' : ['nowhere']
    }

for name, places in fav_places.items():
    if len(places) > 1:
        print(name.title() + "'s favorite places are: ")
    else:
        print(name.title() + "'s favorite place is:")
    for place in places:
        print("\t" + place.title())

###

#fav nums
fav_num = {
    'arm' : [15,16,17,18],
    'kp' : [20,21,29],
    'kt' : [25,30],
    'warm' : [3.14]
}

for person, nums in fav_num.items():
    if len(nums) > 1:
        print(person.title() + "'s favorite numbers are " + str(nums))
    else:
        print(person.title() + "'s favorite number is " + str(nums))

#cities

cities = {
    'bangkok' : {
        'country' : 'thailand',
        'population' : '11 millions',
        'fact' : 'Thailand was actually known as Siam until 1939 (and again from 1945 to 1949).',
    },
    'new york' : {
        'country' : 'usa',
        'population' : 'Functions.47 millions',
        'fact' : 'More than 800 languages are spoken in New York City, \n\t\t  making it the most linguistically diverse city in the world. Working with Lists in 10 households speak a language other than English.'

    }
}

for city, info in cities.items():
    print("The info about " + city.title() + " are :")
    if len(str(info['country'])) < 4:
        print('\t' + city.title() + " is in " + info['country'].upper() + ".")
    else:
        print('\t' + city.title() + ' is in ' + info['country'].title() + ".")
    print('\tPopulation: ' + info['population'] + '.')
    print('\tfact: ' + info['fact'])
