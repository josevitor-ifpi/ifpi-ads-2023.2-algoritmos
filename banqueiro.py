# # def banqueiro(recursos_disponiveis, matriz_alocacao, matriz_requisicoes):
# #     num_processos = len(matriz_alocacao)
# #     num_recursos = len(recursos_disponiveis)

# #     processos_marcados = [False] * num_processos

# #     while True:
# #         processo_encontrado = False

# #         for i in range(num_processos):
# #             if not processos_marcados[i]:
# #                 recursos_suficientes = True

# #                 for j in range(num_recursos):
# #                     if matriz_requisicoes[i][j] > recursos_disponiveis[j]:
# #                         recursos_suficientes = False
# #                         break

# #                 if recursos_suficientes:
# #                     # Adiciona a i-ésima linha de C a A
# #                     for j in range(num_recursos):
# #                         recursos_disponiveis[j] += matriz_alocacao[i][j]

# #                     # Marca o processo como alocado
# #                     processos_marcados[i] = True

# #                     # Indica que um processo foi encontrado
# #                     processo_encontrado = True

# #                     # Sai do loop interno
# #                     break

# #         # Se nenhum processo for encontrado, termina o algoritmo
# #         if not processo_encontrado:
# #             break

# #     # Verifica se todos os processos foram marcados
# #     deadlock = any(not marcado for marcado in processos_marcados)

# #     return deadlock


# # # Exemplo de uso com os dados fornecidos
# # recursos_disponiveis = [2, 1, 0, 0]
# # matriz_alocacao = [
# #     [0, 0, 1, 0],
# #     [2, 0, 0, 1],
# #     [0, 1, 2, 0]
# # ]
# # matriz_requisicoes = [
# #     [2, 0, 0, 1],
# #     [1, 0, 1, 0],
# #     [2, 1, 0, 0]
# # ]

# # deadlock = banqueiro(recursos_disponiveis, matriz_alocacao, matriz_requisicoes)

# # if deadlock:
# #     print("Há deadlock!")
# # else:
# #     print("Não há deadlock.")

# def algoritmo_banqueiro(recursos_existentes, recursos_disponiveis, matriz_alocacao, matriz_requisicoes):
#     num_processos = len(matriz_alocacao)
#     num_recursos = len(recursos_existentes)

#     processos_marcados = [False] * num_processos

#     while True:
#         processo_encontrado = False

#         for i in range(num_processos):
#             if not processos_marcados[i]:
#                 recursos_suficientes = all(matriz_requisicoes[i][j] <= recursos_disponiveis[j] for j in range(num_recursos))

#                 if recursos_suficientes:
#                     # Adiciona a i-ésima linha de C a A
#                     for j in range(num_recursos):
#                         recursos_disponiveis[j] += matriz_alocacao[i][j]

#                     # Marca o processo como alocado
#                     processos_marcados[i] = True

#                     # Indica que um processo foi encontrado
#                     processo_encontrado = True

#                     # Sai do loop interno
#                     break

#         # Se nenhum processo for encontrado, termina o algoritmo
#         if not processo_encontrado:
#             break

#     # Verifica se todos os processos foram marcados
#     deadlock = any(not marcado for marcado in processos_marcados)

#     return deadlock


# # Solicita que o usuário insira os recursos existentes
# recursos_existentes = [int(x) for x in input("Digite os recursos existentes (separados por espaço): ").split()]

# # Solicita que o usuário insira os recursos disponíveis
# recursos_disponiveis = [int(x) for x in input("Digite os recursos disponíveis (separados por espaço): ").split()]

# # Matriz de alocação atual
# matriz_alocacao = []
# print("Digite a matriz de alocação atual:")
# for _ in range(len(recursos_existentes)):
#     linha = [int(x) for x in input().split()]
#     matriz_alocacao.append(linha)

# # Matriz de requisições
# matriz_requisicoes = []
# print("Digite a matriz de requisições:")
# for _ in range(len(recursos_existentes)):
#     linha = [int(x) for x in input().split()]
#     matriz_requisicoes.append(linha)

# # Executa o algoritmo do banqueiro
# deadlock = algoritmo_banqueiro(recursos_existentes, recursos_disponiveis, matriz_alocacao, matriz_requisicoes)

# # Exibe o resultado
# if deadlock:
#     print("Há deadlock!")
# else:
#     print("Não há deadlock.")

def algoritmo_banqueiro(recursos_existentes, recursos_disponiveis, matriz_alocacao, matriz_requisicoes):
    num_processos = len(matriz_alocacao)
    num_recursos = len(recursos_existentes)

    processos_marcados = [False] * num_processos

    while True:
        processo_encontrado = False

        for i in range(num_processos):
            if not processos_marcados[i]:
                recursos_suficientes = all(matriz_requisicoes[i][j] <= recursos_disponiveis[j] for j in range(num_recursos))

                if recursos_suficientes:
                    # Adiciona a i-ésima linha de C a A
                    for j in range(num_recursos):
                        recursos_disponiveis[j] += matriz_alocacao[i][j]

                    # Marca o processo como alocado
                    processos_marcados[i] = True

                    # Indica que um processo foi encontrado
                    processo_encontrado = True

                    # Sai do loop interno
                    break

        # Se nenhum processo for encontrado, termina o algoritmo
        if not processo_encontrado:
            break

    # Verifica se todos os processos foram marcados
    deadlock = any(not marcado for marcado in processos_marcados)

    return deadlock


# Solicita que o usuário insira os recursos existentes
recursos_existentes = [int(x) for x in input("Digite os recursos existentes (separados por espaço): ").split()]

# Solicita que o usuário insira os recursos disponíveis
recursos_disponiveis = [int(x) for x in input("Digite os recursos disponíveis (separados por espaço): ").split()]

# Matriz de alocação atual
matriz_alocacao = [
    [0, 0, 1, 0],
    [2, 0, 0, 1],
    [0, 1, 2, 0]
]

# Matriz de requisições
matriz_requisicoes = [
    [2, 0, 0, 1],
    [1, 0, 1, 0],
    [2, 1, 0, 1] #2 1 0 1 há deadlock, 2 1 0 0 não há deadlock
]

# Executa o algoritmo do banqueiro
deadlock = algoritmo_banqueiro(recursos_existentes, recursos_disponiveis, matriz_alocacao, matriz_requisicoes)

# Exibe o resultado
if deadlock:
    print("Há deadlock!")
else:
    print("Não há deadlock.")
