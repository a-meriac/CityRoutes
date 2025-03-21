import csv

cities = []

def check_city(city):
    if city in cities:
        return True
    else:
        return False

class City:
  def __init__(self, name, latitude, longitude ):
    self.name = name
    self.age = age
    self.latitude = latitude
    self.longitude = longitude

with open('worldcities.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)

    next(reader)

    for row in reader:
        cities.append(row[0])

    print(cities)
