# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

a = 0
b = 1
anterior = 1

Fibonacci = a + b

prompt = "Digite um número: "
n = int(input(prompt))

while Fibonacci <= n:
    # print(Fibonacci, n)
    # print(n == Fibonacci)
    if n == Fibonacci:
        print(f'O número {n} é um número de Fibonacci.')
        break
    temp = Fibonacci
    Fibonacci = Fibonacci + anterior
    anterior = temp
    if(n != Fibonacci & Fibonacci > n):
        print(f'O número {n} não é um número de Fibonacci.')
        
