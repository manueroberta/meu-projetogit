# Gerenciador de Tarefas
tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada!")

def listar_tarefas():
    print("Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")

# Teste do programa
adicionar_tarefa("Estudar Python")
adicionar_tarefa("Estudar matemática")
adicionar_tarefa("Estudar português")
listar_tarefas()
