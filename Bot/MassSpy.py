from Request import Request
from Module.Logger import Logger
import time
import random
from Operator.LinkSearch import search_text_for_links

logger = Logger("-")
request = Request("Goodenough@acc.com", "123")
data = request.enter()[1]
logger.log("logged in")
own_castle = data.get_instance_by_link("l+k://coordinates?16546,16440&230")
logger.log(own_castle)
with open("realattackcastles ", "r") as realsFile:
    realsText = realsFile.read()
realLinks = search_text_for_links(realsText)["habitat"]
realHabs = data.get_instances_by_links(realLinks)
habitats = realHabs  # habitat instances
for habitat in habitats:
    # time.sleep(random.randint(4, 8))
    logger.log("Spy to ")
    logger.log(habitat)
    success, info = request.send_spy(habitat.id, own_castle.id, "1")
    if success:
        logger.log("successfully")
    else:
        logger.log("unsuccessfully. Error: {}".format(info))
    logger.log("-")
