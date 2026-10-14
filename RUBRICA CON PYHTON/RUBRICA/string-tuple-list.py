a = input().split(' ')
b = input().split(' ')

listaa = [ ]


for i in a:
    for t in b:
        listaa.append(i)
        listaa.append(t)
a = []

for i in range(0, len(listaa), 2):
    a.append((int(listaa[i]), int(listaa[i+1])))


string = str(a)

char_to_remove = "[]"

new_string = string
for character in char_to_remove:
  new_string = new_string.replace(character, "")

print(new_string.replace('), (', ') ('))