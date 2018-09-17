def criptografia_cabral(palavra,num):
    resultado = ''
    for letra in palavra:
        if letra == 'a':
            resultado += 'z'
        elif letra == 'e':
            resultado += 'f'
        elif letra == 'i':
            resultado += f'{num}'
        elif letra == 'o':
            resultado += f'{num+1}'
        elif letra == 'u':
            resultado += f'{num-1}'
        else:
            resultado += letra
    return resultado[::-1]

