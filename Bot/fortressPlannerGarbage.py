from Request import Request
from Module.Logger import Logger
from Operator.LinkSearch import search_text_for_links


def pick_best_phabitat(phabitats):
    minimal = None
    instance = None
    for phab in phabitats:
         if len(phab.connections) >= 4 and not phab.used:
             minimal = len(phab.connections)
             instance = phab
    if minimal is None:
        return None

    for phab in phabitats:
        if len(phab.connections) < minimal and not phab.used and len(phab.connections) >= 4:
            minimal = len(phab.connections)
            instance = phab

    return  instance


class PHabitat():

    def __init__(self, habitat):
        self.name = habitat.name
        self.connections = []
        self.x = habitat.x
        self.y = habitat.y
        self.link = habitat.link
        self.player_id = habitat.player_id
        self.distance = habitat.distance
        self.used = False
        self.points = habitat.points

        if int(habitat.points) in range(13, 1000):
            self.type = 'CAST'
            self.required_distance = 3
            # self.required_distance = 6
            # self.required_distance = 8
        elif int(habitat.points) in range(1000, 10000):
            self.type = 'FORT'
            self.required_distance = 8
            # self.required_distance = 12
            # self.required_distance = 14
        else:
            self.type = 'CITY'
            self.required_distance = None

    def find_connections(self, habitats):
        for habitat in habitats:
            if habitat.type == self.type and not self.type == 'CITY':
                if self.distance(habitat) <= self.required_distance:
                    self.connections.append(habitat)

    def remove_from_connections(self, habitats):
        pass
        for habitat in habitats:
            if self in habitat.connections:
                habitat.connections.remove(self)
            if habitat in self.connections:
                self.connections.remove(habitat)

    def used_to_true(self):
        self.used = True
        for connection in self.connections:
            for connection_of_connection in connection.connections:
                if connection_of_connection == self:
                    connection.connections.remove(self)

    def peak_4_best_connections(self):
        connections_amounts = []
        connections_of_nodes = {}
        for connection in self.connections:
            amount = len(connection.connections)
            if amount in connections_amounts:
                connections_of_nodes[amount].append(connection)
            else:
                connections_amounts.append(amount)
                connections_of_nodes[amount] = [connection]
        connections_amounts.sort()
        result_connections = []
        while len(result_connections) < 4:
            amount = connections_amounts[0]
            result_connections.append(connections_of_nodes[amount].pop())
            if len(connections_of_nodes[amount]) == 0:
                del connections_of_nodes[amount]
                connections_amounts.remove(amount)
        return result_connections

    def __str__(self):
        type_to_emoji = {'CAST': "🏠", "FORT": "🏰", "CITY": "🏙"}
        type_emoji = type_to_emoji[self.type]
        return "Habitat({} {} [{}] {})".format(type_emoji, self.name, self.points, self.link)



def main():
    email = "shit11@shit.com"
    password = "shit@shit.com"
    logger = Logger(email)
    request = Request(email, password)
    data = request.enter()[1]

    with open("realattackcastles ", "r") as realsFile:
        realsText = realsFile.read()
    realLinks = search_text_for_links(realsText)["habitat"]
    realHabs = data.get_instances_by_links(realLinks)
    habitats = realHabs  # habitat instances
    phabitats = []
    clusters = []
    lonely = []
    for habitat in habitats:
        phabitat = PHabitat(habitat)
        phabitats.append(phabitat)

    for phab in phabitats:
        phab.find_connections([p for p in phabitats if phab != p])

    for phab in phabitats:
        if len(phab.connections) == 0 or phab.type == 'CITY':
            phab.used = True
            lonely.append(phab)

    print('Initial lonely: {}'.format(len(lonely)))
    connections_by_amount = {}

    while pick_best_phabitat(phabitats) is not None:
        center = pick_best_phabitat(phabitats)
        cluster = [center] + center.peak_4_best_connections()
        for hab in cluster:
            hab.used_to_true()
        center.remove_from_connections(center.peak_4_best_connections())
        clusters.append(cluster)
        print('cluster added')

    print('Initially Lonely:')
    for hab in lonely:
        if int(hab.points) < 10000:
            logger.log(hab)
    lonely.clear()
    for phab in phabitats:
        if not phab.used:
            lonely.append(phab)

    print('Clusters:')
    for cl in clusters:
        print('[')
        for hab in cl:
            logger.log(hab)
        print(']')

    print('Cities:')
    for hab in lonely:
        if int(hab.points) > 10000:
            logger.log(hab)

    print('Lonely:')
    for hab in lonely:
        if int(hab.points) < 10000:
            logger.log(hab)

main()