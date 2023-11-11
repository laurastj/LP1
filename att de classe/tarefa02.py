from tarefa import (lista)

lista_tarefas = lista()

lista_tarefas.adicionar_tarefa('Limpar a casa')
lista_tarefas.adicionar_tarefa('Estudar')
lista_tarefas.adicionar_tarefa('Ler 64 páginas')
lista_tarefas.adicionar_tarefa('Ir a faculdade')

lista_tarefas.tarefas[0].conclusao()
lista_tarefas.tarefas[2].conclusao()


print('Todas as Tarefas:')
lista_tarefas.mostrar_tarefas()

print('\n Tarefas Concluídas:')
lista_tarefas.tarefas_concluidas()

