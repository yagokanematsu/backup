# print("Olá, seja bem vindo ao nosso codificador python da cifra Rail Fence")
# mensagem = input("Escreva a mensagem que você quer que seja codificada: ")
# chave = int(input("Escreva sua chave numérica: "))
# padrao = list(range(chave))+list(range(chave-2, 0, -1))
# print(padrao)

# matriz = [[] for r in range(chave)]

# [matriz[padrao[r%len(padrao)]].append(mensagem[r]) for r in range (len(mensagem))]
# matriz = ''.join([''.join(r) for r in matriz])

# print(matriz)
# print(mensagem)

def rail_fence(mensagem, chave):
    padrao = list(range(chave[0])) + list(range(chave[0] - 2, 0, -1))
    matriz = [[] for _ in range(chave[0])]
    for i in range(len(mensagem)):
        linha_atual = padrao[i % len(padrao)]
        matriz[linha_atual].append(mensagem[i])
    mensagem_codificada = ''.join([''.join(linha) for linha in matriz])
    return mensagem_codificada
print("Olá! Bem-vindo ao nosso codificador Python usando a cifra Rail Fence.")
mensagem = input("Escreva a mensagem que você deseja codificar: ")
chave = list(map(int, input("Sua chave numérica: ").split()))
mensagem_criptografada = rail_fence(mensagem, chave)
print(f"A mensagem codificada é: {mensagem_criptografada}")
print(f"A mensagem original era: {mensagem}")


# def rail_fence_decriptador(mensagem, chave):
#     padrao = list(range(chave)) + list(range(chave - 2, 0, -1))
#     print(padrao)
#     matriz = [[] for _ in range(chave)]
#     contagem_linhas = [0] * chave
#     for i in range(len(mensagem)):
#         linha_atual = padrao[i % len(padrao)]
#         contagem_linhas[linha_atual] += 1
#     print(contagem_linhas)
#     indice = 0
#     for i in range(chave):
#         matriz[i] = list(mensagem[indice:indice + contagem_linhas[i]])
#         indice += contagem_linhas[i]
#     mensagem_original = []
#     for i in range(len(mensagem)):
#         linha_atual = padrao[i % len(padrao)]
#         mensagem_original.append(matriz[linha_atual].pop(0))
#         print(mensagem_original)
#     return ''.join(mensagem_original)

