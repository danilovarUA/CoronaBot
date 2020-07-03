from Request import Request
from Module.Logger import Logger
from Operator.LinkSearch import search_text_for_links
email = "shit11@shit.com"
password = "shit@shit.com"
logger = Logger(email)
request = Request(email, password)
data = request.enter()[1]

hunter = data.get_instance_by_link("l+k://player?377&230")
has = data.get_habitats_by_players([hunter])
for h in has:
    logger.log(h)
exit()

# load spies
with open("ourSpiesText", "r") as targetPlayersFile:
    spiesText = targetPlayersFile.read()
spiesPlayersLinks = search_text_for_links(spiesText)["player"]
spiesPlayers = data.get_instances_by_links(spiesPlayersLinks)

# center
centerHab = data.get_instance_by_link("l+k://coordinates?16473,16384&230")

# Get targets
targetAlliances = data.get_instances_by_links(["l+k://alliance?71&230"])
targetPlayers = data.get_players_by_alliances(targetAlliances)
targetPlayers = [player for player in targetPlayers if player not in spiesPlayers]
targetPlayers = [player for player in targetPlayers if not player.vacation]
targetHabitats = data.get_habitats_by_players(targetPlayers)

# Clean up habitats
targetHabitats = [habitat for habitat in targetHabitats if habitat.points > 200]

# Sort habitats
targetsByDistance = {}
for habitat in targetHabitats:
    distance = habitat.distance(centerHab)
    if distance in targetsByDistance:
        targetsByDistance[distance].append(habitat)
    else:
        targetsByDistance[distance] = [habitat]
sorted_distances = sorted(targetsByDistance)
index = 0
for distance in sorted_distances:
    logger.log("DISTANCE: {}".format(distance))
    habitats = targetsByDistance[distance]
    for habitat in habitats:
        index += 1
        logger.log("{} - {}".format(index, habitat))

