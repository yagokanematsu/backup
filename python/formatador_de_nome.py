a = [x for x in input().lower()]
final = []
cont = 0
for x in a:
    if cont == 0 or a[cont-1].isspace():
        final.append(x.upper())
    else:
        final.append(x)
    cont+=1
final = ''.join(final)
final = final.replace('  ',' ')
print(final)


