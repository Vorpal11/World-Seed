class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Returns a tuple containing the grid locations
    def get_location(self):
        return (self.x, self.y)

    # Returns a tuple containing the coord locations
    def get_coord_location(self):
        return (self.x * 16, self.y * 16)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Location):
            self.x += other.x
            self.y += other.y
        else:
            if len(other) != 2: raise Exception('Error adding to Location')
            self.x += other[0]
            self.y += other[1]
        return self
