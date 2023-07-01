def multiplicarOperación(operador):
    listaMulti = []
    num1 = int(input('Ingrese el número: '))
    listaMulti.append(num1)
    num2 = int(input('Ingrese el número: '))
    listaMulti.append(num2)
    while True:
        multiplicar = listaMulti[0]
        contador = 0
        pos = 0
        multi_anterior = 0
        for i in listaMulti[1:]:
            
            contador+=1
            
            if contador >= 2:
                multi_anterior = multiplicar
                pos +=  1     
            
            multiplicar *= i 
            

            
        if contador >= 1:
            if pos < 1:
                print(listaMulti[pos],'*',listaMulti[pos+1])
            else: 
                print(multi_anterior,'*',listaMulti[pos+1])
            print('=',multiplicar)
            print('Desea continuar multiplicando?')
            decision = str(input('s/n: '))
            if decision == 's':
                num3 = int(input('Ingrese el número: '))
                listaMulti.append(num3) 
                continue
            else:
                break          
    return multiplicar