
def READ(read_in):
    return read_in


def EVAL(eval_in):
    return eval_in


def PRINT(print_in):
    return print_in


def rep(rep_in):
    read_out = READ(rep_in)
    eval_out = EVAL(read_out)
    print_out = PRINT(eval_out)
    return print_out


while True:
    try:
        usr_input = input("user> ")
    except EOFError:
        usr_input = None
    print(rep(usr_input))
