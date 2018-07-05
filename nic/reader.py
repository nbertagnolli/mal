import re
from mal_types import *


def is_int(s):
    try:
        int(s)
        return True
    except:
        return False


def read_str(string):
    return read_form(Reader(tokenizer(string)))


def tokenizer(string):
    p = re.compile("""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"|;.*|[^\s\[\]{}('"`,;)]*)""")
    return p.findall(string)


def read_form(reader):
    first = reader.peek()
    # Ignore comments
    if first[0] == ';':
        reader.next()
        return None
    if first == "(":
        return read_list(reader)
    elif first == '[':
        return read_vector(reader)
    else:
        return read_atom(reader)


def _unescape(s):
    return s.replace('\\\\', '\u029e').replace('\\"', '"').replace('\\n', '\n').replace('\u029e', '\\')

def read_atom(reader):
    # Figure out type
    token = reader.next()
    if is_int(token):
        return int(token)
    elif token == 'nil':
        return None
    elif token == 'true':
        return True
    elif token == 'false':
        return False
    elif type(token) is str:
        if len(token) > 0 and token[0] == '"' and token[-1] == '"':
            return _unescape(token[1:-1])
        else:
            return Symbol(token)


def read_sequence(reader, start='(', end=')'):
    # Create the start of the list expression and increment reader
    token = reader.next()
    expressions = list()
    if token != start:
        raise Exception('Expected ' + start + " found " + token)

    while reader.peek() != end and reader.peek() is not None:
        expressions.append(read_form(reader))

    if reader.peek() is None:
        return "expected )"
    # TODO:: CHECK IF EOF BEFORE ")"
    reader.next()
    return expressions


def read_vector(reader):
    return read_sequence(reader, start='[', end=']')


def read_list(reader):
    return read_sequence(reader)


class Reader:

    def __init__(self, tokens):
        self.position = 0
        self.tokens = tokens

    def next(self):
        current_token = self.tokens[self.position]
        self.position += 1
        return current_token

    def peek(self):
        return self.tokens[self.position]
