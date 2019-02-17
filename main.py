from study import convert_int, print_menu, verify as verify_study
from random import shuffle

#-----------------------------------------DISSECANDOVARIAVEL-----------------------------

def dissect():
    a = input('Digite algo: ')

    print('o tipo primitivo desse dado: ', a.type(a))
    print('contem somente espaço? ', a.isspace())
    print('é um Numero? ', a.isnumeric())
    print('é alfabético? ', a.isalph())
    print('é alphanumerico? ', a.isalnum())
    print('esta em maiuscula? ', a.isupper())
    print('esta em minuscula? ', a.islower())
    print('esta capitalizada? ', a.istitle())

#-----------------------------------------TABUADA--------------------------------------

def table(): 
    a = int(convert_int(input('digite um numero para montar a tabuada: ')))

    for i in range(11):
        print('{}  x  {} = {} ' .format(i, a, i*a))

#----------------------------------------SORTEIONALISTA---------------------------------

def lottery(array_names):
    shuffle(array_names)
    winner = array_names[0]
    print('o ganhador e: ', winner)

def get_names():
    cond = 's'
    array_names = ['claudio', 'rafael', 'Lucas', 'joao', 'maria']

    while (not cond != 's' or cond == 'S'):

        a = input('digite um nome para o sorteio: ')
        array_names.append(a)
        print('----------------------')
        cond = input('deseja acrescentar mais um nome? S/N')

    return array_names

def run():
    opt = 1

    while(not opt == 0):
        print_menu()
        opt = convert_int(input('escolha a opçao: '))
        if (opt <= 3 and opt >= 1):
            verify_study(opt)
        else:
            verify(opt)

def verify(opt):
    if (opt == 4):
        table()
    elif (opt == 5):
        arr = get_names()
        lottery(arr)

run()
