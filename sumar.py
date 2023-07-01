def sumarOperación(operador):
    listaSumar = []
    while True:
        contador = 0
        suma = 0
        suma_anterior = 0
        pos = 0
        for i in range(len(listaSumar)):
            
            suma_anterior = suma
            
            suma += listaSumar[i] 
            
            contador+=1
            if contador > 2:
                pos +=  1     
        if contador == 0:
            num1 = int(input('Ingrese el número: '))
            listaSumar.append(num1)
            num2 = int(input('Ingrese el número: '))
            listaSumar.append(num2)
        if contador > 1:
            if pos == 0:
                print(listaSumar[pos],'+',listaSumar[i])
            elif pos >= 1: 
                print(suma_anterior,'+',listaSumar[pos+1])
            print('=',suma)
            print('Desea continuar sumando?')
            decision = str(input('s/n: '))
            if decision == 's':
                num3 = int(input('Ingrese el número: '))
                listaSumar.append(num3) 
                continue
            else:
                break          
    return suma