favorite_language = {
    'jen' : 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'

}

for name in favorite_language.keys():
    print(name.title())

    #or

for name in favorite_language:
    print(name.title())

print("")

friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              str(favorite_language[name]).title() + "!")

if 'erin' not in favorite_language.keys():
    print("Erin, please take our poll!")