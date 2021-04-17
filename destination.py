"""A destination represented as a city in a country with a set of attractions."""

class Destination:
    def __init__(self, location):
        self.city, self.country = location.split(', ')
        self.attractions = []

    def __str__(self):
        return f"{self.city}, {self.country}\nAttractions:{self.attractions}"

    def __repr__(self):
        return f"Destination('{self.city}, {self.country}')"

    def add_attraction(self, attraction):
        """Add a new attraction to this destination."""
        self.attractions.append(attraction)

    def find_attractions(self, interests):
        """Create a list of attractions in this destination that match interests."""
        matches = []
        for a in self.attractions:
            for interest in interests:
                if a.is_match(interest):
                    matches.append(a)
                    break
        return matches

