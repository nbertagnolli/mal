import reader
import printer
import operator

from mal_types import *


repl_env = {'+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)}


def eval_ast(ast, repl_env):
    if type(ast) is Symbol:
        # Look up the value of the symbol in the repl environment
        if ast in repl_env:
            return repl_env[ast]
        else:
            raise("Not a Valid Symbol")
    elif type(ast) is list:
        # Run EVAL on every element of the list
        evaled_list = []
        for element in ast:
            evaled_list.append(EVAL(element, repl_env))
        return evaled_list
    else:
        return ast


def READ(read_in):
    return reader.read_str(read_in)


def EVAL(eval_in, repl_env):
    if type(eval_in) is list:
        # return the input if it is an empty list
        if not eval_in:
            return eval_in
        else:
            evaled_list = eval_ast(eval_in, repl_env)
            return evaled_list[0](*evaled_list[1:])
    else:
        return eval_ast(eval_in, repl_env)


def PRINT(print_in):
    return printer.pr_str(print_in)


def rep(rep_in):
    read_out = READ(rep_in)
    eval_out = EVAL(read_out, repl_env)
    print_out = PRINT(eval_out)
    return print_out


while True:
    try:
        usr_input = input("user> ")
        print(rep(usr_input))
    except EOFError:
        break