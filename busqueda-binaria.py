objetivo = int(input('Escoge un numero: '))
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