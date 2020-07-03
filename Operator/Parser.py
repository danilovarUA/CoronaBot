from Operator import Decoder
import re


def parse(text):
    temp_namespace = {}
    temp_dictionary_name = "temp_name"
    text = text.replace("=", ":")
    text = text.replace("(", "[")
    text = text.replace(")", "]")
    text = text.replace(";", ",")
    text = re.sub(r'\\U', "\\u", text)
    text = Decoder.surrogate_decoding(text)
    exec(temp_dictionary_name + "=" + text, temp_namespace)
    return temp_namespace[temp_dictionary_name]