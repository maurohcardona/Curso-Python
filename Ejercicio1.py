def suma(a, b):
    resultado = int(a) + int(b)
    return f'El resultado es: {resultado}'


def resta(a, b):
    resultado = int(a) - int(b)
    return f'El resultado es: {resultado}'


while True:
    operacion = int(input("Elija 1 para sumar o 2 para restar: "))
    if operacion == 1:
        a = input("Elija el primer valor: ")
        b = input("Elija el segundo valor: ")
        print(suma(a, b))
        break

    elif operacion == 2:
        a = input("Elija el primer valor")
        b = input("Elija el segundo valor")
        print(resta(a, b))
        break

    else:
        print("La opcion indicada no es valida")
