def describe_pet(animal_type, pet_name):
    '''Display information about a pet.'''
    print("\nI have a " + animal_type + ".")
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('hamster', 'harry')
describe_pet('dog', 'doggo')

describe_pet('harry', 'hamster')
#the order of the key is important
#but there's a way to not be mistaken

describe_pet(pet_name='harry',animal_type='hamster')