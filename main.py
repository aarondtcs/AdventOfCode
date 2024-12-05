ListA = []
ListB = []
with open('input.txt','r') as f: #open means open a file (give file given) the r takes info from file
    for line in f:
        a, b = map(int, line.split())
        ListA.append(a)
        ListB.append(b)
ListA.sort()
ListB.sort()

counting = 0

for i in range(len(ListA)):
    counting += abs(ListA[i]-ListB[i])

print(counting)

counting = 0
for i in range(len(ListA)):
    counting += ListA[i]*ListB.count(ListA[i])
print(counting)