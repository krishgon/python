def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

def add_attraction(destination,attraction):
  try:
    destination_index = get_destination_index(destination)
  except ValueError:
    return destination
  attractions_for_destinations = attractions[destination_index]
  attractions_for_destinations.append(attraction)
  return attractions_for_destinations
  
def find_attractions(destination,interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    attraction_tags = attraction[1]
    possible_attraction = attraction
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])   
  return attractions_with_interest

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
attractions = [[] for i in range(5)]
#print(attractions)

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
#print(get_destination_index("Hyderabad, India"))
test_destination_index = get_traveler_location(test_traveler)

#print(test_destination_index)

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA",['Venice Beach', ['beach']])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#print(attractions)
la_arts = find_attractions("Los Angeles, USA",['art'])
print(la_arts)