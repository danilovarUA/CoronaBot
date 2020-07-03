def create_header(cookie_data_dictionary=None):
    cookie_data_string = ""
    if cookie_data_dictionary is None:
        cookie_data_dictionary = {}
    cookie_data_dictionary.update({"G_ENABLED_IDPS": "google"})
    for element in cookie_data_dictionary:
        cookie_data_string += element + "=" + cookie_data_dictionary[element] + ";"
    login_headers = \
        {

            "XYClient-Capabilities": "base,fortress,city,partialTransits,starterpack,requestInformation,partialUpdate,regions",
            "Cookie": cookie_data_string,
            "XYClient-Platform": "browser"
        }
    return login_headers
