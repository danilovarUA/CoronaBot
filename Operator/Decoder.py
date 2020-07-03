def surrogate_decoding(text):
    return str(text).encode('utf-16', 'surrogatepass').decode('utf-16')
