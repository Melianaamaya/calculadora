def suma (a, b):
    resultado=a+b

    return (resultado)


resultado_suma= suma(2, 4)
print ("La suma es: " + str(resultado_suma))

def resta (a, b):
    resultado=a-b

    return (resultado)

resultado_resta= resta(20, 5)
print ("La resta es: " + str(resultado_resta))


def multiplicacion (a, b):
    resultado=a*b

    return (resultado)

resultado_multiplicacion= multiplicacion(20, 6)
print ("El resultado de la multiplicación es: " + str(resultado_multiplicacion))


def division (a, b):

    if b != 0: 
        resultado=a/b

        return (resultado)
    
resultado_division= division(50, 5)
print ("El resultado de la división es: " + str(resultado_division))


def potencia (a, b):
    resultado= a**b

    return (resultado)

resultado_potencia= potencia(10, 2)
print ("El resultado de la potencia es: " + str(resultado_potencia))


def porcentaje (a, b):
    resultado = (a*b)/100

    return (resultado)

resultado_porcentaje= porcentaje(100, 20)
print ("El porcentaje es: " + str(resultado_porcentaje))
