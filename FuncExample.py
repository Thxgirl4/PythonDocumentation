def fib (n):
    """Imprime a série de Fibonacci menor que n"""
    a, b = 0, 1
    while a < n :
        print(a, end = '')
        a, b = b, a + b
        print()


fib(2000)

# A palavra-chave def introduz uma definição de função .
# Ela deve ser seguida pelo nome da função e pela lista entre parênteses de parâmetros formais.
# As instruções que formam o corpo da função começam na próxima linha e devem ser recuadas.
