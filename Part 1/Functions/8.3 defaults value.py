def describe_pet(pet_name, animal_type = 'dog'):
    '''Display information about a pet.'''
    print("\nI have a " + animal_type + ".")
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet(pet_name= 'harry')
describe_pet('bob')

#if not a default value
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')