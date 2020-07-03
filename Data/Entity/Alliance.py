class Alliance:
    name = None
    world_id = None
    id = None
    link = None
    diplomacy = None

    def __init__(self, alliance_dict, world_id):
        self.world_id = str(world_id)

        if "id" in alliance_dict:
            self.id = alliance_dict["id"]

        if "name" in alliance_dict:
            self.name = alliance_dict["name"]

        self.alliance_dict = alliance_dict

        self._calc_link()

    def _calc_link(self):
        self.link = "l+k://alliance?{}&{}".format(self.id, self.world_id)

    def __str__(self):
        return "Alliance({} {})".format(self.name, self.link)

    def __repr__(self):
        return str(self)
