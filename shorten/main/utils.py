from random import choices
import string

def generate_short_id(num_char):
    # TODO return random & unique short id for shorten
    return ''.join(choices(string.ascii_letters, k=num_char))

