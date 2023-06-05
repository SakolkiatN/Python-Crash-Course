#city names

def city_country(city, country):
    city_name = '"' + city.title() + ", " + country.title() + '"'
    print(city_name)

city_country('santiago', 'chile')
city_country('bangkok', 'thailand')
city_country('new york', 'united states of america')

#album

def make_album(artist, album_tile):
    album_info = {'artist': artist.title(),'album_title' : album_tile.title()}
    return album_info

album = make_album('joji', 'nectar')
print(album)
print(make_album('the weeknd', 'after hours'))

while True:
    print('(enter "q" to stop)')
    artis = input('Artist:')
    if artis == 'q':
        break
    albm = input('Album: ')
    if albm == 'q':
        break
    album = make_album(artis,albm)
    print(album)







