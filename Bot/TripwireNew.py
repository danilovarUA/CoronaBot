from Request import Request
from Module.Logger import Logger
from Module import Telegram
import time

EMAIL = "Goodenough@acc.com"
PASSWORD = "123"
COUNTER_HOURS = 6
MINUTES_BETWEEN_CHECK = 3
REPORTS_IN_MESSAGE = 5
DISCUSSSION_ID = "11453"
SOURCE_HABITAT_LINK = "l+k://coordinates?16546,16440&230"
TRIPWIRE_SIZE = 5

logger = Logger("TripwireNew")
request = Request(EMAIL, PASSWORD)
data = request.enter()[1]
telegram = Telegram.Telegram()
ALLIANCES_LINKS = ["l+k://alliance?408&230"]
ADDITIONAL_PLAYER_LINKS = []  # Inactive
EXCLUDED_PLAYERS_LINKS = []  # Inactive


def clean_changes_dict(changes_dict):
    temp_dict = {}
    for hab_id in changes_dict:
        amount = changes_dict[hab_id]
        if amount == 0:
            continue
        temp_dict[hab_id] = amount
    return temp_dict


def calculate_changes():
    alliances = []
    for link in ALLIANCES_LINKS:
        alliances.append(data.get_instance_by_link(link))
    logger.log("{} Alliances loaded".format(len(alliances)))
    players = data.get_players_by_alliances(alliances)
    logger.log("{} Players loaded".format(len(players)))
    habitats = data.get_habitats_by_players(players)
    logger.log("{} Habitats loaded".format(len(habitats)))
    habitats = [habitat for habitat in habitats if habitat.player_id != data.own_ids["player"]]
    logger.log("{} Habitats left after filtering own".format(len(habitats)))

    change_troops_dict = {}
    for habitat in habitats:
        change_troops_dict[habitat.id] = TRIPWIRE_SIZE

    for habitat_unit in data.data["habitat_unit"]:
        if habitat_unit.battle_type != "1":
            continue
        if habitat_unit.habitat_id in change_troops_dict:
            change_troops_dict[habitat_unit.habitat_id] -= int(habitat_unit.amount)

    for transit in data.data["transit"]:
        if (transit.transit_type == "0"
                and "1" in transit.unit_dictionary
                and transit.destination_habitat_id in change_troops_dict):
            change_troops_dict[transit.destination_habitat_id] -= int(transit.unit_dictionary["1"])
    change_troops_dict = clean_changes_dict(change_troops_dict)
    logger.log("{} changes".format(len(change_troops_dict)))
    return change_troops_dict


def apply_changes(changes_dictionary):
    global data
    source_habitat = data.get_instance_by_link(SOURCE_HABITAT_LINK)
    index = 0
    for habitat_index in changes_dictionary:
        time.sleep(3)
        index += 1
        amount = changes_dictionary[habitat_index]
        if amount > 0:
            unit_dictionary_text = "{1=" + str(amount) + ";}"
            success, data = request.send_support(habitat_index, unit_dictionary_text, source_habitat.id)
            if success:
                logger.log("{}/{} - {} troops sent to {}".format(index, len(changes_dictionary), amount, habitat_index))
        else:  # amount < 0
            unit_dictionary_text = "{1=" + str((-amount)) + ";}"
            success, data = request.recall_support(habitat_index, unit_dictionary_text, source_habitat.id)
            if success:
                logger.log("{}/{} - {} troops recalled from {}".format(index, len(changes_dictionary), amount, habitat_index))


def restock_tripwires():
    changes_dictionary = calculate_changes()
    apply_changes(changes_dictionary)


def get_reports():
    useful = []
    useless = []
    data.load_and_parse_reports()
    for report_id in data.data["report"]:
        report = data.data["report"][report_id]
        if report.is_defensive:
            if report.losses_enough_to_alert:
                useful.append(report)
            else:
                useless.append(report)
    logger.log("Useful: {}, Useless: {}".format(len(useful), len(useless)))
    return useful, useless


def remove_reports(reports):
    for report in reports:
        success, data = request.delete_report(report)
        if success:
            logger.log("Removed report with id: {}".format(report.id))


def publish_reports(reports):
    for report in reports:
        success, data = request.public_report(report)
        if success:
            logger.log("Published report with id: {}".format(report.id))


def game_message_reports(reports):
    def singe_list_message(sublist_reports):
        text = ""
        index = 0
        for report in sublist_reports:
            index += 1
            text += "({})\n{}\n\n".format(index, str(report))
        success, data = request.send_message(DISCUSSSION_ID, text)
        if success:
            logger.log("Message sent")

    sublists = [reports[x:x + REPORTS_IN_MESSAGE] for x in range(0, len(reports), REPORTS_IN_MESSAGE)]
    for sublist in sublists:
        singe_list_message(sublist)


def telegram_message_reports(reports):
    text = ""
    index = 0
    for report in reports:
        index += 1
        text += "({})\n{}\n\n".format(index, str(report))
    telegram.send_message(text)


def process_reports():
    global data
    data = request.enter()[1]
    useful_reports, useless_reports = get_reports()
    remove_reports(useless_reports)
    publish_reports(useful_reports)
    game_message_reports(useful_reports)
    telegram_message_reports(useful_reports)


counter = 0  # if 0 - restock tripwires
while True:
    #try:
        if counter == 0:
            logger.log("Counter==0, restocking...")
            counter = COUNTER_HOURS * 60 // MINUTES_BETWEEN_CHECK
            restock_tripwires()
        process_reports()
        counter -= 1
        logger.log("Sleeping for {} mins".format(MINUTES_BETWEEN_CHECK))
        time.sleep(60 * MINUTES_BETWEEN_CHECK)
    #except:
        pass
        telegram.send_message("SOMETHING IS WRONG!!!", debug=True)
