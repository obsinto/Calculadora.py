import os
import operator
import platform


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


rename = {
    '+': 'Soma',
    '-': 'Subtração',
    '*': 'Multiplicação',
    '/': 'Divisão',
    '^': 'Exponenciação'
}
operations = {
    rename['+']: operator.add,
    rename['-']: operator.sub,
    rename['*']: operator.mul,
    rename['/']: operator.floordiv,
    rename['^']: operator.pow
}

for i, op in enumerate(operations.keys(), start=1):
    print(f"{i} ->{op}")

while True:
    try:
        choice = int(input("Escolha a opção desejada: "))
        if 1 <= choice < len(operations):
            select_op = list(operations.keys())[choice - 1]
            clear()
            num1 = float(input("Insira o valor: "))
            num2 = float(input("insira o valor: "))
            calc = operations[select_op](num1, num2)
            print(f"Resultado da {select_op}: {calc}")
            break
        else:
            print("Opção inválida")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro válido.")
