def factarial(n):
    """Calcula el factorial de n.
       n int >0
       returns n!
    """
    print(n)
    if n == 1:
        return 1

    return n * factarial(n -1)

n= int(input('Escribe un entero: '))
print(factarial(n))