import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk
root = tk.Tk()
root.title("Note-It")
root.geometry("500x600")
root.configure(bg="#050D1F")

bg_image = Image.open(r"C:\Users\DEEKSHITA R\OneDrive\Desktop\Python projects\Note-it.jpg")  # Use .png or .jpg
bg_image = bg_image.resize((500, 200))   # Resize to match window
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo,height=195,width=495,highlightthickness=0)
bg_label.place(x=0,y=0)
label = tk.Label(root, text='Hello! Welcome to Note-it.',bg="#050D1F",fg="#FAFAFB",font=('Viner Hand ITC',20))
label.pack(padx=10,pady=10)
tasks = [] 

def add_task():
    text = entry.get().strip()
    if text:
        var = tk.BooleanVar()
        cb = tk.Checkbutton(task_frame, text=text,variable=var, font=("Baskerville Old Face", 15), anchor="w")
        cb.pack(anchor="w", padx=20)
        tasks.append({"text": text, "var": var})
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Oops!", "Please enter a task.")

def remove_task():
    to_remove = []
    for widget, task in zip(task_frame.winfo_children(), tasks[:]):
        if isinstance(widget, tk.Checkbutton) and task["var"].get():
            to_remove.append((widget, task))
    for widget, task in to_remove[:]:
        widget.destroy()
        tasks.remove(task)
    if not tasks:
        messagebox.showinfo("All Clear 🎉", "You’ve completed everything! Nothing left to do.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            status = "[x]" if task["var"].get() else "[ ]"
            file.write(f"{status} {task['text']}\n")
    messagebox.showinfo("Saved!", "Tasks saved to text file.")

def load_tasks():
    if os.path.exists("tasks.txt"):
        for widget in task_frame.winfo_children():
            widget.destroy()
        tasks.clear()
        with open("tasks.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    done = line.startswith("[x]")
                    text = line[4:]
                    var = tk.BooleanVar(value=done)
                    cb = tk.Checkbutton(task_frame, text=text, variable=var, font=("Baskerville Old Face",15), anchor="w")
                    cb.pack(anchor="w", padx=20)
                    tasks.append({"text": text, "var": var})
    else:
        messagebox.showinfo("File Not Found", "No saved tasks yet!")

entry = tk.Entry(root, width=30,bg="#FEFEFE",fg="#000000",font=("Baskerville Old Face", 15))
entry.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Add Task", font=("Baskerville Old Face",10),width=15, command=add_task).pack(side="left",padx=0)
tk.Button(btn_frame, text="Remove Task",  font=("Baskerville Old Face",10),width=15, command=remove_task).pack(side="left",padx=0)
tk.Button(btn_frame, text="Save Tasks",  font=("Baskerville Old Face",10),width=15, command=save_tasks).pack(side="left",padx=0)
tk.Button(btn_frame, text="Load Tasks",  font=("Baskerville Old Face",10),width=15, command=load_tasks).pack(side="left",padx=0)

label = tk.Label(root, text='Your tasks for today :',bg="#050D1F",fg="#FAFAFB",font=('Baskerville Old Face',15))
label.pack(anchor='w',padx=10,pady=10)
task_frame = tk.Frame(root)
task_frame.pack(pady=10,padx=10,fill=tk.BOTH, expand=True)
root.mainloop()
