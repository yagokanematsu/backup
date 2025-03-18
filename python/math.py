import math

print("Relações métricas no triângulo Rertângulo: Relação entre altura e as projeções")
print("Calcular h: 1\nCalcular m: 2\nCalcular n: 3\nFechar menu: 4")
r = 0
while r !=4:
    r = float(input())
    if r == 1:
        m = float(input("Digite o valor de m: "))
        n = float(input("Digite o valor de n: "))
        s = m*n
        s = math.sqrt(s)
        print("O valor de h é igual a {:.2f}".format(s))
    elif r == 2:
        h = float(input("Digite o valor de h: "))
        n = float(input("Digite o valor de n: "))
        s = h**2
        s = s/n
        print("O valor de m é igual a {:.2f}".format(s))
    elif r == 3:
        h = float(input("Digite o valor de h: "))
        m = float(input("Digite o valor de m: "))
        s = h**2
        s = s/m
        print("O valor de n é igual {:.2f}".format(s))
    elif r == 4:
        break
    else:
      print("Entrada inválida")


