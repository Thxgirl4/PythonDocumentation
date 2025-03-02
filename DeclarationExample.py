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


# break & continue
# A breakdeclaração sai do envoltório forou whilelaço mais interno:
for n in range(2, 10) :
    for x in range(2, n) :
        if n % x == 0 :
            print(f"{n} é igual a {x} * {n // x}")
            break

# A continuedeclaração continua com a próxima iteração do loop:
for num in range(2, 20) :
    if num % 2 == 0 :
        print(f"numero é par {num} ")
        continue
    print(f"numero ímpar {num} ")


# else in for loop