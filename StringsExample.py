print('spam eggs')  # single quotes

print("Paris rabbit got your back :)! Yay!")  # double quotes

print('1975')  # digits and numerals enclosed in quotes are also strings

print('d\'água')  # use \' para escapar a aspa simples...

print("d'água")  # ...ou use aspas duplas

print('"Sim", eles disseram.')

print("\"Sim\", eles disseram.")

print('"Copo d\'água", eles pediram.')

s = 'Primeira linha. \n Segunda linha.'  # com print(), caracteres especiais são interpretados, então \n produz nova linha
print(s)

print(r'C:\algum\nome')  # observe o r antes das aspas

# 3 vezes 'un', seguido por 'ium'
print(3 * 'ola ' + 'humano')

palavra = 'Python'
print(palavra[2]) # caracter na posição 2
print(len(palavra)) # tamanho da palavra
print(palavra[-1]) # ultimo caracter
print(palavra[0:2]) # caracteres da posição 0 (incluída) até 2 (excluída)
print(palavra[:2])  # caracteres do início até a posição 2 (excluída)
print(palavra[4:])   # caracteres da posição 4 (incluída) até o fim

