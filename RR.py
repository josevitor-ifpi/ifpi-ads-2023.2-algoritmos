import time

tarefas = [
    {"nome": "P1", "ingresso": 5, "duracao": 10},
    {"nome": "P2", "ingresso": 15, "duracao": 30},
    {"nome": "P3", "ingresso": 10, "duracao": 20},
    {"nome": "P4", "ingresso": 0, "duracao": 40}
]

quantum = 15
troca_contexto = 4

tempo_atual = 0
tempos_espera = []
tempos_vida = []
tempos_execucao = []
tempos_ingresso = []

while tarefas:
    tarefa_atual = tarefas.pop(0)

    inicio_execucao = max(tarefa_atual["ingresso"], tempo_atual)
    duracao_execucao = min(tarefa_atual["duracao"], quantum)

    tempos_ingresso.append((tarefa_atual["ingresso"], inicio_execucao))
    tempos_execucao.append((inicio_execucao, duracao_execucao))

    tempos_espera.append(inicio_execucao - tarefa_atual["ingresso"])
    tempos_vida.append(inicio_execucao - tarefa_atual["ingresso"] + duracao_execucao + troca_contexto + 10)

    print(f"Executando tarefa: Nome={tarefa_atual['nome']}, Ingresso={tarefa_atual['ingresso']}, Início={inicio_execucao}, Duracão={duracao_execucao}")

    tarefa_atual["duracao"] -= duracao_execucao
    tempo_atual = inicio_execucao + duracao_execucao + troca_contexto

    if tarefa_atual["duracao"] > 0:
        tarefas.append(tarefa_atual)

tempo_medio_espera = sum(tempos_espera) / len(tempos_espera)
tempo_medio_vida = sum(tempos_vida) / len(tempos_vida)

print(f'Tempo médio de espera: {tempo_medio_espera}')
print("Tempo médio de vida:", round(tempo_medio_vida, 2))
