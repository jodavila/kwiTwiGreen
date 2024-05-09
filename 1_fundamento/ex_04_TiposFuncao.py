# função sem retorno e sem entrada
def MostrarData1():
    print("15/01/2024")

# função sem retorno e com entrada
def MostarData2(dia):
    print(dia)

# funcao com retorno e sem entrada
def InformarDia1():
    return "15/01/2024"

# funcao com retorno e com entrada
def InformarDia2(dia):
    return "Hoje é " + dia


##MostrarData1()
##MostarData2("15/01/2024")

# InformarDia1()

# dia = InformarDia1()
# print ("valor " + dia)

print(InformarDia2(InformarDia1()))