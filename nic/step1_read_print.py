import reader
import printer


def READ(read_in):
    return reader.read_str(read_in)


def EVAL(eval_in):
    return eval_in


def PRINT(print_in):
    return printer.pr_str(print_in)


def rep(rep_in):
    read_out = READ(rep_in)
    eval_out = EVAL(read_out)
    print_out = PRINT(eval_out)
    return print_out


while True:
    try:
        usr_input = input("user> ")
        print(rep(usr_input))
    except EOFError:
        break
