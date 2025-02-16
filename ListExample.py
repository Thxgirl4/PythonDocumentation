quadrados = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(quadrados)

print(quadrados[0])  # indexação retorna o item

cubos = [1, 8, 27, 65, 125] # 65 esta errado na lista
cubos[3] = 64
print(cubos)
cubos.append(216) # add o cubo de 6
cubos.append(7 ** 3) # add o cubo de 7
print(cubos)

rgb = ["red", "green", "blue"]
rgba = rgb
id(rgb) == id(rgba) # referenciam os mesmos objetos
rgba.append("Alf")
print(rgb)

letras = ['a', 'b', 'c', 'd']
print(len(letras))