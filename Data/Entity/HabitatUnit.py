class HabitatUnit:
    in_defense = None
    # TODO: Translate battle type code to word
    def __init__(self, habitat_unit_dict):

        if "battleType" in habitat_unit_dict:
            self.battle_type = habitat_unit_dict["battleType"]

        if "unitId" in habitat_unit_dict:
            self.unit_type = habitat_unit_dict["unitId"]

        if "amount" in habitat_unit_dict:
            self.amount = habitat_unit_dict["amount"]

        if "sourceHabitat" in habitat_unit_dict:
            self.source_habitat_id = habitat_unit_dict["sourceHabitat"]

        if "habitat" in habitat_unit_dict:
            self.habitat_id = habitat_unit_dict["habitat"]

        self._calc_is_in_defense()

    def _calc_is_in_defense(self):
        self.in_defense = self.battle_type == "1"

    def __str__(self):
        return "{} of ({}) from {} in {} doing {}".format(self.amount,
                                                          self.unit_type,
                                                          self.source_habitat_id,
                                                          self.habitat_id,
                                                          self.battle_type)

    def __repr__(self):
        return str(self)