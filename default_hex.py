import sys

def display_as_hex(item):
    if isinstance(item, (int, long)):
        print(hex(item))
    else:
        print(repr(item))

sys.displayhook = display_as_hex
