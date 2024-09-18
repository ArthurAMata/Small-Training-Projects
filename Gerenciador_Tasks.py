class Task:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.completed = False

    def complete(self):
        self.completed = True

listatasks = []

def showList(lista):
    for item in lista:
        if item.completed:
            print(f"{item.name}[x]")
        else:
            print(item.name)

def showList_index(lista):
    for i, item in enumerate(lista):
        print(f"{i+1} {item.name}")

def select_task():
    index = int(input("Digite o índice da tarefa que você quer completar: ")) - 1
    if 0 <= index < len(listatasks):
        task = listatasks[index]
        task.complete()
        print(f"Tarefa '{task.name}' completada.")
    else:
        print("Índice inválido.")

while True:
    print(" --------MENU-------")
    print("O que você quer fazer?")
    print("1. Criar nova tarefa")
    print("2. Deletar uma tarefa")
    print("3. Concluir uma tarefa")
    print("4. Ver as tarefas pendentes")
    print("5. Fechar o gerenciador de tarefas")
    
    try:
        option = int(input(" "))
    except ValueError:
        print("Digite apenas números, por favor.")
        continue
    
    if option == 1:
        name = input("Digite o nome da sua nova tarefa: ").capitalize()
        date = input("Digite a data de entrega da sua tarefa: ")
        new_task = Task(name, date)
        listatasks.append(new_task)
        print('Tarefa adicionada.')
    elif option == 2:
        if listatasks:
            for i, task in enumerate(listatasks, start=1):
                print(f"{i}. {task.name}")
            index_pop_task = int(input('Digite o índice da tarefa que você quer deletar: ')) - 1
            if 0 <= index_pop_task < len(listatasks):
                del listatasks[index_pop_task]
                print("Tarefa deletada.")
            else:
                print("Índice inválido.")
        else:
            print("Não há tarefas para deletar.")
    elif option == 3:
        if listatasks:
            showList_index(listatasks)
            select_task()
        else:
            print("Não há tarefas para concluir.")
    elif option == 4:
        showList(listatasks)
    elif option == 5:
        break
    else:
        print("Opção inválida.")