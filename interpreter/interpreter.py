import operator

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

try:
    expr = input("Enter an arithmetic expression (e.g. 1 + 1): ")
    x, op, y = expr.split()
    result = ops[op](int(x), int(y))
    print("{:.1f}".format(result))
except (ValueError, KeyError, ZeroDivisionError):
    print("Invalid input")

#bem simples, basicamente uma calculadora de soma, divisao, multiplicação e subtração, nada complicado.
#so lembra de revisar sobre a função try: