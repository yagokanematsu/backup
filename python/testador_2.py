a = [x for x in input().lower()]
b = []
cont = 0
for x in a:
    if cont == 0 or (a[a.index(x)-1].isspace() and not a[a.index(x)+2].isspace()):
        b.append(x.upper())
    else:
        b.append(x)
    cont+=1
b = ''.join(b)
print(b)