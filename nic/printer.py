from mal_types import *


def pr_str(mal_data):
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
    else:
        print("")
