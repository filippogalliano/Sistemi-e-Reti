import string

def criptare(stringa):
    x = ""
    for k in stringa:
        k = ord(k) + 15
        k = chr(k)
        k = x + k
    print(f"Stringa criptata: {x}")

def decript(stringa):
    x = ""
    for k in stringa:
        k = ord(k) - 15
        k = chr(k)
        x = x + k
    print(f"Stringa decriptata: {temp}")