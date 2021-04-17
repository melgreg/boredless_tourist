import traveler
import destination
import attraction

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index


def add_attraction(location, new_attraction):
  try:
    destination = destinations[location]
    new_attraction = attraction.Attraction(new_attraction[0], new_attraction[1])
    destination.add_attraction(new_attraction)
  except KeyError:
    return

  
def find_attractions(destination, interests):
  '''Find attractions that match interests.'''
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for possible_attraction in attractions_in_city:
    attraction_tags = possible_attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
        break
  return attractions_with_interest


def get_attractions_for_traveler(traveler):
  '''Recommend attractions for a traveler.'''
  traveler_destination, traveler_interests = traveler[1:]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = f'Hi {traveler[0]}, we think you\'ll like these places around {traveler_destination}: ' + ','.join(['the ' + attraction for attraction in traveler_attractions]) + '.'
  return interests_string



if __name__ == '__main__':
  destinations = [
  'Paris, France',
  'Shanghai, China',
  'Los Angeles, USA',
  'São Paulo, Brazil',
  'Cairo, Egypt',
  ]
  destinations = {d : destination.Destination(d) for d in destinations}
  #print(*destinations.items(), sep='\n')

  add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
  add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
  add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
  add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
  add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
  add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
  add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
  add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
  add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
  add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
  add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

  for d in destinations.values():
    print(d)
  #test_traveler = traveler.Traveler('Erin Wilkes', 'Shanghai, China', ['historical site', 'art'])
  #print(test_traveler)
  #print(repr(test_traveler))
  

  #test_destination_index = get_traveler_location(test_traveler)
  #print(test_destination_index)
  #print(attractions)
  #la_arts = find_attractions('Los Angeles, USA', ['art'])
  #print(la_arts)
  #smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
  #print(smills_france)

