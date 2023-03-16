### Contains functions to convert between formats


# string to bytestring
# the raw option converts the intermediate str representation to a bytestring
def tobyte(string, raw=False):
    if not raw:
        return string.encode()
    else:
        return string.encode('all-escapes')

# bytestring to string
# the raw option converts the bytestring to an intermediate str representation
def tostr(string, raw=False):
    if not raw:
        return string.decode()
    else:
        return string.decode('all-escapes')
