"""A destination represented as a city in a country with a set of attractions."""

class Destination:
    def __init__(self, location):
        self.city, self.country = location.split(', ')
        self.attractions = []

    def __str__(self):
        return f"{self.city}, {self.country}"

    def __repr__(self):
        return f"Destination('{self.city}, {self.country}')"

    def add_attraction(self, attraction):
        self.attractions.append(attraction)
