# Calculadora em Python utilizando funções

import os

executar = True
while executar:
    def somar(x, y):
        total = x + y
        return total
    
    def subtrair(x, y):
        total = x - y
        return total
    
    def multiplicar(x, y):
        total = x * y
        return total
    
    def dividir(x, y):
        total = x / y
        return total


    operador = input('Escolha a operação [+, -, *, /]: ')
    if (operador != '+') and (operador != '-') and (operador != '*') and (operador != '/'):
        print('Digite um operador válido')
        continue
    
    try:
        x = float(input('Primeiro valor: '))
    except ValueError as error:
        if error:
            print('Isso não é um número')
            continue
    
    try:
        y = float(input('Segundo valor: '))
    except ValueError as error:
        if error:
            print('Isso não é um número')
            continue

    if operador == '+':
        resultado = somar(x, y)
        print(f'Resultado: {resultado}')
    elif operador == '-':
        resultado = subtrair(x, y)
        print(f'Resultado: {resultado}')
    elif operador == '*':
        resultado = multiplicar(x, y)
        print(f'Resultado: {resultado}')
    elif operador == '/':
        resultado = dividir(x, y)
        print(f'Resultado: {resultado}')
    else:
        print('Digite um operador matemático')

    continuar = input('Continuar? [S]im / [N]ão: ')
    if continuar == ('S' and 's'):
        executar = True
        os.system('clear')
    elif continuar == ('N' and 'n'):
        executar = False
    else:
        print('Digite uma das opções')

    
