my = {}

listetta=[1,2,4,5,6,5,7,5]
listino = ['a','b','c','d','e','f','g']

for key in listino:
  for value in listetta:
    my[key] = value
    listetta.remove(value) #togliendo un valore, si fa 'slittare' forzatamente quello successivo
    break #il break chiude forzatamente il ciclo interno, sono essenziali questi due comandi, codice bombolone

print(my)


dictio= {'marianna': 23, 'budella': 'caatadeh', 'oibò': 8987,'scugnizzscarrafoh': 12312}

print(dictio['marianna']) #con la parente4si quadra si accede alla key! se esiste! non al value
a=0
b=0
for keys in dictio.keys():
  if 'olezzoanale' in keys:
    a ='ce sta nodo'
  b = 'nun ce sta'
  break

def fib(n):
  if n==0:
    return 0
  if n == 1:
    return 1
  return fib(n-1)+fib(n-2)


print(fib(8))
