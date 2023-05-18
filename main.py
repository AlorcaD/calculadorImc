# Calculadora de IMC
# IMC = Peso / (Altura x Altura)
# < 19: delgadez
# entre 20 y 25: normal
# entre 26 y 30: sobrepeso
# > de 30: obesidad


def calcularIMC(parametro):
    print('el valor del parametro es: ' + parametro)

    calcularIMC('1')

peso = float(input('ingrese su peso en kg'))
alturaEnCm = int(input('ingrese su altura en cm'))
alturaEnMetros = alturaEnCm / 100
imc = peso / (alturaEnMetros * alturaEnMetros)

print('su IMC es de ' + str(imc))


if imc < 20:
    print('estado de delgadez')
if imc >= 20 and imc < 26:
    print('peso normal')
if imc >= 26 and imc < 30:
    print('sobre peso')
if imc >= 30:
        print('obesidad')