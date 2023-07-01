from sumar import sumarOperación
from restar import restarOperación
from multiplicar import multiplicarOperación
from dividir import dividirOperación
def main():
    
    # print('----------------------------------------------')
    # print('|****| ¿Que operacion desea realizar? |******|')
    # print('|***********| Sumar       = [+] |************|')
    # print('|***********| Restar      = [-] |************|')
    # print('|***********| Multiplicar = [*] |************|')
    # print('|***********| Dividir     = [/] |************|')
    # print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    
    print('----------------------------------------------')
    print('|*****| '+'\033[31m' + '¿Que operacion desea realizar?'+ '\033[0m'+ '|******|')
    print('|***********| Sumar       = ' + '\033[31m' + '[+]' + '\033[0m'+ ' |************|')
    print('|***********| Restar      = ' + '\033[31m' + '[-]' + '\033[0m'+ ' |************|')
    print('|***********| Multiplicar = ' + '\033[31m' + '[*]' + '\033[0m'+ ' |************|')
    print('|***********| Dividir     = ' + '\033[31m' + '[/]' + '\033[0m'+ ' |************|')
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    
    
    # print('Potencia = [**]')
    # print('Modulacion == [%]')
    try:
        # cantidad = int(input('Cuantos números desea operar?: '))
        
        operador = str(input('Digite el operador: '))
        if operador == '+':
            sumar = sumarOperación(operador)
            print('la suma total es: ',sumar)
        if operador == '-':
            restar = restarOperación(operador)
            print('La resta total es: ',restar)
    
            
        if operador == '*':
            multiplicacion = multiplicarOperación(operador)   
            print('La multiplicacion total es: ',multiplicacion) 
            
        if operador == '/':
            division,decimal = dividirOperación(operador)
            print('La division total es: ',division)
            print('La división que decimales es: ', division+decimal)
            
    except ValueError:
        print('Ningun signo de operador coincide..')
        
    
if __name__ == '__main__':
    main()