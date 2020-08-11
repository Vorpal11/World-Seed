class Location:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    # Returns a tuple containing the grid locations
    def get_location(self):
        return (self._x, self._y)

    # Returns a tuple containing the coord locations
    def get_coord_location(self):
        return (self._x * 16, self._y * 16)

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __add__(self, other):
        if isinstance(other, Location):
            self._x += other._x
            self._y += other._y
            return Location(self._x + other._x, self._y + other._y)
        else:
            if len(other) != 2: raise Exception('Error adding to Location')
            return Location(self._x + other[0], self._y + other[1])
