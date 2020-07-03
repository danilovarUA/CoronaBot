import re


def search_text_for_links(text):
    link_type_to_pattern = {'alliance': r'l\+k://alliance\?\d+&\d+',
                            'player': r'l\+k://player\?\d+&\d+',
                            'habitat': r'l\+k://coordinates\?\d+,\d+&\d+'}
    # TODO add region

    links_by_type = {}
    for link_type in link_type_to_pattern.keys():
        links_by_type[link_type] = re.findall(link_type_to_pattern[link_type], text, flags=0)
    return links_by_type
