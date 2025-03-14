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
for n in range(2, 10) :
    for x in range(2, n) :
        if n % x == 0 :
            print(n, 'é igual a', x, '*', n // x)
            break
    else :
        # o loop falhou em encontrar um fator
        print(n, 'é um numero primo')
# Em um forloop, a elsecláusula é executada após o loop terminar sua iteração final,
# ou seja, se nenhuma interrupção tiver ocorrido.
# Se a condição for verdadeira, a break acontecerá.
# Se a condição nunca for verdadeira, a else cláusula fora do loop será executada.


# pass
# while True :
    # pass   # Ocupado-espera por interrupção do teclado (Ctrl+C)

# Outro lugar pass que pode ser usado é como um espaço reservado para uma função ou corpo condicional quando você está trabalhando em um novo código,
# permitindo que você continue pensando em um nível mais abstrato.
# O pass é ignorado silenciosamente:

# def initlog(* args) :
    #pass


# match
# Uma match declaração pega uma expressão e compara seu valor a
# padrões sucessivos dados como um ou mais blocos case.
# Isso é superficialmente semelhante a uma declaração switch

def http_error(status) :
    match status :
        case 400 :
            return "Solicitação invalida"
        case 404 :
            return "Não encontrado"
        case 418 :
            return "Sou um bule de chá"
        case 401 | 403 | 405 :
            return "Não permitido"
        case _ :
            return "Something went wrong with internet"
#  o “nome da variável” _atua como um curinga
#  e nunca falha em corresponder

class Ponto :
    def __init__(self, x, y):
        self.x = x
        self.y = y
def where_is(Ponto):
    match Ponto:
        case Ponto(x=0, y=0):
            print("Origem")
        case Ponto(x=0, y=y):
            print((f"Y={y}"))
        case Ponto(x=x, y=0):
            print(f"X={x}")
        case Ponto():
            print("Somewhere else")
        case _:
            print("Not a point")

