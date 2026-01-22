import random
scores = []
for i in range(5):
    scores.append(random.randint(i,10))
print(scores)

caps = []
for letter in "Henry Honey":
	if letter.isupper():
		caps.append(letter)
print(caps)

list_of_lists = [['a','b','c'], ['d','e','f'], ['g','h','i']]
flat = []
flat1 = []

for sub_list in list_of_lists:      # 1. Bucle Externo
    for item in sub_list:          # 2. Bucle Interno
        flat.append(item)          # 3. Acción
print(flat)

flat1= [item for sublist in list_of_lists for item in sublist]

flat2= [ifinal for sub_i in list_of_lists for ifinal in sub_i]

print(flat1)
print(flat2)