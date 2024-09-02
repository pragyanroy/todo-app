import functions_todo
import FreeSimpleGUI as sg
#1
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")
window= sg.Window("My To-Do Application",layout = [[label, input_box,add_button]])

window.read()
window.close()