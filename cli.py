#from functions import get_todos, write_todos
import functions
import time

now = time.strftime( "%b %d, %Y %H: %M: %S")
print("it is ", now)

while True:
  user_action = input("Type Add or show  edit or complete exit")
  user_action = user_action.strip()


  if user_action.startswith("add"):
      todo = user_action[4:]

      todos = functions.get_todos()

      todos.append(todo + "\n")

      functions.write_todos(todos)

  elif user_action.startswith("show"):

      todos = get_todos()

      #new_todos = []

     # for item in todos:
         # new_item = item.strip("\n")
         # new_todos.append(new_item)

      for index, item in enumerate(todos):
          item = item.strip("\n")
          row = f"{index + 1}-{item}"
          print(row)
  elif user_action.startswith("edit"):
      try:
          number = int(user_action[5:])
          print(number)

          number = number - 1

          todos = functions.get_todos()

          new_todo = input("enter a new todos :")
          todos[number] = new_todo + '\n'

          functions.write_todos(todos)
      except ValueError:
          print("your given command is not valid")
          continue

  elif user_action.startswith("complete"):
      try:
          number = int(user_action[9:])

          todos = functions.get_todos()
          index = number - 1
          todo_to_remove = todos[index].strip("\n")
          todos.pop(index)

          functions.write_todos("todos.txt", todos)

          message = f"Todo {todo_to_remove} was remove from the list"
          print(message)
      except IndexError:
       print("There is non item match with that number")
      continue

  elif user_action.startswith("exit"):
      break
  else:
      print("plz enter valid command")

print("Bye Bye see u later")








