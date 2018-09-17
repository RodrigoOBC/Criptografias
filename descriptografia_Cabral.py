def Descriptografia_cabral(palavra,num):
    resultado = ''
    for letra in palavra:
        if letra == 'z':
            resultado += 'a'
        elif letra == 'f':
            resultado += 'e'
        elif letra == f'{num}':
            resultado += 'i'
        elif letra == f'{num+1}':
            resultado += 'o'
        elif letra == f'{num-1}':
            resultado += 'u'
        else:
            resultado += letra
    return resultado[::-1]
