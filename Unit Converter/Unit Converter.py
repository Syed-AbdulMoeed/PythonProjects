import tkinter as tk

conversions = {
    ('centimeter', 'meter'): 0.01,
    ('meter', 'centimeter'): 100,
    ('centimeter', 'kilometer'): 0.00001,
    ('kilometer', 'centimeter'): 100000,
    ('centimeter', 'inch'): 0.393701,
    ('inch', 'centimeter'): 2.54,
    ('centimeter', 'foot'): 0.0328084,
    ('foot', 'centimeter'): 30.48,
    ('centimeter', 'yard'): 0.0109361,
    ('yard', 'centimeter'): 91.44,
    ('centimeter', 'mile'): 0.0000062137,
    ('mile', 'centimeter'): 160934.4,

    ('meter', 'kilometer'): 0.001,
    ('kilometer', 'meter'): 1000,
    ('meter', 'inch'): 39.3701,
    ('inch', 'meter'): 0.0254,
    ('meter', 'foot'): 3.28084,
    ('foot', 'meter'): 0.3048,
    ('meter', 'yard'): 1.09361,
    ('yard', 'meter'): 0.9144,
    ('meter', 'mile'): 0.000621371,
    ('mile', 'meter'): 1609.34,

    ('kilometer', 'inch'): 39370.1,
    ('inch', 'kilometer'): 0.0000254,
    ('kilometer', 'foot'): 3280.84,
    ('foot', 'kilometer'): 0.0003048,
    ('kilometer', 'yard'): 1093.61,
    ('yard', 'kilometer'): 0.0009144,
    ('kilometer', 'mile'): 0.621371,
    ('mile', 'kilometer'): 1.60934,

    ('inch', 'foot'): 1 / 12,
    ('foot', 'inch'): 12,
    ('inch', 'yard'): 1 / 36,
    ('yard', 'inch'): 36,
    ('inch', 'mile'): 1 / 63360,
    ('mile', 'inch'): 63360,

    ('foot', 'yard'): 1 / 3,
    ('yard', 'foot'): 3,
    ('foot', 'mile'): 1 / 5280,
    ('mile', 'foot'): 5280,

    ('yard', 'mile'): 1 / 1760,
    ('mile', 'yard'): 1760
}


units = ['centimeter', 'meter', 'kilometer', 'inch', 'foot', 'yard', 'mile']

class GUI:


    def __init__(self):
        self.en_text = 'Saif is the best'
        self.root = tk.Tk()
        self.root.title('Unit Converter')

        self.frm = tk.Frame(self.root)
        self.frm.grid(column=0)
        self.label1 = tk.Label(self.frm, text='Unit Converter', font=('Aerial', 10))
        self.label1.grid(column=0, row=0)
        

        self.frm1 = tk.Frame(self.root, padx=0)
        self.frm1.grid(row=1, column=0 , sticky='nw')
        self.label2 = tk.Label(self.frm1, text='From', font=('Aerial', 8))
        self.label3 = tk.Label(self.frm1, text='To', font=('Aerial', 8))

        self.select1 = tk.StringVar()
        self.select2 = tk.StringVar()
        self.select1.set('meter')
        self.select2.set('yard')
        self.entry1 = tk.OptionMenu(self.frm1, self.select1, *units)
        self.entry2 = tk.OptionMenu(self.frm1, self.select2, *units)

        self.label2.grid(row=1, column=0)
        self.label3.grid(row=2, column=0)
        self.entry1.grid(row=1, column=1)
        self.entry2.grid(row=2, column=1)

        self.label4 = tk.Label(self.root, text='Enter here')
        self.label4.grid(row=3, pady=(10,0))

        self.num = tk.Entry(textvariable=self.en_text)
        self.num.grid(row=4, pady=0)

        self.button = tk.Button(self.root,text='Convert', command=self.convert)
        self.button.grid(row=5, pady=(10,0))

        self.label5 = tk.Label(self.root, text='test')
        self.label5.grid(row=6)
        self.root.mainloop()

    def convert(self):
        f_unit = self.select1.get()
        t_unit = self.select2.get()
        num = self.num.get()
        if num.isnumeric():
            if f_unit == t_unit:
                rate = 1
            else:
                rate = conversions[f_unit, t_unit]
                print(rate)

            result = str(int(num) * rate)
            self.label5.configure(text=result+' '+t_unit+'s')
            
        else:
            self.num.delete(0, tk.END)
            self.num.insert(0,'Insaan banjao')
            
GUI()