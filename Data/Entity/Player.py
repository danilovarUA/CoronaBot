class Player:
    name = None
    world_id = None
    id = None
    link = None
    alliance_id = None

    def __init__(self, player_dict, world_id):
        self.world_id = str(world_id)
        if 'isOnVacation' in player_dict:
            self.vacation = player_dict['isOnVacation'] == 'true'
        else:
            self.vacation = False

        if "id" in player_dict:
            self.id = player_dict["id"]

        if "nick" in player_dict:
            self.name = player_dict["nick"]

        if "points" in player_dict:
            self.points = player_dict["points"]
        else:
            if "quantifier" in player_dict:
                self.points = player_dict["quantifier"].split(".")[0]

        if "alliance" in player_dict:
            self.alliance_id = player_dict["alliance"]
        else:
            self.alliance_id = None

        if "rank" in player_dict:
            self.rank = player_dict["rank"]

        self._calc_link()

    def _calc_link(self):
        self.link = "l+k://player?{}&{}".format(self.id, self.world_id)

    def __str__(self):
        return "Player({}[{}] {})".format(self.name, self.points, self.link)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.link == other.link
