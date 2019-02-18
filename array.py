#--------------------------------------trocar','por'.'---------------------------------
text = "1.5"

def convert(text):
    resp = ""

    for i in text:
        if i == ',':
            resp += '.'
        else:
            resp += i
    return resp

#print(convert("1,5"))

#----------------------------------manipular-array-tuples-dicionarios-----------------

my_array = ['c', 'l', 'a', 'Claudio', 'Rafael', 'Joao', 'Maria', '10', '7']
my_tuples = ('c', 'l', 'a', 'Claudio', 'Rafael', 'Joao', 'Maria', '10', '7')
my_dicio = {'claudio':'rafael', 1:'c', 2:'l', 3:True, 4:'Claudio', 5:'Rafael', 6:'Joao', 7:'Maria'}

print('')

print(my_array)
print(my_tuples)
print(my_dicio)

print('')

print(my_array[4])
print(my_tuples[4])
print(my_dicio[5])

print('')

print(my_array[3:5])
print(my_tuples[:])
print(my_dicio['claudio'])

print('')

cl = my_array[3:5]
print(cl[0], cl[1])

print('')

print(my_dicio[3])

print(type(my_dicio[3]))

print(my_array[0::2])

for chave in my_dicio:
    print(chave, my_dicio[chave])

print('')

print(my_array[7:2:-1])

nums = [i*2 for i in range(10)]
print(nums)

print('')

evens = [i ** 2 for i in range(10) if i ** 2 % 2 ==0]
print(evens)

print('')

evens = [i for i in range(0, 10, 2)]

for i in evens:
    if i % 2 == 0:
        print(i) 