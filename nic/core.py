from printer import pr_str
from reader import read_str
from mal_types import Atom
from functools import reduce


def list2(*args):
    return list(args)


def equals(a, b):
    if not type(a) == type(b):
        return False

    return a == b


def slurp(file_name):
    """Takes a file name and returns a String"""
    with open(file_name) as file:
        string = '"'
        for line in file:
            string += line

    string += '"'

    return string

# String functions
# def pr_str(*args):
#     return " ".join(map(lambda exp: pr_str(exp, True), args))

def do_str(*args):
    return "".join(map(lambda exp: pr_str(exp, False), args))

def prn(*args):
    print(" ".join(map(lambda exp: pr_str(exp, True), args)))
    return None

def println(*args):
    print(" ".join(map(lambda exp: pr_str(exp, False), args)))
    return None

def reset(atm, mal_val):
    atm.val = mal_val
    return mal_val


def concat(*args):
    if len(args) == 0:
        return []
    else:
        return reduce(lambda x, y: x + y, args)



ns = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: int(a / b),
    '<': lambda a, b: a < b,
    '>': lambda a, b: a > b,
    '=': equals,
    '<=': lambda a, b: a <= b,
    '>=': lambda a, b: a >= b,
    'prn': lambda x: pr_str(x),
    'list': list2,
    'list?': lambda x: type(x) is list,
    'count': lambda x: len(x) if x else 0,
    'empty?': lambda x: len(x) == 0,
    'read-string': read_str,
    'pr-str': pr_str,
    'str': do_str,
    'println': println,
    'slurp': slurp,
    'atom': lambda x: Atom(x),
    'atom?': lambda x: isinstance(x, Atom),
    'deref': lambda x: x.val,
    'reset!': reset,
    'swap!': 1,
    'cons': lambda x, y: [x] + y,
    'concat': concat,

}

