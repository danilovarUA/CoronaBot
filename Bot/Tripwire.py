import time
from Module import Telegram
from Request import Request

telegram = Telegram.Telegram()
excluded_players = []
DISCUSSION_ID = ""
MINUTES_BETWEEN_CHECK = 3


def refresh_tripwires(account):
    for habitat_trip in habitat_trips:
        print("\t" * 2 + "{}/{}: ".format(trip_counter, len(habitat_trips)), end="")
        if habitat_trips[habitat_trip] > 0:
            unit_dictionary = "{1=" + str(habitat_trips[habitat_trip]) + ";}"
            counter = 1
            while counter > 0:
                result = account.support(habitat_trip, unit_dictionary, Data.trips_source)
                if result[0]:
                    counter = 0
                    print("\t" * 2 + "support to {} of amount {} sent".format(habitat_trip, habitat_trips[habitat_trip]))
                else:
                    login(account)
                    counter -= 1
                    print(result[1])
                    print("\t" * 2 + "support to {} of amount {} was not send".format(habitat_trip, habitat_trips[habitat_trip]))
        else:
            unit_dictionary = "{1=" + str(- habitat_trips[habitat_trip]) + ";}"
            counter = 2
            while counter > 0:
                result = account.recall_units(habitat_trip, unit_dictionary, Data.trips_source)
                if result[0]:
                    counter = 0
                    print("\t" * 2 + "units from {} in amount {} recalled".format(habitat_trip, habitat_trips[habitat_trip]))
                else:
                    login(account)
                    counter -= 1
                    print(result[1])
                    print("\t" * 2 + "units from {} in amount {} was not recalled".format(habitat_trip, habitat_trips[habitat_trip]))
