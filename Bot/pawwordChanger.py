from Request import Request
from Module.Logger import Logger
import time
mails = [
"maniac.geiv3259@gmail.com",
"anastasia.geiv3259@gmail.com",
"anna.geiv3259@gmail.com",
"elsa.geiv3259@gmail.com",
"agnes.geiv3259@gmail.com",
]

for number in range(len(mails)):
    new_password = "32594398"
    logger = Logger("mail placeholder")
    request = Request(mails[number], "3259")
    data = request.enter()[1]
    # alliance = data.get_instance_by_link("l+k://alliance?1035&230")
    res1 = request.change_password(new_password)
    # print("{} - apply:{} change:{}".format(number, res1[0], res2[0]))
    print("{} - change:{}".format(number, res1[0]))
    time.sleep(11)
