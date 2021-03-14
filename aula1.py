ALFABETO = 'abcdefghijklmnopqrstuvwxyz'

def criptografar(palavra):
  palavracriptografada = ""
  print("Vou criptografar a palavra ", palavra)
  for posicaoletra in range(0,len(palavra)):
    letra = palavra[posicaoletra:posicaoletra+1]
    posicaoalfa = ALFABETO.index(letra)
    if(posicaoalfa>23):
      posicaoalfa=posicaoalfa-26 
    palavracriptografada=palavracriptografada+ALFABETO[posicaoalfa+3:posicaoalfa+4]
  print("A palavra ",palavra," criptografada é: ",palavracriptografada)
  return (palavracriptografada)
    
def descriptografar(palavra):
  palavracriptografada = ""
  print("Vou descriptografar a palavra: ", palavra)
  for posicaoletra in range(0,len(palavra)):
    letra = palavra[posicaoletra:posicaoletra+1]
    posicaoalfa = ALFABETO.index(letra)
    if(posicaoalfa<3):
      posicaoalfa=posicaoalfa+26 
    palavracriptografada=palavracriptografada+ALFABETO[posicaoalfa-3:posicaoalfa-2]
  print("A palavra ",palavra," descriptografada é ",palavracriptografada)

PALAVRA = input("Digite a palavra: ")

palacri = criptografar(PALAVRA)

descriptografar(palacri)
