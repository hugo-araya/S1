# Autor: Hugo Araya Carrasco
def lee_datos(nombre):
    ent = open(nombre)
    cantidad = int(ent.readline().rstrip('\n'))
    linea1 = ent.readline().rstrip('\n').split(' ')
    linea2 = ent.readline().rstrip('\n').split(' ')
    linea3 = ent.readline().rstrip('\n').split(' ')
    ent.close()
    digitos_braille = []
    i = 0
    while i < cantidad:
        digi = linea1[i] + linea2[i] + linea3[i]
        digitos_braille.append(digi)
        i = i + 1
    return digitos_braille

def traduce(digitos_braille):
    numeros = ['.***..', '*.....', '*.*...', '**....', '**.*..', '*..*..', '***...', '****..','*.**..', '.**...']
    nro_str = ''
    for digito in digitos_braille:
        nro = numeros.index(digito)
        nro_str = nro_str + str(nro)
    return nro_str
    
def genera_salida(nombre, digitos_arabigos):
    sal = open(nombre, 'w')
    sal.write(digitos_arabigos+'\n')
    sal.close()

if __name__ == '__main__':
    digitos_braille = lee_datos('mensaje_in.txt')
    digitos_arabigos = traduce(digitos_braille)
    genera_salida('mensaje_out.txt', digitos_arabigos)
