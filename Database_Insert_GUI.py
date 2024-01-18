import tkinter as tk
from db_bridge import *
from tkinter import messagebox


class DatabaseInsert:
    def __init__(self, pos, master=None):
        # build ui
        self.master = master
        toplevel1 = tk.Tk() if self.master is None else tk.Toplevel(self.master)
        toplevel1.configure(height=200, width=200)
        toplevel1.resizable(False, False)
        toplevel1.title("CryptoShop Database Insert")
        toplevel1.geometry(pos)
        toplevel1.protocol("WM_DELETE_WINDOW", self.close_wind)
        toplevel1.rowconfigure(0, pad=5)
        toplevel1.columnconfigure(0, pad=9)

        labelframe1 = tk.LabelFrame(toplevel1)
        labelframe1.configure(height=200, text='Profit Calculator', width=200)
        labelframe1.grid(column=0, ipadx=77, row=0)

        self.entry1_var = tk.StringVar()
        self.entry1 = tk.Entry(labelframe1, textvariable=self.entry1_var)
        self.entry1.pack(padx=5, pady=10, side="top")

        button1 = tk.Button(labelframe1)
        button1.configure(text='Calculate', command=self.calculate_button)
        button1.pack(ipadx=5, pady="0 5", side="top")

        labelframe2 = tk.LabelFrame(toplevel1)
        labelframe2.configure(height=200, text='New Buys Entry', width=200)
        labelframe2.grid(column=0, row=1)

        self.entry2 = tk.Entry(labelframe2)
        self.entry2.grid(column=0, padx=10, row=1)

        label1 = tk.Label(labelframe2)
        label1.configure(text='Wallet Address')
        label1.grid(column=0, ipadx=5, ipady=3, row=0)

        self.entry3 = tk.Entry(labelframe2)
        self.entry3.grid(column=1, padx=10, row=1)

        label2 = tk.Label(labelframe2)
        label2.configure(text='Telegram User')
        label2.grid(column=1, ipadx=5, ipady=3, row=0)

        self.entry4 = tk.Entry(labelframe2)
        self.entry4.grid(column=0, padx=10, row=3)

        label3 = tk.Label(labelframe2)
        label3.configure(text='Quantity')
        label3.grid(column=0, ipadx=5, ipady=3, row=2)

        self.entry5_var = tk.StringVar()
        self.entry5 = tk.Entry(labelframe2, textvariable=self.entry5_var)
        self.entry5.grid(column=1, padx=10, row=3)

        label4 = tk.Label(labelframe2)
        label4.configure(text='Original Price')
        label4.grid(column=1, ipadx=5, ipady=3, row=2)

        self.entry6_var = tk.StringVar()
        self.entry6 = tk.Entry(labelframe2, textvariable=self.entry6_var)
        self.entry6.grid(column=0, padx=10, pady="0 10", row=5)

        label5 = tk.Label(labelframe2)
        label5.configure(text='Paid Price')
        label5.grid(column=0, ipadx=5, ipady=3, row=4)

        self.entry7 = tk.Entry(labelframe2)
        self.entry7.grid(column=1, padx=10, pady="0 10", row=5)

        label6 = tk.Label(labelframe2)
        label6.configure(text='Date')
        label6.grid(column=1, ipadx=5, ipady=3, row=4)

        label7 = tk.Label(toplevel1)
        label7.configure(text='Item Bought')
        label7.grid(column=0, row=2)

        self.optionmenu1_var = tk.StringVar(value="")
        values1 = get_item_list()
        optionmenu1 = tk.OptionMenu(toplevel1, self.optionmenu1_var, *values1, command=None)
        optionmenu1.grid(column=0, row=3)

        label8 = tk.Label(toplevel1)
        label8.configure(text='Promo?')
        label8.grid(column=0, row=4)

        button3 = tk.Button(toplevel1)
        button3.configure(text='Add buy to Database', width=40, command=self.add_buy_button)
        button3.grid(column=0, pady=7, row=6)

        self.optionmenu2_var = tk.StringVar(value="No Promo")
        values2 = get_promo_list()
        optionmenu2 = tk.OptionMenu(toplevel1, self.optionmenu2_var, *values2, command=None)
        optionmenu2.grid(column=0, row=5)

        labelframe3 = tk.LabelFrame(toplevel1)
        labelframe3.configure(height=200, text='Add to tables', width=200)
        labelframe3.grid(column=0, ipadx=0, row=7)

        label9 = tk.Label(labelframe3)
        label9.configure(text='Add a Promo')
        label9.pack(side="top")

        self.entry11 = tk.Entry(labelframe3)
        self.entry11.configure(width=45)
        self.entry11.pack(padx=7, pady="5 7", side="top")

        button6 = tk.Button(labelframe3)
        button6.configure(text='Add Promo', command=self.add_promo_button)
        button6.pack(pady="0 15", side="top")

        label11 = tk.Label(labelframe3)
        label11.configure(text='Add an Item')
        label11.pack(side="top")

        self.entry12 = tk.Entry(labelframe3)
        self.entry12.configure(width=45)
        self.entry12.pack(padx=7, pady="5 7", side="top")

        button7 = tk.Button(labelframe3)
        button7.configure(text='Add Item', command=self.add_item_button)
        button7.pack(pady="0 5", side="top")

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()
        
    def close_wind(self):
        self.master.destroy()

    def calculate_button(self):
        original_price = float(self.entry1_var.get())
        paid_price = str(original_price + original_price * 0.40 + 0.80)
        self.entry5_var.set(original_price)
        self.entry6_var.set(paid_price)

    def add_promo_button(self):
        try:
            add_promo(self.entry11.get())
            messagebox.showinfo("Add Promo Successful", "New Promo added to the Database")
        except:
            messagebox.showerror("Add Promo Error", "Error adding new Promo to the Database")

    def add_item_button(self):
        try:
            add_item(self.entry12.get())
            messagebox.showinfo("Add Item Successful", "New Item added to the Database")
        except:
            messagebox.showerror("Add Item Error", "Error adding new Item to the Database")

    def add_buy_button(self):
        try:
            time = int(date_time_encode(self.entry7.get()))
            add_buy(self.entry2.get(), self.entry3.get(), int(self.entry4.get()), float(self.entry5.get()),
                    float(self.entry6.get()), get_promo_id(self.optionmenu2_var.get()), time,
                    get_item_id(self.optionmenu1_var.get()), 0)
            messagebox.showinfo("Add Buy Successful", "New Buy added to the Database")
        except:
            messagebox.showerror("Add Buy Error", "Error adding new Buy to the Database")


