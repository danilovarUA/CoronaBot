from Operator import Parser


def validate(text):
    try:
        parser_result = Parser.parse(text)
    except SyntaxError:
        raise ValueError("Incorrect syntax: " + text)
    if "error" in parser_result:
        raise ValueError("Response contains error saying: " + parser_result["error"])
