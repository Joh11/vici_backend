"""Utility stuff to upload files using POST"""

from django.core.files import File

def match_file(name):
    """Returns file__<>__<> -> (<>, <>)"""
    tokens = name.split('__')
    if len(tokens) < 3 or tokens[0] != 'file':
        return None
    return tokens[1], ''.join(tokens[2:])

# TODO SECURITY BREACH HERE
def get_file_from_data(data, filename):
    with open(filename, 'wb+') as dest:
        dest.write(data.encode())
    return File(open(filename, 'rb'))
