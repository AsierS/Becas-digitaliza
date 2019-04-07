def calculo():
    operacion = input('''
Elige la operación que quieras: + para sumar, - para restar, * para multiplicar, / para dividir o ** para hacer exponenciales''')

    num1 = float(input('Introduce el primer número: '))
    num2 = float(input('Introduce el segundo número: '))

    if operacion == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)

    elif operacion == '-':
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)

    elif operacion == '*':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)

    elif operacion == '/':
        print('{} / {} = '.format(num1, num2))
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print("No se puede dividir entre cero.")
            repetir()
        
    elif operacion == '**':
        print('{} ** {} = '.format(num1, num2))
        print(num1 ** num2)

    else:
        print('No se ha asignado el operador correctamente.')


    repetir()

def repetir():
    calc_again = input('''¿Quieres hacer otro cálculo? Introduce S si quieres. Introduce N si no quiers.''')

    if calc_again.upper() == 'S':
        calculo()
    elif calc_again.upper() == 'N':
        print('Has terminado de operar.')
        wait = input('Pulsa enter para salir.')
    else:
        repetir()
        
calculo()
