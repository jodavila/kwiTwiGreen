__name__= "Joana"
__date__="15/01/2024"

#a = 1
#b = 2
#c = 4

print("Escreva o valor para A: ")
a = input()
print("Escreva o valor para B: ")
b = input()
print("Escreva o valor para C: ")
c = input()

if a > b and a > c :
    print("A é o maior número")
else :
    if b > c and b > a :
        print("B é o maior número")
    else: 
        print("C é o maior número")

