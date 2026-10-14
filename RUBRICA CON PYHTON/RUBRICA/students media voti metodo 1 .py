number_of_students = int(input('insert the students number: '))

student=[]
votes= []
k=[]
for i in range(number_of_students):
    students_name = input('insert the names: ')
    student.append(students_name)
for d in student:
    for t in range(3):
        votes.append(input('insert the ' + str(t) + ' vote of the '+ str(d) + ' student: '))
voti_studenti = [votes[i:i+3] for i in range(0, len(votes), 3)]

print(student)
print(voti_studenti)

result = [None]*(len(voti_studenti)+len(student))
result[1::2] = voti_studenti  #Lst[ Initial : End : IndexJump ]
result[0::2] = student

dictionary = dict(zip(student, voti_studenti)) #once we have two lists, we can use dict-zip

print(dictionary)



