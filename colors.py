# Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

# Estilos
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'

# Salida en consola
print(RED + 'Este texto será de color rojo' + RESET)
print(GREEN + 'Este texto será de color verde' + RESET)
print(YELLOW + 'Este texto será de color amarillo' + RESET)
print(BLUE + 'Este texto será de color azul' + RESET)

print('\033[34m' + 'Este texto será de color azul' + '\033[0m')

print(MAGENTA + 'Este texto será de color magenta' + RESET)
print(CYAN + 'Este texto será de color cyan' + RESET)
print(WHITE + 'Este texto será de color blanco' + RESET)

# Salida en consola con estilo
print(BOLD + 'Este texto será en negrita' + RESET)
print(UNDERLINE + 'Este texto será subrayado' + RESET)
