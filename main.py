from datetime import datetime
import json


def load_task():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_task():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)


tasks = load_task()


def add_task():
    task = input("enter the task: ")
    priority = input("Priority (High / Medium / Low): ").capitalize()
    Categories=input("Categories (Study / Work / Life): ").capitalize()
    task = {
        "task": task,
        "status": "not started",
        "priority": priority,
        "Categories": Categories,
        "time": datetime.now().isoformat(),
    }
    tasks.append(task)
    print("task added sucssfaly")
    save_task()


def show_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks, 1):
            time_obj = datetime.fromisoformat(task["time"])
            time_str = time_obj.strftime("%I:%M %p").lstrip("0")
            print(
                f"{i}. task: {task['task']} | status: {task['status']} | priority: {task['priority']} | Categories: {task['Categories']} | time: {time_str}"
            )


def delete_task():
    if not tasks:
        print("no tasks valid now to deleted.")
    else:
        show_tasks()
        index = int(input("enter the number of task to deleted: "))
        if 0 <= index - 1 < len(tasks):
            tasks.pop(index - 1)
            print("the task to delete successfully.")
            save_task()
        else:
            print("invalid input")


def edit_task():
    if not tasks:
        print("no tasks valid now to edited")
    else:
        show_tasks()
        index = int(input("enter old task: "))
        if 0 <= index - 1 < len(tasks):
            new_task = input("enter the new task: ")
            tasks[index - 1]["task"] = new_task
            tasks[index - 1]["time"] = datetime.now().isoformat()
            save_task()
            print("task edited successfully")
        else:
            print("invalid task number")


def complete_task():
    if not tasks:
        print("no tasks valid now to complete.")
    else:
        show_tasks()
        index = int(input("enter the numb of task to completed: "))
        if 0 <= index - 1 < len(tasks):
            tasks[index - 1]["status"] = "done"
            save_task()
        else:
            print("invalid task number")


def edit_priority():
    show_tasks()
    index = int(input("enter the number of task: "))
    if 0 <= index - 1 < len(tasks):
        priority = input("Priority (High / Medium / Low): ").capitalize()
        tasks[index - 1]["priority"] = priority
        tasks[index - 1]["time"] = datetime.now().isoformat()
        save_task()
    else:
        print("invalid input")


def show_done_task():
    if not tasks:
        print("no tasks valid")
    else:
        for i, task in enumerate(tasks, 1):

            if task["status"] == "done":
                time_obj = datetime.fromisoformat(task["time"])
                time_str = time_obj.strftime("%I:%M %p").lstrip("0")
                print(
                    f"{i}. task: {task['task']} | status: {task['status']} | priority: {task['priority']} | Categories{task['Categories']} |  time: {time_str}"
                )


def search_by_name():
    task_name = input("enter task name: ").lower()
    for i, task in enumerate(tasks, 1):
        if task["task"].lower()== task_name:
            time_obj = datetime.fromisoformat(task["time"])
            time_str = time_obj.strftime("%I:%M %p").lstrip("0")
            print(
                f"{i}. task: {task['task']} | status: {task['status']} | priority: {task['priority']} |Categories: {task['Categories']} | time: {time_str}"
            )


def menu():
    while True:
        print("------->>>> Welcome to simple TODO APP <<<<-------")
        print("1.add task")
        print("2.show task")
        print("3.delete task")
        print("4.edit task")
        print("5.complete task")
        print("6.edit priority")
        print("7.show done task")
        print("8.search task")
        print("9.---EXIT---")
        choice = int(input("enter the number of operation: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            show_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            edit_task()
        elif choice == 5:
            complete_task()
        elif choice == 6:
            edit_priority()
        elif choice == 7:
            show_done_task()
        elif choice == 8:
            search_by_name()
        elif choice == 9:
            print("GOODBY")
            break
        else:
            print("invalid choices")


menu()
