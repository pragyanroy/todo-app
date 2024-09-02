import os
import time
#from functions_todo import get_todos,write_todos
import functions_todo

# file_path = os.path.join(os.path.dirname(__file__), 'todo.txt')
# # print("Current Working Directory:", os.getcwd())
#1234
user_prompt = "Enter a Todo: "
user_prompt = user_prompt.strip()
#Added Time now V2
now = time.strftime("%A,%B %d,%Y %H:%M:%S")
print(f"It is Time {now}")

while True:
    user_action = input('Enter add or show or edit or complete or exit: ')
    user_action = user_action.strip()
    #match user_action:
    #case 'add':
    if user_action.startswith('add'):
        try:
            #todo=input(user_prompt) + "\n"
            todo = user_action[4:] + '\n'
            todos = functions_todo.get_todos()
            todos.append(todo)

            functions_todo.write_todos(todos, )

        except ValueError:
            print("Your command is not valid")
            continue


    elif user_action.startswith('show'):
        try:
            todos = functions_todo.get_todos()
            #file.close()
            #todos.append(todo + '\n')

            #file.close()
            #new_todos = []
            #print(todos)

            # See below create list on the fly in 1 line
            #for item in todos:
            #new_item = item.strip('\n')
            #new_todos.append(new_item)
            # See below create list on the fly in 1 line
            new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(new_todos):
                item = item.title()
                row = f"{index + 1}-{item}"
                print(row)
                #item = item.title()
                #print(f"{index+1}-{item}")
        except ValueError:
            print("Your command is not valid")
            continue


    elif user_action.startswith('edit'):
        try:
            #existing_todo_num = int(input('Enter the number of Todo you want to edit:'))

            #existing_todo_num = existing_todo_num -1
            number = int(user_action[5:])
            number = number - 1

            todos = functions_todo.get_todos()

            new_todo = input('Enter the new Todo: ')
            todos[number] = new_todo + "\n"

            #todos[existing_todo_num] = new_todo
            functions_todo.write_todos(todos)

            #file.close()
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            #existing_todo_num = int(input('Enter the number of Todo you want to complete: '))
            existing_todo_num = int(user_action[9:])
            existing_todo_num = existing_todo_num - 1
            todos = functions_todo.get_todos()
            removetodo = todos[existing_todo_num].strip('\n')
            todos.pop(existing_todo_num)
            functions_todo.write_todos(todos)

            message = f"Todo {removetodo} was removed"
            print(message)
        except IndexError:
            print("Index Entered  is not valid")
            continue


    elif user_action.startswith('exit'):
        break
    else:
        print("Hey you entered unknown command")

print('bye')
