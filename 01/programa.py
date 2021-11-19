x = str("Nicolas")
y = int(18)
z = float(1.8)
espaco = "\n"

print(x)
print(type(x))
print(espaco)

print(y)
print(type(y))
print(espaco)
y = float
print(y)
print(type(y))

print(z)
print(type(z))
print(espaco)
z = complex
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
    print(len(x))

escreverNome()
print(x)

import random

print(espaco)
print(random.randrange(0, 10))

print(espaco)
for x in "mandioca":
    print(x)

print(espaco)
print("maça" in saladaFrutas)

print(espaco)
if "banana" in saladaFrutas:
    print("me vê um pouco de bananas")
else:
    print("que droga eu amo bananas")

print(espaco)
X = "testemaluco"
print(X[0:5])
print(X[5:11])
print(X[:-6])
print(X[-6:])

print(espaco)
Y = "   quero cagar! droga"
print(Y.upper())
print(Y.replace("cagar", "peidar").upper())
print(Y.strip())
print(Y.strip().split("!"))

xx = "Nicolas"
yy = int(18)
zz = float(1.8)

print(espaco)
txt = "Meu nome é {}, tenho {} anos e {} de altura\n"
print(txt.format(xx, yy, zz))

def simOuNao():
    return False

if simOuNao():
    print("SIM!\n")
else:
    print("NÂO!\n")

print(saladaFrutas)
print(len(saladaFrutas))
saladaFrutas.append("abacate")
saladaFrutas.insert(2, "laranja")

print(saladaFrutas)
print(len(saladaFrutas))

saladaFrutasMist = ("pitaya", "mirtilo", "pessego")
saladaFrutas.extend(saladaFrutasMist[:2])
print(saladaFrutas)
print(len(saladaFrutas))

saladaFrutas.remove("banana")
saladaFrutas.pop(0)
del saladaFrutas[3]
saladaFrutas.clear()
print(saladaFrutas)
print(len(saladaFrutas))