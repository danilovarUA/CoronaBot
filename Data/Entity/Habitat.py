class Habitat:
    name = None
    world_id = None
    id = None
    link = None
    regionId = None

    def __init__(self, habitat_dict, world_id):
        self.world_id = str(world_id)

        if "id" in habitat_dict:
            self.id = habitat_dict["id"]

        if "regionId" in habitat_dict:
            self.regionId = habitat_dict["regionId"]

        if "points" in habitat_dict:
            self.points = int(habitat_dict["points"])

        if 'points' in habitat_dict:
            if self.points in range(0, 1000):
                self.type = 'CAST'
            elif self.points in range(1000, 10000):
                self.type = 'FORT'
            elif self.points in range(10000, 100000):
                self.type = 'CITY'
            else:
                raise ValueError('unexpected amount of points')

        if "name" in habitat_dict:
            self.name = habitat_dict["name"]
        else:
            self.name = "Free Knight{}".format(self.id)

        if "player" in habitat_dict:
            self.player_id = habitat_dict["player"]
        else:
            self.player_id = "-1"

        if "mapX" in habitat_dict:
            self.x = habitat_dict["mapX"]
        else:
            self.x = None

        if "mapY" in habitat_dict:
            self.y = habitat_dict["mapY"]
        else:
            self.y = None

        self._calc_link(habitat_dict, world_id)

    def _calc_link(self, habitat_dict, world_id):
        self.link = "l+k://coordinates?{},{}&{}".format(habitat_dict['mapX'], habitat_dict['mapY'], world_id)
        pass  # link should be made with coordinates, not id

    def compare_coordinates(self, x_y):
        x, y = x_y
        return self.x and self.y and x == self.x and y == self.y

    def distance(self, another_habitat):
        x1 = int(self.x)
        x2 = int(another_habitat.x)
        y1 = int(self.y)
        y2 = int(another_habitat.y)
        if y1 & 1:
            X1 = x1 + 0.5
        else:
            X1 = x1
        Y1 = y1

        if y2 & 1:
            X2 = x2 + 0.5
        else:
            X2 = x2
        Y2 = y2

        dx = abs(X1 - X2)
        dy = abs(Y1 - Y2)

        if dy * 0.5 >= dx:
            distance = dy
        else:
            distance = dy * 0.5 + dx
        return int(distance)

    def __str__(self):
        type_to_emoji = {'CAST': "🏠", "FORT": "🏰", "CITY": "🏙"}
        type_emoji = type_to_emoji[self.type]
        return "Habitat({} {} [{}] {})".format(type_emoji, self.name, self.points, self.link)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.link == other.link
