import random as r

j = int(input("small"))
i = int(input("big"))
l = int(input("Don't bigger than 10"))
m = int(input("Swap"))

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
    count += 1
    if j == count:
        count = 0
        break

print(arr)
count = 0
c = 0
while 1:
    while 1:
        if arr[count][c] > l:
            arr[count][c] = m

        c+=1
        if c >= i:
            c = 0
            break
    count+=1
    if count == j:
        count = 0
        break


print(arr)