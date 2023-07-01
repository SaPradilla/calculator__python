def restarOperación(operador):
    listaRestar = []
    num1 = int(input('Ingrese el número: '))
    listaRestar.append(num1)
    num2 = int(input('Ingrese el número: '))
    listaRestar.append(num2)
    while True:
        resta = listaRestar[0] 
        contador = 0
        pos = 0
        resta_anterior = 0
        for i in listaRestar[1:]:
            contador+=1
            if contador >= 2:
                resta_anterior = resta
                pos +=  1   
            resta -= i
        if contador >= 1: 
            if pos < 1:
                print(listaRestar[pos],'-_',listaRestar[pos+1])
            else: 
                print(resta_anterior,'-',listaRestar[pos+1])
            print('=',resta)
            print('Desea continuar restando?')
            decision = str(input('s/n: '))
            if decision == 's':
                num3 = int(input('Ingrese el número: '))
                listaRestar.append(num3) 
                continue
            else:
                break        
              
    return resta