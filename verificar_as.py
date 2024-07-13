# verificar_as.py
def es_as_privado(as_numero):
    if 64512 <= as_numero <= 65534 or 4200000000 <= as_numero <= 4294967294:
        return True
    return False

as_numero = int(input("Introduce el número de AS de BGP: "))
if es_as_privado(as_numero):
    print(f"El AS {as_numero} es privado.")
else:
    print(f"El AS {as_numero} es público.")
