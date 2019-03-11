lista = [50, 6, 3, 500, 4, 8, 2, 1, 6, 10, 11, 254, 27, 102]

def bubble_sort(lista):

    for inicial in range(0, len(lista) -1):
        mudou = False
        print('loop')
        for atual in range(0, len(lista) -1):
            if lista[atual] > lista[atual + 1]:
                lista[atual], lista[atual + 1] = lista[atual + 1], lista[atual]
                mudou = True

        if not mudou:
            break   

bubble_sort(lista)

print(lista)  