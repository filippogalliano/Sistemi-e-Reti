import string
import random;

def generaListaPassword( tipo ):
    
    semplice = string.digits + string.ascii_letters #numeri
    complicata = string.digits + string.ascii_letters + string.punctuation #ascii

    while True:
        if (tipo == 'semplice'):
            lungPassword = 8
            x = semplice
        else:
            lungPassword = 20
            x = complicata
        if(tipo != 'semplice' && tipo != 'complicata'):
            break
    
    password =""

    for k in range (lungPassword):
        y = random.choise(x)
        password = password + y
