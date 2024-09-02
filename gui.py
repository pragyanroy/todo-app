import functions_todo
import FreeSimpleGUI as sg
#1
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo",key = "todo")
add_button = sg.Button("Add")
window= sg.Window("My To-Do Application",layout = [[label, input_box,add_button]])

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions_todo.get_todos()
            new_todo = values['todo']
            todos.append(new_todo)
            functions_todo.write_todos(todos)

        case sg.WIN_CLOSED:
            break
window.close()