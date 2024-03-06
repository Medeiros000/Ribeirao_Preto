# 5) Escreva um programa que inverta os caracteres de um string.
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;
# Pedindo ao usuário para digitar uma palavra

prompt = "Digite uma palavra para ser invertida: "

# Recebendo a palavra do usuário
string = input(prompt)

# Convertendo a string para uma lista
string_lista = list(string)

# Criando uma lista vazia para armazenar a lista reversa
string_lista_reversa = []

# Calculando o tamanho da lista
listaLen = len(string_lista)

# Invertendo a lista
while listaLen > 0:
    # adicionando o último elemento da lista para a lista reversa
    string_lista_reversa.append(string_lista[listaLen - 1])

    # Removendo o último elemento da lista
    listaLen = listaLen - 1

# Usando o join para união dos elementos da lista
string_reversa = ''.join(string_lista_reversa)

# Imprimindo a string reversa
print(string_reversa)