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
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(float(lat1))
    lon1 = math.radians(float(lon1))
    lat2 = math.radians(float(lat2))
    lon2 = math.radians(float(lon2))

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Earth's radius in kilometers (mean radius)
    circumference = 6371.0
    return circumference * c

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
    print("""

   ___ _ _             __             _       
  / __(_) |_ _   _    /__\ ___  _   _| |_ ___ 
 / /  | | __| | | |  / \/// _ \| | | | __/ _ \\
/ /___| | |_| |_| | / _  \ (_) | |_| | ||  __/
\____/|_|\__|\__, | \/ \_/\___/ \__,_|\__\___|
             |___/                            

""")
    print('Welcome to City Route!')
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

    for x in range(5):






main()


