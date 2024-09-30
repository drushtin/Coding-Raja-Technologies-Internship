from tkinter import *
from tkinter import ttk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('My To-Do List')
        self.root.geometry('850x610+400+150')
        self.label = Label(self.root, text='My To-Do List', font='a 20 bold', width=10, bd=5, bg='purple', fg='white')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Enter the Task', font='Arial, 15 bold', width=15, bd=5, bg='purple', fg='white')
        self.label2.place(x=40, y=60)

        self.label3 = Label(self.root, text='List of Tasks', font='Arial, 15 bold', width=15, bd=5, bg='purple', fg='white')
        self.label3.place(x=550, y=60)

        self.main_text = Listbox(self.root, height=20, bd=5, width=60, font="Arial 12 bold")
        self.main_text.place(x=450, y=100)

        self.text = Entry(self.root, bd=5, width=30, font='Arial 10 bold')
        self.text.place(x=30, y=100)

        self.due_date_label = Label(self.root, text='Due Date (yy-mm-dd):', font='Arial 10 bold', bg='purple', fg='white')
        self.due_date_label.place(x=20, y=150)
        self.due_date_entry = Entry(self.root, bd=5, width=18, font='Arial 10 bold')
        self.due_date_entry.place(x=200, y=150)

        self.priority_label = Label(self.root, text='Priority:', font='Arial 10 bold', bg='purple', fg='white')
        self.priority_label.place(x=20, y=200)
        self.priority_var = StringVar(self.root)
        self.priority_var.set("Normal") 
        self.priority_dropdown = ttk.Combobox(self.root, textvariable=self.priority_var, values=["Low", "Normal", "High"])
        self.priority_dropdown.place(x=100, y=200)

        def add_task():
            task = self.text.get()
            due_date = self.due_date_entry.get()
            priority = self.priority_var.get()
            if task:
                task_with_due_date = f"{task} (Due: {due_date}) - Priority: {priority}"
                self.main_text.insert(END, task_with_due_date)
                with open('data.txt', 'a') as file:
                    file.write(task_with_due_date + '\n')
                self.text.delete(0, END)
                self.due_date_entry.delete(0, END)

        def delete_task():
            selection = self.main_text.curselection()
            if selection:
                index = selection[0]
                self.main_text.delete(index)
                with open('data.txt', 'r') as file:
                    lines = file.readlines()
                with open('data.txt', 'w') as file:
                    for i, line in enumerate(lines):
                        if i != index:
                            file.write(line)

        def mark_completed():
            selection = self.main_text.curselection()
            if selection:
                index = selection[0]
                task = self.main_text.get(index)
                if "(Completed)" not in task:
                    completed_task = task + " (Completed)"
                    self.main_text.delete(index)
                    self.main_text.insert(index, completed_task)
                    with open('data.txt', 'r') as file:
                        lines = file.readlines()
                    with open('data.txt', 'w') as file:
                        for i, line in enumerate(lines):
                            if i != index:
                                file.write(line)
                        file.write(completed_task + '\n')

        def update_task():
            selection = self.main_text.curselection()
            if selection:
                index = selection[0]
                task = self.text.get()
                due_date = self.due_date_entry.get()
                priority = self.priority_var.get()
                if task:
                    updated_task = f"{task} (Due: {due_date}) - Priority: {priority}"
                    self.main_text.delete(index)
                    self.main_text.insert(index, updated_task)
                    with open('data.txt', 'r') as file:
                        lines = file.readlines()
                    with open('data.txt', 'w') as file:
                        for i, line in enumerate(lines):
                            if i != index:
                                file.write(line)
                        file.write(updated_task + '\n')
                    self.text.delete(0, END)
                    self.due_date_entry.delete(0, END)

        with open('data.txt', 'r') as file:
            tasks = file.readlines()
            for task in tasks:
                self.main_text.insert(END, task.strip())

        self.add_button = Button(self.root, text="Add Task", font='Arial 12 bold', width=10, bd=5, bg='purple', fg='white', command=add_task)
        self.add_button.place(x=20, y=250)

        self.delete_button = Button(self.root, text="Delete Task", font='Arial 12 bold', width=10, bd=5, bg='purple', fg='white', command=delete_task)
        self.delete_button.place(x=20, y=300)

        self.mark_button = Button(self.root, text="Mark Completed", font='Arial 12 bold', width=15, bd=5, bg='purple', fg='white', command=mark_completed)
        self.mark_button.place(x=20, y=350)

        self.update_button = Button(self.root, text="Update Task", font='Arial 12 bold', width=12, bd=5, bg='purple', fg='white', command=update_task)
        self.update_button.place(x=20, y=400)

def main():
    root = Tk()
    todo_app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
