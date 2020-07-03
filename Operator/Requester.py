from . import Parser, Header, Validator
import requests
import hashlib
from Module import Logger
import time


REQUEST_TIMEOUT = 6
SERVER_URL = "https://backend2.lordsandknights.com/XYRALITY/WebObjects/LKWorldServer-RE-DE-4.woa/wa/"
VALID_BROWSER_URL = "https://login.lordsandknights.com/XYRALITY/WebObjects/BKLoginServer.woa/wa/LoginAction/checkValidLoginBrowser"
CHANGE_PASSWORD_URL = 'https://login.lordsandknights.com/XYRALITY/WebObjects/BKLoginServer.woa/wa/LoginAction/changePassword'


class Requester:

    def __init__(self, email, password):
        self.logger = Logger.Logger("Requester of {}".format(email))
        self.email = email
        self.password = password
        self.password_hashed = hashlib.sha256(self.password.encode("utf-8")).hexdigest()
        self.header = Header.create_header()
        self.player_info = None

    def make(self, url, params, short_url, parse=True, return_cookies=False):
        if short_url:
            full_url = SERVER_URL + url
        else:
            full_url = url
        try:
            to_check, to_use = self.send(full_url, params, return_cookies)
            Validator.validate(to_check)
            if parse:
                return [True, Parser.parse(to_use)]
            else:
                self.header = Header.create_header(to_use)
                self.player_info = to_use
                return [True, "Headers updated"]
        except requests.exceptions.ReadTimeout or requests.exceptions.ConnectTimeout:
            return [False, "Timeout"]
        except requests.exceptions.ConnectionError:
            return [False, "Can not establish connection, check internet"]
        except ValueError as error:
            return [False, str(error)]

    def send(self, url, params, return_cookies):
        response = requests.get(url, params=params, headers=self.header, timeout=REQUEST_TIMEOUT)
        if return_cookies:
            cookie_data_list = response.cookies.items()
            cookie_data_dict = {}
            for element in cookie_data_list:
                cookie_data_dict[element[0]] = element[1]
            return [response.text, cookie_data_dict]
        else:
            return [response.text, response.text]

    def enter(self):
        def reset():
            self.gen_dict = None
            self.header = Header.create_header()

        token_result = self.token()
        if not token_result[0]:
            reset()
            return token_result

        login_result = self.login()
        if not login_result[0]:
            reset()
        return login_result

    def token(self):
        url = "LoginAction/token"
        params = {
            "login": self.email,
            "password": self.password_hashed,
            "deviceType": "Email",
        }
        return self.make(url=url,
                         params=params,
                         short_url=True,
                         parse=False,
                         return_cookies=True)

    def login(self):
        url = "LoginAction/login"
        params = {}
        return self.make(url, params, short_url=True)
