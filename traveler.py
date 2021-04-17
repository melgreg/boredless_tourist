"""A class to represent a traveler with a name, a current location and
specific interests."""

class Traveler:
    def __init__(self, name, location, interests):
        self.name = name
        self.location = location
        self.interests = interests


    def __str__(self):
        return f"Name: {self.name}\nLocation: {self.location}\nInterests: {self.interests}"

    def __repr__(self):
        return f"Traveler({self.name}, {self.location}, {self.interests})"
        
