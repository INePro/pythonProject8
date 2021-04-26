import random as r

i = int(input("big"))
j = int(input("small"))

arr = []
count = 0
c = 0
while j:
    ar = []
    while 1:
        ar.append(r.randint(0,10))
        c+=1
        if i==c:
            c = 0
            break

    arr.append(ar)
    j-=1

print(arr)

an = 0

for i in arr:
    for j in i:
        if j % 2 == 0:
            an += j

print(an)