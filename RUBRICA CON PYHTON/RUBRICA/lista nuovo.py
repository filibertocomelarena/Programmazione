stringoza ='pepfejfhshfgsdufgbqudyf'

def smezza(string, max_width):
    l=[]
    for i in range(0, len(string), max_width):
        l.append(string[i:i + max_width]) #slicing da i a i, ma aggiungendo il passo, vado da i a i+4 in pratica
        #appendo alla lista l, che poi joino con l'accapo
    return "\n".join(l)








print(smezza(stringoza,4))
