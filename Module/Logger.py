import datetime
from Operator.Decoder import surrogate_decoding


class Logger:

    def __init__(self, email, show_logs=True, show_warnings=True):
        self.show_logs = show_logs
        self.show_warnings = show_warnings
        self.email = email

    def log(self, text):
        if self.show_logs:
            self._message(text)

    def warning(self, text):
        if self.show_warnings:
            self._message(text, pretext='<WARN> ')

    def error(self, text, raiseValueError=False):
        self._message(text, pretext='<ERROR> ')
        if raiseValueError:
            raise ValueError(text)

    def _message(self, message, pretext=""):
        time_string = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        text = "{}[{}]({}) {}".format(pretext, time_string, self.email, message)
        text = surrogate_decoding(text)
        print(text)
