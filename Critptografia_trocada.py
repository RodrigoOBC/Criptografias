def criptografar_cabralI(texto):
    if texto.isdigit():
        return int(texto)/2
    else:
        RESULT = 0
        resposta = ''
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        texto = texto.upper()
        NUM = 5
        for i in texto:
            if i in alfabeto:
                RESULT = RESULT + alfabeto.find(i) + NUM
                resposta += alfabeto[RESULT]
                RESULT = 0
        resposta = resposta.rjust(15)
        resposta = resposta[::-1]
        return resposta
entrar_dado = input()
print(criptografar_cabralI(entrar_dado))





N = int(input())
x = 0
RESULT = int()
resposta = ''
while (x < N):
  alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  palavra = input()
  palavra = palavra.upper()
  num = int(input())
  for i in palavra:
    if i in alfabeto:
      RESULT = RESULT + alfabeto.find(i) + num
      resposta += alfabeto[RESULT]
      RESULT = 0
  print(resposta)
  resposta = ''
  x = x +  1