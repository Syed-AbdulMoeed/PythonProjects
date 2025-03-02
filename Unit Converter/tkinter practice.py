import tkinter as tk
from tkinter import messagebox

class GUI:
    

    def __init__(self):
        self.word = "init"
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text='Heyy saifii')
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, width=20)
        self.textbox.pack(padx=10, pady=10)

        self.check_status = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text='Print in app', variable=self.check_status)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Print this', command=self.set_label)
        self.button.pack(padx=10, pady=10)

        self.list1 = tk.Listbox(self.root, selectmode='SINGLE', height=3)
        self.list1.insert(1 , 'keria')
        self.list1.insert(2, 'showmaker')
        self.list1.insert(3, 'zeka')
        self.list1.pack(padx=10, pady=10)

        self.clicked = tk.StringVar()
        self.clicked.set('cook')
        options = ['elyoya', 'supa', 'myrwin' , 'cook', 'peyz']
        self.drop = tk.OptionMenu(self.root, self.clicked, *options )
        self.drop.pack()

        self.button1 = tk.Button(self.root, text='enter', command=self.set_label)
        self.button1.pack()

        self.label2 = tk.Label(self.root, text=self.word)
        self.label2.pack(padx=10, pady=10)

        self.quit = tk.Button(self.root, text='Quit', command=self.root.destroy)
        self.quit.pack(padx=10, pady=10)

        self.root.mainloop()
    def print_check(self):
        if self.check_status.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo("Message",self.textbox.get('1.0', tk.END))

    def set_label(self):
        self.label2.config(text=self.textbox.get('1.0', tk.END))
        print(self.list1.get('active'))
        print(self.clicked.get())
         
    


GUI()