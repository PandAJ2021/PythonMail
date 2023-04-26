import tkinter as tk

class MyTkinterApp:
    def __init__(self, master):
        self.master = master

    def create_button(self, text, command=None ):
        button = tk.Button(self.master, text=text, command=command)
        button.pack()
        return button

    def create_entry(self):
        entry = tk.Entry(self.master)
        entry.pack()
        return entry
        
    def create_label(self, text):
        label = tk.Label(self.master, text=text)
        label.pack()
        return label

root = tk.Tk()
my_app = MyTkinterApp(root)

# create a button and an entry using the class methods
my_app.create_button("Click me!")
my_app.create_entry()

root.mainloop()

