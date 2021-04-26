import string

i = str(input())
s = string.ascii_lowercase

while 1:
    for j in range(len(i)):
        if i[0] == "_":
            if i[j].lower() in s:
                if i[0]=="_":
                    print("yes")
                    break
                else:
                    print("no")
                break
        else:
            print('no')
            break
    break