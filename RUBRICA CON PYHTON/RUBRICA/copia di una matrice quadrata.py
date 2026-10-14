'''copia di una matrice quadrata'''

mA=[ [2,7], [1,0] ]
mB=[ [1,2], [0,4] ]
mC=[ [1,8], [0,5] ]

def copia(m):
   n=len(m)
   mm=[]
   for r in range(n): #crea 2 liste di nome riga, per la lunghezza di n
       riga=[] #mA ha lunghezza pari a 2
       for c in range(n): #appende dentro riga, che sono 2 come visto sopra,
           riga.append(m[r][c]) #mette in riga, m1 e c1
           print(r)
       mm.append(riga)
   return mm


print(copia(mA))