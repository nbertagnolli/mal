import reader
import printer
import operator
from env import Env
from core import ns

from mal_types import *


def eval_ast(ast, repl_env):
    if type(ast) is Symbol:
        # Look up the value of the symbol in the repl environment
        return repl_env.get(ast)
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


def EVAL(ast, env):
    if type(ast) is list:
        # return the input if it is an empty list
        if not ast:
            return ast
        else:
            # get the first element of the list
            arg0 = ast[0]

            # Examine all language special forms and their arguments
            # before applying to all remaining elements of the list
            if arg0 == "def!":
                result = EVAL(ast[2], env)
                return env.set(ast[1], result)
            elif arg0 == 'let*':
                let_env = Env(outer=env)
                for i in range(0, len(ast[1]), 2):
                    key = ast[1][i]
                    value = EVAL(ast[1][i + 1], let_env)
                    let_env.set(key, value)

                return EVAL(ast[2], let_env)
            elif arg0 == 'do':
                return eval_ast(ast[1:], env)[-1]
            elif arg0 == 'if':
                result = EVAL(ast[1], env)
                if result:
                    return EVAL(ast[2], env)
                else:
                    if len(ast) >= 4:
                        return EVAL(ast[3], env)
                    else:
                        return None
            elif arg0 == 'fn*':
                def func(*args):
                    new_env = Env(outer=env, binds=ast[1], exprs=list(args))
                    return EVAL(ast[2], new_env)
                return func
            else:
                evaled_list = eval_ast(ast, env)
                return evaled_list[0](*evaled_list[1:])

    # If it is not a list just evaluate it
    else:
        return eval_ast(ast, env)


def PRINT(print_in):
    return printer.pr_str(print_in)


def rep(rep_in):
    read_out = READ(rep_in)
    eval_out = EVAL(read_out, repl_env)
    print_out = PRINT(eval_out)
    return print_out


repl_env = Env()

# Add namespace variables to repl environment
for key, value in ns.items():
    repl_env.set(key, value)

while True:
    try:
        usr_input = input("user> ")
        print(rep(usr_input))
    except EOFError:
        break