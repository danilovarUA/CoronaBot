from Operator import Time

class Report:
    is_defensive = None
    losses_enough_to_alert = None
    world_id = None
    published = None
    id = None

    def __init__(self, report_dict, world_id):
        self.report_dict = report_dict
        self.world_id = str(world_id)

        if "published" in report_dict:
            self.published = report_dict["published"] == "true"

        if "id" in report_dict:
            self.id = report_dict["id"]

        self._calc_is_defensive_()
        if self.is_defensive:
            self._calc_losses_enough_to_alert()

    def _calc_is_defensive_(self):
        correct_type = "type" in self.report_dict and self.report_dict["type"] == "8"
        not_offensive = "content" in self.report_dict and "ownOffenderUnitDictionary" not in self.report_dict["content"]
        self.is_defensive = correct_type and not_offensive

    def _calc_units_sum(self):
        # TODO: exclude any kind of transport units from here
        if "content" in self.report_dict and "unitDictionary" in self.report_dict["content"]:
            unit_dictionary = self.report_dict["content"]["unitDictionary"]
        else:
            unit_dictionary = {}
        left_sum = 0
        if "content" in self.report_dict and "lossDictionary" in self.report_dict["content"]:
            losses_dictionary = self.report_dict["content"]["lossDictionary"]
        else:
            losses_dictionary = {}
        losses_sum = 0

        for unit_kind in unit_dictionary:
            left_sum += int(unit_dictionary[unit_kind])
        for unit_kind in losses_dictionary:
            losses_sum += int(losses_dictionary[unit_kind])

        return left_sum, losses_sum

    def _calc_losses_enough_to_alert(self):
        left_sum, losses_sum = self._calc_units_sum()
        total_sum = losses_sum + left_sum
        if total_sum == 0:
            self.losses_enough_to_alert = False
        else:
            self.losses_enough_to_alert = (losses_sum / total_sum) > 0.21

    def _calc_destruction_percents(self):
        if self.report_dict["content"]["specialAbilityModifierDictionary"] == {}:
            return 0
        _, coefficient = self.report_dict["content"]["specialAbilityModifierDictionary"]["1"]["value"].split('.')
        coefficient = int(coefficient)
        if coefficient < 10:
            coefficient *= 10
        percentage = 100 - coefficient
        return percentage

    def __str__(self):  # I have to make custom function rather than str as far as this only works with defensive reports
        alive, dead = self._calc_units_sum()

        destruction_perc = self._calc_destruction_percents()

        try:
            player_name = self.report_dict["content"]["destinationHabitat"]["nick"]
        except KeyError:
            player_name = "no_player_name"

        try:
            habitat_name = self.report_dict["content"]["destinationHabitat"]["name"]
        except KeyError:
            habitat_name = "Free Habitat {}".format(self.report_dict["content"]["destinationHabitat"]["id"])

        try:
            habitat_type = self.report_dict["content"]["destinationHabitat"]["publicHabitatType"]
        except KeyError:
            habitat_type = "?"

        habitat_type_to_emoji = {"0": "🏡", "2": "🏰", "4": "🌃", "?": "?"}

        link = "l+k://report?{}&{}&{}".format(self.report_dict['id'],
                                              self.report_dict["habitat"],
                                              self.world_id)  # TODO: move creation of link for report in the function
        strings = [""] * 5
        strings[0] = "{}: 😇{}/💀{}/💣{}%".format(habitat_type_to_emoji[habitat_type], alive, dead, destruction_perc)
        strings[1] = str(Time.current_time(self.report_dict["date"]))
        strings[2] = "👤: {}".format(player_name)
        strings[3] = "📍: {}".format(habitat_name)
        strings[4] = "{}".format(link)
        return "\n".join(strings)

