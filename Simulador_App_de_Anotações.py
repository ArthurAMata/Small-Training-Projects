class Note:
    def __init__(self,title,body):
        self.title = title
        self.body = body
    
DB_notes = []

while True:
    print('-------MENU De NOTAS---------')
    print('1 Criar uma nota')
    print('2 Consultar uma nota')
    print('3 deletar uma nota')
    try:
        option_main_menu = int(input(' '))
    except ValueError:
        print('Digite apenas valores inteiros por favor')

    if option_main_menu == 1:
        note_title = input('Digite o título da sua nota ').capitalize()
        note_body = input('Digite o corpo da sua nota ')
        new_note = Note(note_title,note_body)
        DB_notes.append(new_note)
    elif option_main_menu == 2:
        for i in DB_notes:
             print(f' {i.title} ')
        note_query = input('Quais das suas notas você quer consultar? ').capitalize()
        for i in DB_notes:
            if i.title == note_query:
                while True:
                    print(i.body)
                    note_view_option = input('Aperte qualquer tecla para parar a visualização da nota ')
                    if note_view_option == ' ':
                        break
                    else:
                        break
    elif option_main_menu == 3:
       for i in DB_notes:
             print(f' {i.title} ')
       note_delete = input('Qual nota você quer deletar? ').capitalize()
       for i in DB_notes:
            if i.title == note_delete:
                DB_notes.remove(i)