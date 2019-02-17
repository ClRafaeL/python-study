# printMenu -> camelCase : js, json
# print_menu -> snake_case : python, c
# print-menu -> kebob-case : dir, repo

def print_menu():
    print('Menu Principal')
    print('1 - Soma')
    print('2 - multiplicacao')
    print('3 - soma e multiplica')
    print('4 - tabuada')
    print('5 - loteria')
    print('0 - Sair')

def verify(opt):
    if opt == 1:
        a = convert_float(convert_dot(input('Digite um numero :')))
        b = convert_float(convert_dot(input('Digite outro numero :')))
        result = sum(a, b)
        print('Resultado da soma : ', result)

    elif opt == 2:
        a = convert_float(convert_dot(input('Digite um numero :')))
        b = convert_float(convert_dot(input('Digite outro numero :')))
        result = multiply(a, b)
        print('{} x {} = {}'.format(a, b, result))

    elif opt == 3:
        a = convert_float(convert_dot(input('Digite um numero :')))
        b = convert_float(convert_dot(input('Digite outro numero :')))
        c = convert_float(convert_dot(input('Digite mais um numero :')))
        result = sum(a, b)
        result = multiply(result, c)
        print('resultado da soma e multiplicao : ', result)

def sum(a, b):
    return a + b

def multiply(a, b):
    return a * b

def convert_int(text):
    return int(text) 

def convert_float(text):
    return float(text)

def convert_dot(text):
    resp = ""

    for i in text:
        if i == ',':
            resp += '.'
        else:
            resp += i
    return resp

def run():
    opt = 1 
    while(not opt == 0):
        print_menu()
        opt = convert_int(input('Escolha uma opcao : '))

        verify(opt)
   