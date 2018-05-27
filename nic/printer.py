from mal_types import *


def pr_str(mal_data, print_readably=False):
    if type(mal_data) is Symbol:
        return mal_data
    elif type(mal_data) is int:
        return str(mal_data)
    elif type(mal_data) is list:
        expression = []
        # Iterate through tree:
        while len(mal_data) > 0:
            expression.append(pr_str(mal_data.pop(0)))

        return "(" + " ".join(expression) + ")"
    elif callable(mal_data):
        print("#<function>")
    elif type(mal_data) is str:
        if print_readably:
            pass
        else:
            print(mal_data)
    elif type(mal_data) is bool:
        print(mal_data)
    elif mal_data is None:
        print("None")
    else:
        print("")
