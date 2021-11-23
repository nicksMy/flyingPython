"""
aqui será feito um sistema de inventario
semelhante ao do jogo minecraft
"""

itemConsumivel = ("banana", "mirtilo", "cura", "mana", "espelho", "???")
itemDescricao = ("", "", "", "")
itemEquipavel = ("", "", "", "")

def mostrarInv(item01, item02, item03, item04):
    print("\n               ESSE É SEU INVENTÁRIO, USE-O COM SABEDORIA!\n")

    print("I-----------------I-----------------I-----------------I-----------------I")
    print("|                 |                 |                 |                 |")
    inventario = "| {0:^15} | {1:^15} | {2:^15} | {3:^15} |"
    print(inventario.format(item01, item02, item03, item04))
    print("|                 |                 |                 |                 |")
    print("I-----------------I-----------------I-----------------I-----------------I")

mostrarInv(itemConsumivel[0], itemConsumivel[1], itemConsumivel[2], itemConsumivel[3])