arm = {

    'first_name' : 'sakolkiat',
    'last_name' : 'noirak',
    'age' : 22,
    'city' : 'bangkok'

}

print(arm['first_name'].title() + " " + arm['last_name'].title())
print("age : " + str(arm['age']))
print('city : ' + arm['city'])

##

fav_num = {
    'arm' : 15,
    'kp' : 20,
    'kt' : 25
}

for person in fav_num:
    print(person.title() + "'s favorite number is " + str(fav_num[person]))

##Glossary

words = {

    'skk' : 'sakolkiat',
    'kp' : 'khawpun',
    'kt' : 'khawtoo',

}

for name in words:
    print(name.upper() + " is stand for " + str(words[name]).title())




