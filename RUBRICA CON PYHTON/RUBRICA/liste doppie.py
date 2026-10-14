lis=[4,3,4,5,6,7,8,90]
li= [1,3,4,5,6,8,7,65]
n=[]
d=[]
for i in lis:
    for t in li:
        if i % 2 == 0:
            if t % 2 == 0:
               n.append((i,t))

print(n)

for s in range(len(n)):
    for y in range(s+1,len(n)):
        if n[s]==n[y]:
            d.append(n[s])


print(d)


for i in n:
    for h in d:
        if i == h:
            n.remove(i)

print(n)