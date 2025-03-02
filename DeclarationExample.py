# if
x = int (input ("Insira um inteiro: "))
if x < 0:
    x = 0
    print('Negativo alterado para zero')
elif x == 0 :
    print('Zero')
elif x == 1 :
    print('Unico')
else :
    print('Mais')


# for
palavras = ['gato', 'macaco', 'pneumoultravulcanocaniose']
for a in palavras :
    print(a, len(a))


# range() Ela gera progressões aritméticas
for i in range(5) :
    print(i)

list(range(5, 10))

a = ['Marcos', 'tinha', 'um', 'ponei']
for i in range(len(a)) :
    print(i, a [i])
