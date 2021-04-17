"""A tourist attraction with a name and a set of interests that it matches."""

class Attraction:
    def __init__(self, name, interests):
        self.name = name
        self.interests = set(interest.lower() for interest in interests)

    def __str__(self):
        return f"The {self.name}"

    def __repr__(self):
        return f"Attraction({self.name}, {list(self.interests)})"
