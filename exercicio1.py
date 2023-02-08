contaPalavras = 0
string = ['hello', 'world', 'world', 'how', 'are', 'you', 'doing', 'doing']
conta = {}
for word in string:
   if word in conta :
      conta[word] += 1
   else:
      conta[word] = 1
len(conta)

a = print(conta)

def conta_palavras_unicas():
    return a