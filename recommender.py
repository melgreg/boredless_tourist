import traveler
import destination
import attraction


def add_attraction(location, new_attraction):
  try:
    d = destinations[location]
    new_attraction = attraction.Attraction(new_attraction[0], new_attraction[1])
    d.add_attraction(new_attraction)
  except KeyError:
    return

  
def find_attractions(location, interests):
  '''Find attractions that match interests.'''
  d = destinations[location]
  return d.find_attractions(interests)


def get_attractions_for_traveler(traveler):
  '''Recommend attractions for a traveler.'''
  traveler_destination, traveler_interests = traveler.location, traveler.interests
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = f'Hi {traveler.name}, we think you\'ll like these places around {traveler_destination}:\n' + ','.join([str(a) for a in traveler_attractions]) + '.'
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

  #for d in destinations.values():
  #  print(d)
  #test_traveler = traveler.Traveler('Erin Wilkes', 'Shanghai, China', ['historical site', 'art'])
  #print(test_traveler)
  #print(repr(test_traveler))

  #la_arts = find_attractions('Los Angeles, USA', ['art'])
  #print(la_arts)
  smills = traveler.Traveler('Derick Smill', 'Paris, France', ['monument'])
  smills_france = get_attractions_for_traveler(smills)
  print(smills_france)

