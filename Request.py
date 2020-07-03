import hashlib
import urllib
import time
from Operator.Requester import Requester
from Data.Data import Data
from Module.Logger import Logger

REATTEMPTS_COUNT = 3
RELOGIN_TIMEOUT = 6

WORLDS_URL = "https://login.lordsandknights.com/XYRALITY/WebObjects/BKLoginServer.woa/wa/worlds"


class Request:
    def __init__(self, email, password):
        self.requester = Requester(email, password)
        self.data = None
        self.logger = Logger(email)

    def request(self, url, params, short_url=True, times=REATTEMPTS_COUNT, sleeping_time=3):
        success = False
        data = "No error info"
        while not success and times > 0:
            times -= 1
            success, data = self.requester.make(url, params, short_url)
            if not success and times > 0:
                if "No session" in str(data):
                    self.logger.warning("re-loginning")
                    self.enter()
                elif "Please try again in a minute" in str(data):
                    self.logger.warning("{} secs waiting".format(sleeping_time))
                    time.sleep(sleeping_time)
                else:
                    self.logger.warning(data)
        if success:
            self.data.parse_dict(data)
        return [success, data]

    def enter(self, times=REATTEMPTS_COUNT):
        success = False
        data = "No error info"
        while not success and times > 0:
            times -= 1
            success, data = self.requester.enter()
            if not success and times > 0:
                self.logger.warning("Cant log in {}".format(data))
                time.sleep(RELOGIN_TIMEOUT)
        if success:
            self.logged_in = True
            if self.data is None:
                self.data = Data(data, self.requester.player_info, self)
            else:
                self.data.parse_dict(data)
        return [success, self.data]

    def request_help(self):
        url = "AllianceAction/helpAllMembersForFree"
        params = {}
        return self.request(url, params)

    def habitat_info(self, habitat_id):
        url = "HabitatAction/habitatInformation"
        params = {
            "id": habitat_id
        }
        return self.request(url, params)

    def alliance_info(self, alliance_id):
        url = "AllianceAction/allianceInformation"
        params = {
            "id": alliance_id
        }
        return self.request(url, params)

    def player_info(self, player_id):
        url = "ProfileAction/playerInformation"
        params = {
            "id": player_id
        }
        return self.request(url, params)

    def send_message(self, content, discussion_id):
        url = "DiscussionAction/addDiscussionEntry"
        params = {
            "discussionId": str(discussion_id),
            "content": urllib.parse.quote_plus(str(content))
        }
        return self.request(url, params)

    def public_report(self, report):
        url = "ReportAction/setReportPublished"
        params = {
            "id": str(report.id),
            "published": "true"
        }
        return self.request(url, params)

    def fetch_reports(self):
        url = "ReportAction/habitatReportArray"
        params = {}
        return self.request(url, params)

    def send_support(self, destination_id, unit_dictionary, source_id):
        url = "TransitAction/startTransit"
        params = {
            "transitType": str(0),
            "unitDictionary": str(unit_dictionary),
            "sourceHabitatID": str(source_id),
            "resourceDictionary": "{}",
            "destinationHabitatID": str(destination_id)

        }
        return self.request(url, params)

    def send_resources(self, destination_id, unit_dictionary, resource_dictionary, source_id):
        url = "TransitAction/startTransit"
        params = {
            "transitType": str(4),
            "resourceDictionary": str(resource_dictionary),
            "unitDictionary": str(unit_dictionary),
            "sourceHabitatID": str(source_id),
            "destinationHabitatID": str(destination_id)
        }
        return self.request(url, params)

    def delete_report(self, report):
        url = "ReportAction/deleteHabitatReport"
        params = {
            "id": str(report.id)
        }
        return self.request(url, params)

    def recall_support(self, source_id, unit_dictionary, destination_id):
        url = "TransitAction/startTransit"
        params = {
            "destinationHabitatID": str(destination_id),
            "sourceHabitatID": str(source_id),
            "unitDictionary": str(unit_dictionary),
            "transitType": str(1)
        }
        return self.request(url, params)

    def load_alliance_rating(self):
        url = "QueryAction/allianceRanks"
        params = {
            "offset": str(0),
            "limit": str(50)
        }
        return self.request(url, params)

    def load_player_rating(self, offset):
        url = "QueryAction/playerRanks"
        params = {
            "offset": str(offset),
            "limit": str(50)
        }
        return self.request(url, params)

    def create_message(self, subject, player_id, content):
        url = "DiscussionAction/createDiscussion"
        params = {
            "content": str(content),
            "subject": str(subject),
            "receivingPlayerArray": str(player_id)
        }
        return self.request(url, params)

    def check_valid_login_browser(self):
        url = ""
        params = {
            "login": self.requester.email,
            "password": self.requester.password_hashed,
            "deviceType": "Email",
        }
        return self.request(url, params, short_url=False, times=1)

    def load_worlds(self):
        url = WORLDS_URL
        params = {
            "login": self.requester.email,
            "deviceId": self.requester.email,
            "password": self.requester.password_hashed,
            "deviceType": "Email",
        }
        return self.request(url, params, short_url=False)

    def send_attack(self, destination_id, unit_dictionary, source_id):
        url = "TransitAction/startTransit"
        params = {
            "unitDictionary": str(unit_dictionary),
            "sourceHabitatID": str(source_id),
            "destinationHabitatID": str(destination_id)
        }
        return self.request(url, params)

    def set_diplo(self, alliance_id, alliance_rel):
        url = "AllianceAction/setDiplomaticRelation"
        params = {
            "id": str(alliance_id),
            "diplomaticValue": str(alliance_rel)
        }
        return self.request(url, params)

    def send_spy(self, destination_id, source_id, amount=1):
        url = "SpyAction/startSpyingTransit"
        params = {
            "copperAmount": str(amount),
            "sourceHabitatID": str(source_id),
            "destinationHabitatID": str(destination_id)
        }
        return self.request(url, params)

    def map(self, x, y, width, height):
        url = "MapAction/map"
        params = {
            "mapX": x,
            "mapY": y,
            "mapWidth": width,
            "mapHeight": height
        }
        return self.request(url, params)

    def change_password(self, new):
        url = ""
        params = {
            "password": self.requester.password_hashed,
            "newPassword": hashlib.sha256(new.encode("utf-8")).hexdigest(),
            "deviceId": self.requester.email,
            "login": self.requester.email,
            "deviceType": "Email"
        }
        return self.request(url, params, short_url=False)

    def create_account(self, nick, world_id):
        url = "LoginAction/create"
        params = {
            "worldId": str(world_id),
            "nick": nick,
            "deviceId": self.requester.email,
            "deviceType": "Email",
            "login": self.requester.email,
            "password": self.requester.password_hashed,
        }
        print(params)
        return self.request(url, params)

    def apply_to_alliance(self, alliance_id):
        url = "AllianceAction/apply"
        params = {
            "id": alliance_id
        }
        return self.request(url, params)

    def change_nickname(self, name):
        url = "ProfileAction/changeNickname"
        params = {
            "nick": name
        }
        return self.request(url, params)

    def get_messages_titles(self):
        url = "MessageAction/messageTitleArray"
        params = {}
        return self.request(url, params)
