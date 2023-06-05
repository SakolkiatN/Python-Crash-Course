favorite_language = {

    'jen' : 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'

}

for name in sorted(favorite_language.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentiond: ")
for language in favorite_language.values():
    print(language.title())

print('')

#set will wrap things up
for language in set(favorite_language.values()):
    print(language.title())
