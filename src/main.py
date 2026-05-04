import sys
from utils import *

def expression_evaluator(tokens):
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token == "+":
            second = stack.pop()
            first = stack.pop()
            stack.append(first + second)
        elif token == "-":
            second = stack.pop()
            first = stack.pop()
            stack.append(first - second) 
        elif token == "*":
            second = stack.pop()
            first = stack.pop()
            stack.append(first * second) 
        elif token == "/":
            second = stack.pop()
            first = stack.pop()
            stack.append(first / second) 
        print(stack)
    return stack[0]

def interpret(file):
    with open(file, "r") as f:
        content = f.read()
    lines = content.splitlines()
    for line in lines:
        if not is_blank_line(line):
            tokens = line.split()
            print(expression_evaluator(tokens))

cli_args = sys.argv
file = cli_args[1]
interpret(file)

