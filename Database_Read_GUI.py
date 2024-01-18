import tkinter
import tkinter as tk
from db_bridge import *
from tkinter import messagebox
from Database_Viewer import CryptoshopviewerApp


class DatabaseReader:
    def __init__(self, pos, master=None):
        self.reversed_status = 0
        # build ui
        self.master = master
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=200, width=200)
        toplevel1.geometry(pos)  
        toplevel1.title("CryptoShop Database Reader")
        toplevel1.protocol("WM_DELETE_WINDOW", self.close_wind)

        labelframe1 = tk.LabelFrame(toplevel1)
        labelframe1.configure(
            height=200,
            padx=15,
            text='Database Finder',
            width=200)
        labelframe1.pack(padx=5, pady=5, side="top")

        self.entry1 = tk.Entry(labelframe1)
        self.entry1.pack(padx=5, pady=5, side="top")

        button1 = tk.Button(labelframe1)
        button1.configure(text='Find All', width=20, command=self.find_all_button)
        button1.pack(padx=5, pady=5, side="top")

        button2 = tk.Button(labelframe1)
        button2.configure(text='Find Wallet', width=20, command=lambda: self.find_value_button("Compras.wallet"))
        button2.pack(padx=5, pady=5, side="top")

        button3 = tk.Button(labelframe1)
        button3.configure(text='Find Tlg User', width=20, command=lambda: self.find_value_button("Compras.tlg_user"))
        button3.pack(padx=5, pady=5, side="top")

        button4 = tk.Button(labelframe1)
        button4.configure(text='Find Promo', width=20, command=lambda: self.find_value_button("Promos.promo"))
        button4.pack(padx=5, pady=5, side="top")

        button5 = tk.Button(labelframe1)
        button5.configure(text='Find Date', width=20, command=lambda: self.find_value_button("Compras.fecha"))
        button5.pack(padx=5, pady=5, side="top")

        button6 = tk.Button(labelframe1)
        button6.configure(text='Find Item', width=20, command=lambda: self.find_value_button("Items.item"))
        button6.pack(padx=5, pady=5, side="top")

        button7 = tk.Button(labelframe1)
        button7.configure(text='Find Status', width=20, command=lambda: self.find_value_button("Compras.completada"))
        button7.pack(padx=5, pady=5, side="top")

        button8 = tk.Button(labelframe1)
        button8.configure(text='Total Profit', width=20, command=self.total_profit_button)
        button8.pack(padx=5, pady=(20, 5), side="top")
        
        button9 = tk.Button(labelframe1)
        button9.configure(text='Complete Transaction', width=20, command=self.complete_transaction_button)
        button9.pack(padx=5, pady=(5, 20), side="top")

        labelframe3 = tk.LabelFrame(labelframe1)
        labelframe3.configure(height=200, padx=25, text='ORDER BY', width=200)
        labelframe3.pack(pady="0 10", side="top")

        self.var = tk.StringVar()
        self.var.set("Compras.id")

        radiobutton1 = tk.Radiobutton(labelframe3)
        radiobutton1.configure(padx=10, text='ID', variable=self.var, value="Compras.id")
        radiobutton1.grid(column=0, row=0, sticky="w")

        radiobutton2 = tk.Radiobutton(labelframe3)
        radiobutton2.configure(padx=10, text='quantity', variable=self.var, value="cantidad")
        radiobutton2.grid(column=0, row=1, sticky="w")

        radiobutton3 = tk.Radiobutton(labelframe3)
        radiobutton3.configure(padx=10, text='price', variable=self.var, value="precio_pagado")
        radiobutton3.grid(column=0, row=2, sticky="w")

        radiobutton4 = tk.Radiobutton(labelframe3)
        radiobutton4.configure(padx=10, text='fecha', variable=self.var, value="fecha")
        radiobutton4.grid(column=0, row=3, sticky="w")

        checkbutton1 = tk.Checkbutton(labelframe3)
        checkbutton1.configure(text='Reversed', command=self.activate_check)
        checkbutton1.grid(column=0, pady=10, row=4)

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def close_wind(self):
        self.master.destroy()
        
    def activate_check(self):
        self.reversed_status = 0 if self.reversed_status else 1

    def find_all_button(self):
        data = find_all(self.var.get(), self.reversed_status)
        data_viewer = CryptoshopviewerApp(data)
        data_viewer.run()

    def find_value_button(self, value_type):
        if value_type == "Compras.fecha":
            entry = date_time_encode(self.entry1.get())
        elif value_type == "Compras.completada":
            entry = 1 if self.entry1.get().lower() == "yes" else 0 if self.entry1.get().lower() == "no" else self.entry1.get()
        else:
            entry = self.entry1.get()
            
        data = find_value(entry, value_type, self.var.get(), self.reversed_status)
        if not data:
            return messagebox.showerror("Error Finding Value", f"{self.entry1.get()} value not found in Database")
        data_viewer = CryptoshopviewerApp(data)
        data_viewer.run()
    
    def total_profit_button(self):
        messagebox.showinfo("Transactions Total Profit", f"Total profit in USD: {total_profit()}")
    
    def complete_transaction_button(self):
        if self.entry1.get() and complete_transaction(self.entry1.get()):  
            messagebox.showinfo("Transaction Closed", f"The transaction with the id {self.entry1.get()} has been closed")
        else:
            messagebox.showerror("Error Finishing Transaction", f"The id {self.entry1.get()} does not belong to an open transaction in the Database")  
        
        
