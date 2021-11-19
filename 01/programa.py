x = str("Nicolas")
y = int(18)
z = float(1.8)
espaco = "\n"

print(x)
print(type(x))

print(y)
print(type(y))

print(z)
print(type(z))

i, l, j = "picles", "tomate", "cenoura"
print(espaco)
print(i)
print(l)
print(j)

saladaFrutas = ["mamão", "banana", "maça"]
i, l, j = saladaFrutas
print(espaco)
print(i)
print(l)
print(j)

print(espaco)

def escreverNome():
    global x
    x = "Maribel"
    print(x)

escreverNome()
print(x)