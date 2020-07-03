class Transit:
    is_defensive = None
    contains_spearman = None

    def __init__(self, transit_dict):

        if "transitType" in transit_dict:
            self.transit_type = transit_dict["transitType"]

        if "unitDictionary" in transit_dict:
            self.unit_dictionary = transit_dict["unitDictionary"]
        else:
            self.unit_dictionary = None

        if "destinationHabitat" in transit_dict:
            self.destination_habitat_id = transit_dict["destinationHabitat"]

        self._calc_contains_spearman()
        self._calc_is_defensive()

    def _calc_is_defensive(self):
        if self.transit_type == "0":
            self.is_defensive = True
        else:
            self.is_defensive = False

    def _calc_contains_spearman(self):
        if self.unit_dictionary is None:
            return
        if "1" in self.unit_dictionary:
            self.contains_spearman = True
        else:
            self.contains_spearman = False