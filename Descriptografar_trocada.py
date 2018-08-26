def descriptografar_cabralI(texto):
    if texto.isdigit():
        return int(texto)/2
    else:
        RESULT = 0
        resposta = ''
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        texto = texto.upper()
        NUM = 5
        resposta = resposta[::-1]
        for i in texto:
            if i in alfabeto:
                RESULT = RESULT + alfabeto.find(i) - NUM
                resposta += alfabeto[RESULT]
                RESULT = 0
        resposta = resposta.rjust(-15)
        resposta = resposta[::-1]
        return resposta
entrar_dado = input()
print(descriptografar_cabralI(entrar_dado))