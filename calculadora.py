print("Bienvenido a mi primera calculadora dame tus numeros para empezar")
dato1 = int(input('Numero 1:'))  
dato2 = int(input('Numero 2:'))
calculadora = int(input('Que quieres hacer con los datos: 1) sumar, 2) restar, 3) multiplicar, 4) dividir:'))
suma = 0

if 1 <= calculadora <= 4:
    if calculadora == 1:
        suma = dato1 + dato2
        print(suma)
    elif calculadora == 2:
        suma = dato1 - dato2
        print(suma)
    elif calculadora == 3:
        suma = dato1 * dato2
        print(suma)
    elif calculadora == 4:
        if dato2 == 0:
            print('error no se puede dividir')
        else:
            suma = dato1 / dato2
            print(suma)
    while True:
        k = input('Quieres añadir otro, si o no?: ')
        
        if k == 'si':
            z = int(input('Que numero quieres agregar?: '))
            i = int(input('Que quieres hacer con este nuevo numero 1) sumar, 2) restar, 3) multiplicar o 4) dividir?: '))
            if 1 <= i <= 4:
                if i == 1:
                    suma = suma + z
                    print(suma)
                elif i == 2:
                    suma = suma - z
                    print(suma)
                elif i == 3:
                    suma = suma * z
                    print(suma)
                elif i == 4:
                    if z == 0:
                        print('no es divisible por 0')
                        print(suma)
                        break
                    else:
                        suma = suma / z
                        print(suma)
            
        if k == 'no':
            print(suma)
            break
    
else:   
    print('opcion invalida')