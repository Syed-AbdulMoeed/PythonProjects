import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import logic

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x300')
        self.root.title('Expenses')

        self.frames = {}

        self.df = logic.read_csv()

        self.create_home_page()
        self.create_home_top()
        self.create_view_page()
        self.create_add_page()
        self.create_del_page()
        self.create_mon_page()

        self.show_home()


        self.root.mainloop()

    def create_home_page(self):
        #Create homepage frame and top frame containing buttons, this is the first frame

        home = tk.Frame(self.root)
        home.place(rely=0.25, relwidth=1, relheight=0.75) 
        #bu -> button
        bu_view = tk.Button(home, text='View All Expenses', command=lambda: self.show_frame('view') ) # TO-DO: Include Highest expense here
        bu_view.place(relx=0, rely=0, relwidth=1, relheight=0.25)

        bu_add = tk.Button(home, text='Add New Expense', command=lambda: self.show_frame('add'))
        bu_add.place(relx=0, rely=0.25, relwidth=1, relheight=0.25)

        bu_del = tk.Button(home, text='Delete Expense', command=lambda: self.show_frame('del')) 
        bu_del.place(relx=0, rely=0.5, relwidth=1, relheight=0.25)

        bu_month = tk.Button(home, text='View Monthly Expense', command=lambda: self.show_frame('month'))
        bu_month.place(relx=0, rely=0.75, relwidth=1, relheight=0.25)

        self.frames['home'] = home


    def create_home_top(self):
        home_top = tk.Frame(self.root)
        home_top.place(y=0, relheight=0.25, relwidth=1)
        home_title = tk.Label(home_top, text='Expense Manager')
        home_title.pack()
        self.frames['home_top'] = home_top

    
    def create_view_page(self):
        if 'view' not in self.frames:
            v_p = tk.Frame(self.root)
            v_p.place(relheight=1, relwidth=1)

            # Save frame for reuse
            self.frames['view'] = v_p

            # Create static buttons (only once)
            tk.Button(v_p, text='Sort Values', command=self.sort_df).place(rely=0.7, relheight=0.1, relwidth=1)
            tk.Button(v_p, text='Pie Chart', command=lambda: logic.chart(self.df)).place(rely=0.8, relheight=0.1, relwidth=1)
            tk.Button(v_p, text='Return to HomePage', command=self.show_home).place(rely=0.9, relheight=0.1, relwidth=1)

            # Create the sub-frame to hold the table
            self.table_frame = tk.Frame(v_p)
            self.table_frame.place(relheight=0.7, relwidth=1)

        # Clear and redraw table contents
        self.update_table()


    def update_table(self):
        # Clear the old table
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Draw table headers
        for index, col_name in enumerate(['name', 'category', 'cost', 'date']):
            tk.Label(self.table_frame, text=col_name, borderwidth=1, relief='solid').grid(row=0, column=index, sticky='nsew')
            self.table_frame.grid_columnconfigure(index, weight=1)

        # Draw table data
        expenses = logic.view_df(self.df)
        for rowi, expense in enumerate(expenses, 1):
            for coli, val in enumerate(expense):
                tk.Label(self.table_frame, text=val).grid(row=rowi, column=coli)


    def create_add_page(self):
        add = tk.Frame(self.root)
        add.place(relheight=1, relwidth=1)

        info_input = tk.Frame(add)
        info_input.place(rely=0.1, relwidth=1, relheight=0.7)
        category = tk.StringVar()
        cat_combo = ttk.Combobox(info_input, textvariable=category, values=['Food & Groceries', 'Housing & Rent', 'Transportation', 'Entertainment & Leisure', 
                                                                            'Health & Medical', 'Personal Care', 'Bills & Subscriptions'])
        cat_combo.place(relx=0.5, relwidth=0.5)
        tk.Label(info_input, text='Select Category').place(relwidth=0.5)

        cost = tk.IntVar()
        cost_entry = tk.Entry(info_input, textvariable=cost)
        cost_entry.place(rely=0.1, relwidth=0.5, relx=0.5)
        tk.Label(info_input, text='Money Spent').place(rely=0.1,relwidth=0.5)

        tk.Label(info_input, text='Select Date').place(rely=0.2,relwidth=0.5)
        date_entry = DateEntry(info_input, date_pattern='yyyy-mm-dd')
        date_entry.place(rely=0.2, relwidth=0.5, relx=0.5)

        tk.Label(info_input, text='Bought item').place(rely=0.3, relwidth=0.5)
        name_var = tk.StringVar()
        name_var.set('e.g: Toy')
        name_entry = tk.Entry(info_input, textvariable=name_var)
        name_entry.place(rely=0.3, relx=0.5, relwidth=0.5)
        
        status = tk.Label(info_input, text='Pending')
        status.place(rely=0.8, relwidth=0.5, relx=0.5)
        tk.Label(info_input, text='Status:').place(rely=0.8, relwidth=0.5)

        tk.Button(add, text='Add Expense', command=lambda: self.add_expense(category, cost, date_entry, name_var, status) ).place(rely=0.8, relwidth=1, relheight=0.1)
        tk.Button(add, text='Return to HomePage', command=self.show_home).place(rely=0.9, relheight=0.1, relwidth=1)
        self.frames['add'] = add


    def create_del_page(self):
        delete = tk.Frame(self.root)
        delete.place(relheight=1, relwidth=1)
        self.del_table = tk.Frame(delete)
        self.del_table.place(rely=0.1, relwidth=1, relheight=0.7)
        #add checkbox to each row to delete
        self.del_table_update()


        tk.Button(delete, text='Delete Selected Items' , command=self.row_delete).place(rely=0.8, relheight=0.1, relwidth=1)
        tk.Button(delete, text='Return to HomePage', command=self.show_home).place(rely=0.9, relheight=0.1, relwidth=1)
        self.frames['del'] = delete
        

    def create_mon_page(self):
        mon_page = tk.Frame(self.root)
        mon_page.place(relheight=1, relwidth=1)
        self.mon_table = tk.Frame(mon_page)
        self.mon_table.place(rely=0.1, relheight=0.7, relwidth=1)
        self.month_table()
        


        tk.Button(mon_page, text='Return To HomePage', command=self.show_home).place(rely=0.9, relheight=0.1, relwidth=1)
        self.frames['month'] = mon_page


    def month_table(self):
        # Clear the old table
        for widget in self.mon_table.winfo_children():
            widget.destroy()

        # Draw table headers
        for index, col_name in enumerate(['Month', 'Sum of Cost']):
            tk.Label(self.mon_table, text=col_name, borderwidth=1, relief='solid').grid(row=0, column=index, sticky='nsew')
            self.mon_table.grid_columnconfigure(index, weight=1)

        summary = logic.monthly_summary(self.df)

        for rowi, (month, total) in enumerate(summary, 1):
            tk.Label(self.mon_table, text=month, borderwidth=1, relief='solid').grid(row=rowi, column=0)
            tk.Label(self.mon_table, text=total, borderwidth=1, relief='solid').grid(row=rowi, column=1)



    def del_table_update(self):
        # Clear the old table
        for widget in self.del_table.winfo_children():
            widget.destroy()

        # Draw table headers
        for index, col_name in enumerate(['name', 'category', 'cost', 'date', 'delete']):
            tk.Label(self.del_table, text=col_name, borderwidth=1, relief='solid').grid(row=0, column=index, sticky='nsew')
            self.del_table.grid_columnconfigure(index, weight=1)

        # Make list of intvars and checks for checks
        self.intvars = []
        self.checks = []
        for i in range(self.df.shape[0]):
            self.intvars.append(tk.IntVar())
            self.checks.append(tk.Checkbutton(self.del_table, variable=self.intvars[i]))
            

        # Draw table data
        expenses = logic.view_df(self.df)
        for rowi, expense in enumerate(expenses, 1):
            for coli, val in enumerate(expense):
                tk.Label(self.del_table, text=val).grid(row=rowi, column=coli)
            self.checks[rowi-1].grid(row=rowi, column=4)


    def row_delete(self):
        #get id from checked
        del_index = []
        for i,var in enumerate(self.intvars):
            if var.get() == 1:
                del_index.append(self.df.loc[i, 'id'])
        if del_index:
            logic.delete(self.df, del_index)
            self.df['id'] = self.df.index + 1
            logic.save_csv(self.df)
            self.del_table_update()
            self.update_table()
            self.month_table()


    def add_expense(self,category, cost, date, name, status):
        try:
            category = category.get()
            cost = cost.get()
            date = date.get()
            name = name.get()

            self.df = logic.add_expense(self.df,category, name, cost, date)
            logic.save_csv(self.df)
            self.update_table()
            self.del_table_update()
            self.month_table()
            status.configure(text='Success!')
        except:
            status.configure(text='Failed, Cost must be integer')

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def show_home(self):
        self.show_frame('home')
        self.show_frame('home_top')

    def sort_df(self):
        self.df = logic.sort(self.df)
        self.update_table()



App()