# To-Do-List : A command line interface application where user can add, remove and view tasks
# Features 
# User can add, delete, update, view, mark as complete,


tasks = []

def addTask():
    task = input("Enter task : ")
    tasks.append(task)
    print("Task added successfully!")

def viewTask():
    num = 1
    for i in tasks:
        print(f"{num}. {i}")
        num += 1

def deletTask():
    delTask = int(input("Enter task number you want to delete : "))
    tasks.pop(delTask-1)
    print("Task deleted successfully!")

def updateTask():
    upd = int(input("Enter task number you want to update : "))
    new = input("Enter new updated task : ")
    tasks[upd-1] = new 
    print("Task updated successfully!")

def completeTask():
    com = int(input("Enter task numner, want to tick as complete : "))
    tasks[com-1] = "[✔] " + tasks[com-1]


def main():
    print("""\033[32m
      ╔╦╗╔═╗  ╔╦╗╔═╗   ╦  ╦╔═╗╔╦╗
       ║ ║ ║───║║║ ║───║  ║╚═╗ ║ 
       ╩ ╚═╝  ═╩╝╚═╝   ╩═╝╩╚═╝ ╩ 
       \033[0m""")
    print("\033[32m*********************************************\033[0m")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Mark as complete Task")
    print("5. delete Task")
    print("6. Exit")
    print("\033[32m*********************************************\033[0m")

    while True:
        try:
            choice = int(input("Enter Choice : "))
            match choice:
                case 1:
                    addTask()
                case 2:
                    viewTask()
                case 3:
                    updateTask()
                case 4:
                    completeTask()
                case 5:
                    deletTask()
                case 6:
                    break
        except ValueError:
            print("Enter a valid input")


if __name__ == "__main__":
    main()