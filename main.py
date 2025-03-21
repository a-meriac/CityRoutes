import csv
import math
import itertools
import folium

cities = []
latitudes = []
longitudes = []

def enter_city():
    city_input = input(f'\nEnter a city name: ')
    if city_input in cities:
        return cities.index(city_input)
    else:
        print('City not found, please try again and ensure proper punctuation and capitalization')
        return enter_city()

def distance(city1, city2):
    lat1 = city1.latitude
    lon1 = city1.longitude
    lat2 = city2.latitude
    lon2 = city2.longitude

    lat1 = math.radians(float(lat1))
    lon1 = math.radians(float(lon1))
    lat2 = math.radians(float(lat2))
    lon2 = math.radians(float(lon2))

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    circumference = 6371.0
    return circumference * c


def make_distance_list(city_list):
    distance_list = [[0 for _ in range(6)] for _ in range(6)]

    for i in range(len(city_list)):
        for j in range(len(city_list)):
            distance_list[i][j] = distance(city_list[i], city_list[j])

    return distance_list



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
    print('Welcome to City Route!')
    print('\nPlease enter 5 cities:\n')
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

    start = City("Start", float(input("\nPlease enter the latitude of your starting point: ")), float(input("\nPlease enter the longitude of your starting point: ")))

    city_list = [start, c1, c2, c3, c4, c5]
    distance_list = make_distance_list(city_list)

    best_distance = 2 ** 999

    for perm in itertools.permutations([1,2,3,4,5]):
        total_distance = distance_list[0][perm[0]]

        for i in range(len(perm)-1):
            total_distance += distance_list[perm[i]][perm[i+1]]

        total_distance += distance_list[0][perm[4]]

        if total_distance < best_distance:
            best_distance = total_distance
            best_route = perm

    output = "Start -> "
    for x in best_route:
        output += city_list[x].name
        output += "-> "

    output += "Start"

    print(output)
    print(f"To follow this route you would have to travel {best_distance} kilometers.")

    #This end part is not my code, I took it from the folium documentation to visualise the route
    print("\nGenerating map...")

    # Create map centered at the start location
    route_map = folium.Map(location=[float(start.latitude), float(start.longitude)], zoom_start=3)

    # Build list of coordinates in the best route order
    route_coords = [[float(start.latitude), float(start.longitude)]]
    for x in best_route:
        route_coords.append([float(city_list[x].latitude), float(city_list[x].longitude)])
    route_coords.append([float(start.latitude), float(start.longitude)])  # Return to start

    # Add markers
    folium.Marker(location=[float(start.latitude), float(start.longitude)], popup='Start',
                  icon=folium.Icon(color='green')).add_to(route_map)
    for x in best_route:
        folium.Marker(
            location=[float(city_list[x].latitude), float(city_list[x].longitude)],
            popup=city_list[x].name
        ).add_to(route_map)

    # Draw the route line
    folium.PolyLine(route_coords, color="blue", weight=2.5, opacity=1).add_to(route_map)

    # Save the map
    route_map.save("best_route_map.html")
    print("Map saved as 'best_route_map.html'! Open it in your browser to view the route.")


main()