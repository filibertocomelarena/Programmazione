n = int(input()) #inserire il numero studenti
student_marks = {} #dizionario inizializzato
for _ in range(n): #ciclo sul numero di studenti
    name, *line = input().split() #name prende un valore solo, ma line con l'* può prendere valori multipli, per questo si splitta
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
l =student_marks[query_name]
s=sum(l)/len(l)
print('%.2f'%s)


'''line 1:Getting input for n(number of students). 
line 2:Initialization of dictonary. 
line 3:for loop to get input for n number of students. 
line 4:"name" can accept only one value but " * line " can accept multiple inputs. 
line 5: "Score" stores marks(which is stored in line variable) in a list. 
line 6:In our dictionary "name" is the key and "score " is the value. Dictionary can be access using "key" Eg: student_marks={Harsh : [25 26.5 28], Anurag : [26 28 30]} so we assign "score" to "name"(which is the key in our dict). 
line 7:Get name of the student to whom u want to find average mark line 
8:stores the marks of the required student in variable "L" (which is a list).
print('%.2f'%s)'''