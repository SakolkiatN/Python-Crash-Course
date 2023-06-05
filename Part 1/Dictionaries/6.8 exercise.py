# words = {
#
#     'BDFL' : 'benevolent Dictator For Life',
#     'EAFP' : 'easier to ask for forgiveness than permission',
#     'GIL' : 'global interpreter lock.',
#
# }
#
# for name in words.keys():
#     print(name.upper())
#
# for name1 in words.values():
#     print(name1.upper())
#
# for name, name1 in words.items():
#     print(name + ' is stand for '+ name1)
#
# print('')
# #Rivers
#
# rivers = {
#
#     'niger' : 'nigeria',
#     'nile' : 'egypt',
#     'lena' : 'russia',
#     'missouri' : 'united states'
#
# }
#
# for key, value in rivers.items():
#     print("The " + key.title() + " run through " + value.title())
#
# for key in rivers.keys():
#     print("The " + key.title())
#
# for value in rivers.values():
#     print("The " + value.title())

#Polling
favorite_language = {

    'jen' : 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'

}

should_poll = ['jack', 'john', 'judy', 'edward', 'phil']

for people in should_poll:
    if people in favorite_language.keys():
        print("Hey " + people.title() + ", thank you for your response.")
    else:
        print("Hey " + people.title() + ", you should take the poll.")






