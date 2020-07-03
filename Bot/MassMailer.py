from Request import Request
from Module.Logger import Logger

logger = Logger("-")
request = Request("dkdj@kdjd.de", "1")
data = request.enter()[1]
print("im in")
res = request.load_worlds()[1]["allAvailableWorlds"]
for server in res:
    if server["language"] in ["de"]:
        logger.log(server["url"])
exit()
alliancesFromRating = request.load_alliance_rating()[1]["allianceRanks"]
ids = [allianceFromRating["id"] for allianceFromRating in alliancesFromRating]
alliances = data.get_instances_by_ids("alliance", ids)
logger.log(alliances)
players = data.get_players_by_alliances(alliances)
subject = "!!!"
content = """Ihr Russen spielt euch immer auf und denkt ihr hättet einen Wert in Lords and Knights und in der echten Welt 
Kommt auf G4 und holt euch die Niederlage ab die ihr auch im Weltkrieg kassiert hättet wenn eure großen Brüder USA Großbritannien und Frankreich euch nicht gerettet hätten.
Alleine seid ihr Russen nichts, Insekten unter meinen deutschen Füßen."""
counter = 0
for player in players:
    counter += 1
    response = request.create_message(subject, player.id, content)
    if response[0]:
        logger.log("{}/{} - Sent to {}".format(counter, len(players), player))
    else:
        logger.log("{}/{} - Didnt succeed sending message to {}".format(counter, len(players), player))
