import random

def randomize(n):
    dic ={}
    for i in range(n):
        r = random.random()
        if r not in dic.keys():
            dic[r]=r
    print(dic)

randomize(4)



