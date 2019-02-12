array = ['r', 'a', 'f', 'a']

array2 = "rafael"

text = "1.5"

def convert(text):
    resp = ""

    for i in text:
        if i == ',':
            resp += '.'
        else:
            resp += i
    return resp

print(convert("1,5"))
