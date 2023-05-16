frase = "Não vai da não."
conta_palavra = 0
palavra = ""
conta = []
conta_unica = []

def conta_palavras_unicas(fr):
  global conta_palavra
  global palavra
  global conta
  global conta_unica

  fr = fr.lower()
  for i in fr:
    if i == " " or i == "," or i == "." or i == "!" or i == "?" or i == ";":
      conta.append(palavra)
      palavra = ""
    else:
      palavra += i
  
  for i in conta:
    word = 0
    for j in conta:
      if j == i:
        word += 1
    if word == 1:
      conta_unica.append(i)

  value = len(conta_unica)

  return value

a = conta_palavras_unicas(frase)
print(a)