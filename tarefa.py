class tarefa:
    def __init__(self, descricao, status='Pendente'):
        self.descricao = descricao
        self.status = status

    def conclusao(self):
        self.status = 'Concluída'

    def __str__(self):
        return f'{self.descricao} - Status: {self.status}'

class lista:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        tarefa_nova = tarefa(descricao)
        self.tarefas.append(tarefa_nova)

    def mostrar_tarefas(self):
        for tarefa in self.tarefas:
            print(tarefa)

    def tarefas_concluidas(self):
        for tarefa in self.tarefas:
            if tarefa.status == 'Concluída':
                print (tarefa)


