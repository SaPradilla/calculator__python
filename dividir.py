def dividirOperación(operador):
    listaDivi = []
    num1 = int(input('Ingrese el número: '))
    listaDivi.append(num1)
    num2 = int(input('Ingrese el número: '))
    listaDivi.append(num2)
    while True:
        divi_entero = listaDivi[0]
        divi_ant = 0
        contador = 0
        pos = 0
        divi_anterior = 0
        decimales = 0
        for i in listaDivi[1:]:
            
            divi_ant = divi_entero
            
            contador+=1
            
            if contador >= 2:
                divi_anterior = divi_entero
                pos +=  1     
                
            
                
            divi_entero //= i   
            
            
            fracionaria = (divi_ant / i) - divi_entero 
           
            decimales = int(fracionaria * 1000 + 0.5) / 1000


            
        if contador >= 1:
            if pos < 1:
                print(listaDivi[pos],'/',listaDivi[pos+1])
            else: 
                print(divi_anterior,'/',listaDivi[pos+1])
            print('Division entera =',divi_entero)
            print('Division con 3 decimales =',divi_entero + decimales)
            
            print('Desea continuar dividiendo?')
            decision = str(input('s/n: '))
            if decision == 's':
                num3 = int(input('Ingrese el número: '))
                listaDivi.append(num3) 
                continue
            else:
                break          
    return divi_entero, decimales