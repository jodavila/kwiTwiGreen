# Percorrer itens de uma lista

#uma lista é uma variavel que possui mais de um objeto, unidimensional = array ou lista, bidimensional = matriz

#declaracao de uma lista
sabores = ["chocolate","morango","baunilha","limão"]

# percorrer lista e mostar sabores

print("os sabores de sorvetes que temos são:")
for sabor in sabores:  # para cada item em lista:
    print(sabor,end=" ") # fazer essa ação

print ("\n") # esse print fará que seja pulado uma linha na tela de saida
# Outro loop / repetição é o while
posicao = 0
sabor=sabores[posicao]
while(sabor != "limão"):
    print(sabor + " não é o que quero, qual é o proximo sabor?")
    sabor=sabores[posicao]
    posicao = posicao + 1
    print(posicao,"\n")