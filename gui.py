import functions
import PySimpleGUI as sg


clock = sg.Text("", key="clock")
label = sg.Text("type in a To-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.button("Add")
list_box = sg.List_box(values=functions.get_todos(), key='todos',
                       enable_events=True, size=[45, 10])
edit_button = sg.button("Edit")
complete_button = sg.button("complete")
exit_button = sg.button("exit")

window = sg.Window('My-Todo-App',
                   layout=[[clock],
                          [lable],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],[exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout= 10)
    window["clock"].update(value=time.strftime(" %b %d, %Y %H: %M: %S"))
    print(1, even)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit" :
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values[" todos"]
                todos = function.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("please select a item first : ", font=("helvetica", 20))
        case "complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values="todo")
                window['todo'].update(values="")
            except IndexError:
                sg.popup("please select a item first : ", font=("helvetica", 20))
        case "exit":
            break
        case 'todos':
            window['todos'].update(value=values['todos'])
        case sg.Win_CLOSED:
            break

window.close()
