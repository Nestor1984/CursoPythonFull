# 3- Recorrer una lista de forma recursiva

def mostrarListaRec(lista, index):
    if index != len(lista):
        print(lista[index])
        mostrarListaRec(lista, index + 1)
        
lista = [1, 2, 3, 4, 5]
mostrarListaRec(lista, 0)
"""
Salida:
1
2
3
4
5
"""