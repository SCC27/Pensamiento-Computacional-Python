
def enumeracion(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raiz cuadrada exacta')
    

def aproximacion (objetivo):
    epsilon = 0.0001
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo )>= epsilon:
        print(f'No se encontro la raiz cuadrada del objetivo')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def busqueda_binaria (objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.2, objetivo)
    respuesta = (alto + bajo)

    while abs(respuesta** 2 - objetivo) >= epsilon:
        print(f'bajp={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else: 
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada del {objetivo} es {respuesta}')

menu = """
Algoritmos para encontrar la reiz cuadrada de un numero

1 - Enumeracion
2 - Aproximacion
3 - Busqueda binaria

Elige una opcion:
"""
opcion = int(input(menu))
numero = int(input('Escoge un numero: '))

if opcion == 1:
    enumeracion(numero)

elif opcion == 2:
    aproximacion(numero)
elif opcion ==3:
    busqueda_binaria(numero)
else:
    print("Elige una opcion correcta porfavor")

