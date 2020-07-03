import requests
import urllib
from Operator.Decoder import surrogate_decoding

TOKEN = "560145098:AAGoLcHjsnj59TOGcPoZ2WkcVh_M4WtKmsU"
CHAT_ID = "-408438399"
DEBUG_CHAT_ID = "-430114074"


class Telegram:
    """This class sends messages to main chat and some debug info to debug chat. There is only one debug and chat
    for messages can be chosen.
    """
    url = None
    chat_id = None
    debug_chat_id = None

    def __init__(self, chat_id=CHAT_ID, debug_chat_id=DEBUG_CHAT_ID, token=TOKEN):
        self.url = "https://api.telegram.org/bot{}/".format(token)
        self.chat_id = chat_id
        self.debug_chat_id = debug_chat_id

    def send_message(self, text, debug=False):
        text = surrogate_decoding(text)
        text = urllib.parse.quote_plus(text)
        if debug:
            chat_id = self.debug_chat_id
        else:
            chat_id = self.chat_id
        url = self.url + "sendMessage?text={}&chat_id={}".format(text, chat_id)
        # TODO rewrite that with params
        return self._get_request(url)

    def _get_request(self, url):
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content
