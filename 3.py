n = int(input("Number"))
l = int(input("from"))
k = int(input("to"))

while l !=k:
    m = n*l
    print("{0}*{1}={2}".format(n, l, m))
    l +=1