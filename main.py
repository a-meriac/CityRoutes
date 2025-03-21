import csv
import math

cities = []
latitudes = []
longitudes = []

def enter_city():
    city_input = input(f'\nEnter a city name:')
    if city_input in cities:
        return cities.index(city_input)
    else:
        print('City not found, please try again and ensure proper punctuation and capitalization')
        return enter_city()

def distance(lat1, lon1, lat2, lon2):
    return math.sqrt(math.pow(lat2 - lat1, 2) + math.pow(lon2 - lon1, 2))

class City:
  def __init__(self, name, latitude, longitude ):
    self.name = name
    self.latitude = latitude
    self.longitude = longitude

with open('worldcities.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)

    next(reader)

    for row in reader:
        cities.append(row[0])
        latitudes.append(row[2])
        longitudes.append(row[3])

def main():
    print('\nWelcome to City Route!')
    print('\nPlease enter 5 cities starting with your starting city\n')
    c1_index = enter_city()
    c1 = City(cities[c1_index], latitudes[c1_index], longitudes[c1_index])

    c2_index = enter_city()
    c2 = City(cities[c2_index], latitudes[c2_index], longitudes[c2_index])

    c3_index = enter_city()
    c3 = City(cities[c3_index], latitudes[c3_index], longitudes[c3_index])

    c4_index = enter_city()
    c4 = City(cities[c4_index], latitudes[c4_index], longitudes[c4_index])

    c5_index = enter_city()
    c5 = City(cities[c5_index], latitudes[c5_index], longitudes[c5_index])

    print(c1.name, c2.name, c3.name, c4.name, c5.name)
    print(c1.latitude, c2.latitude, c3.latitude, c4.latitude, c5.latitude)
    print(c1.longitude, c2.longitude, c3.longitude, c4.longitude, c5.longitude)



main()


