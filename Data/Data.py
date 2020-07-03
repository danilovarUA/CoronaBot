from .Entity.Player import Player
from .Entity.Alliance import Alliance
from .Entity.Habitat import Habitat
from .Entity.HabitatUnit import HabitatUnit
from .Entity.Report import Report
from .Entity.Transit import Transit
from Module.Logger import Logger

RELATIONSHIP_NUM_TO_WORD = {"-1": "red", "1": "blue", "2": "green", "3": "orange"}


class Data:
    world_id = None

    def __init__(self, gen_dict, headers_info, request):
        self.logger = Logger("Data")
        self.data = {"player": {},
                     "alliance": {},
                     "habitat": {},
                     "habitat_unit": [],
                     "report": {},
                     "transit": [],
                     "diplomacy": {"red": [], "green": [], "blue": [], "orange": []}}
        self.own_ids = {'player': headers_info["playerID"],
                        'alliance': None}
        self._calc_server_id(gen_dict)
        self.parse_dict(gen_dict)
        self._find_own()
        self.request = request

    def parse_dict(self, dict_to_parse):
        # Player from Rating
        try:
            for item in dict_to_parse["playerRanks"]:
                new_object = Player(item, world_id=self.world_id)
                self.data["player"][new_object.id] = new_object
        except KeyError:
            pass

        # Player
        try:
            for item in dict_to_parse["Data"]["Player"]:
                new_object = Player(item, world_id=self.world_id)
                self.data["player"][new_object.id] = new_object
        except KeyError:
            pass

        # Alliance
        try:
            for item in dict_to_parse["Data"]["Alliance"]:
                new_object = Alliance(item, world_id=self.world_id)
                self.data["alliance"][new_object.id] = new_object
        except KeyError:
            pass

        # Habitat
        try:
            for item in dict_to_parse["Data"]["Habitat"]:
                new_object = Habitat(item, world_id=self.world_id)
                self.data["habitat"][new_object.id] = new_object
        except KeyError:
            pass

        # Diplomacy
        try:
            for diplomacy_item in dict_to_parse["Data"]["Diplomacy"]:
                _, target_alliance_id = diplomacy_item['id'].split('-')
                relationship_kind = RELATIONSHIP_NUM_TO_WORD[diplomacy_item["relationship"]]
                self.data["diplomacy"][relationship_kind].append(target_alliance_id)
        except KeyError:
            pass

        # HabitatUnit
        try:
            if "HabitatUnit" in dict_to_parse["Data"]:
                self.data["habitat_unit"] = []
            for item in dict_to_parse["Data"]["HabitatUnit"]:
                new_object = HabitatUnit(item)
                self.data["habitat_unit"].append(new_object)
        except KeyError:
            pass

        # Transit
        try:
            if "Transit" in dict_to_parse["Data"]:
                self.data["transit"] = []
            for item in dict_to_parse["Data"]["Transit"]:
                new_object = Transit(item)
                self.data["transit"].append(new_object)
        except KeyError:
            pass

    def load_and_parse_reports(self):
        request_result = self.request.fetch_reports()
        try:
            for item in request_result[1]["Data"]["Report"]:
                new_object = Report(item, world_id=self.world_id)
                self.data["report"][new_object.id] = new_object
        except KeyError:
            return True, []

    def _find_own(self):
        own_player_instance = self.get_instances_by_ids("player", [self.own_ids["player"]])[0]
        own_alliance_id = own_player_instance.alliance_id
        if own_alliance_id:
            self.own_ids['alliance'] = self.get_instances_by_ids("alliance", [own_alliance_id])[0]

    def _calc_server_id(self, gen_dict):
        string = gen_dict["serverVersion"]
        _, _, server_ids = string.split("_")
        world_id, _, _ = server_ids.split("-")
        self.world_id = world_id

    def get_instances_by_ids(self, instance_type, ids, force_request=False):

        def get_instance_by_id():
            if not force_request:
                try:
                    return self.data[instance_type][item_id]
                except ValueError:
                    pass
                except KeyError:
                    pass

            type_to_request = {
                "alliance": self.request.alliance_info,
                "player": self.request.player_info,
                "habitat": self.request.habitat_info,
            }

            type_to_request[instance_type](item_id)
            return self.data[instance_type][item_id]

        items = []
        index = 0
        for item_id in ids:
            index += 1
            self.logger.log("Getting instance {} out of {}".format(index, len(ids)))
            items.append(get_instance_by_id())
        return items

    def get_players_by_alliances(self, alliances, force_request=True):
        alliance_ids = [alliance.id for alliance in alliances]

        # only to make sure all players of these alliances are in data
        self.get_instances_by_ids("alliance", alliance_ids, force_request=force_request)

        players_list = []
        for player_id in self.data["player"]:
            player = self.data["player"][player_id]
            if player.alliance_id in alliance_ids:
                players_list.append(player)
        return players_list

    def get_habitats_by_players(self, players, force_request=True):
        # only to make sure all habitats of these players are in data
        player_ids = [player.id for player in players]
        if force_request:
            self.get_instances_by_ids("player", player_ids, force_request=force_request)
        habitats_list = []
        for habitat_id in self.data["habitat"]:
            habitat = self.data["habitat"][habitat_id]
            try:
                if habitat.player_id in player_ids:
                    habitats_list.append(habitat)
            except AttributeError:
                pass
        return habitats_list

    def get_habitat_by_coordinates(self, x, y):
        for habitat_id in self.data["habitat"]:
            habitat = self.data["habitat"][habitat_id]
            if habitat.compare_coordinates((x, y)):
                return habitat
        self.request.map(x, y, width="15", height="15")
        return self.get_habitat_by_coordinates(x, y)

    def get_instance_by_link(self, link):
        if 'alliance' in link:
            item_id = link.split("l+k://alliance?")[1].split("&")[0]
            return self.get_instances_by_ids("alliance", [item_id])[0]
        if 'player' in link:
            item_id = link.split("l+k://player?")[1].split("&")[0]
            return self.get_instances_by_ids("player", [item_id])[0]
        if 'coordinates' in link:
            x, y = link.split("l+k://coordinates?")[1].split("&")[0].split(",")
            return self.get_habitat_by_coordinates(x, y)

    def get_instances_by_links(self, links):
        instances = []
        for link in links:
            instances.append(self.get_instance_by_link(link))
        return instances
