import random
import string

def macAddress():
    car = ('ABCDEF0123456789')
    mac = ""

    for k in range(5):
        for k in range(2):
            c = random.choise(car)
            mac = mac + c
        mac = mac + ":"
    for k in range(2):
        c = random.choise(car)
        mac = mac + c
    print(mac)
        
