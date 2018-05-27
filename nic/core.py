from printer import pr_str


def list2(*args):
    return list(args)

ns = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: int(a / b),
    '<': lambda a, b: a < b,
    '>': lambda a, b: a > b,
    '<=': lambda a, b: a <= b,
    '>=': lambda a, b: a >= b,
    'prn': lambda x: pr_str(x, print_readably=True),
    'list': list2,
    'list?': lambda x: type(x) is list,
    'count': lambda x: len(x) if x else 0,
    'empty?': lambda x: len(x) == 0

}

