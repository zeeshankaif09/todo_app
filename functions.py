Filepath = "todos.txt"


def get_todos(filepath=Filepath):
  with open(filepath, "r") as file_local:
    todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=Filepath):
  with open(filepath, "w") as file:
    file.writelines(todos_arg)


if__name__ = "__main__"
print("hello")
print(get_todos())
