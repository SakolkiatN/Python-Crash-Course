def make_shirt(size, text):
    print('Your shirt size is ' + size.upper() + ', and the message on it is "' + text + '".' )

make_shirt('m', 'lmao')
make_shirt(size= 'm', text= 'hehe')

#large
def make_shirt(text, size = 'large'):
    print('Your shirt size is ' + size.upper() + ', and the message on it is "' + text + '".' )

make_shirt('lmao')
make_shirt('i love python')
make_shirt('hey yo', 'medium')
make_shirt(size='m',text='sadad')

def describe_city(city, country = 'thailand'):
    print(city.title() + " is in " + country.title())

describe_city('bangkok')
describe_city('chanthaburi')
describe_city('nonthaburi')
