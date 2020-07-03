from Request import Request
from Module.Logger import Logger
import time
mails = [
"arianaanaira@yandex.com",
"selenaaneles@ukr.net",
"khrystynaanytsyrhk@outlook.com",
"camilaalimac@mail.ru",
"shakiraarikash@icloud.com",
]
names = [
"Nichobow",
"Nichoth",
"Antinicholas",
"Lobstroscholas",
"Scolka"
]
for number in range(len(mails)):
    logger = Logger("mail placeholder")
    request = Request(mails[number], "3259")
    data = request.enter()[1]
    # alliance = data.get_instance_by_link("l+k://alliance?408&230")
    # res1 = request.apply_to_alliance(alliance.id)
    res2 = request.change_nickname(names[number])
    # print("{} - apply:{} change:{}".format(number, res1[0], res2[0]))
    print("{} - rename:{}".format(number, res2[0]))
    time.sleep(11)
