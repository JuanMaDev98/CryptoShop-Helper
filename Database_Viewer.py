#!/usr/bin/python3
import tkinter as tk
from db_bridge import *


class CryptoshopviewerApp:
    def __init__(self, data, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=200, width=200)
        toplevel1.title("Database Viewer")
        
        labelframe1 = tk.LabelFrame(toplevel1)
        labelframe1.configure(
            height=200,
            text='CryptoShop Database',
            width=200)
        labelframe1.grid(column=0, row=0, sticky="nsew")
        
        labelframe2 = tk.LabelFrame(labelframe1)
        labelframe2.configure(height=200, width=20)
        labelframe2.grid(column=0, row=0, sticky="nsew")
        
        label1 = tk.Label(labelframe2)
        label1.configure(text='ID')
        label1.pack(ipady=8, side="top")
        

        labelframe3 = tk.LabelFrame(labelframe1)
        labelframe3.configure(height=200, width=200)
        
        label2 = tk.Label(labelframe3)
        label2.configure(text='Wallet')
        label2.pack(ipady=8, side="top")
        
        labelframe3.grid(column=1, row=0, sticky="nsew")
        labelframe4 = tk.LabelFrame(labelframe1)
        labelframe4.configure(height=200, width=200)
        label3 = tk.Label(labelframe4)
        label3.configure(text='Telegram User')
        label3.pack(ipady=8, side="top")
        labelframe4.grid(column=2, row=0, sticky="nsew")
        labelframe5 = tk.LabelFrame(labelframe1)
        labelframe5.configure(height=200, width=200)
        label4 = tk.Label(labelframe5)
        label4.configure(text='Quantity')
        label4.pack(ipady=8, side="top")
        labelframe5.grid(column=3, row=0, sticky="nsew")
        labelframe6 = tk.LabelFrame(labelframe1)
        labelframe6.configure(height=200, width=200)
        label5 = tk.Label(labelframe6)
        label5.configure(text='Original \nPrice')
        label5.pack(side="top")
        labelframe6.grid(column=4, row=0, sticky="nsew")
        labelframe7 = tk.LabelFrame(labelframe1)
        labelframe7.configure(height=200, width=200)
        label6 = tk.Label(labelframe7)
        label6.configure(text='Paid\nPrice')
        label6.pack(side="top")
        labelframe7.grid(column=5, row=0, sticky="nsew")
        labelframe8 = tk.LabelFrame(labelframe1)
        labelframe8.configure(height=200, width=200)
        label7 = tk.Label(labelframe8)
        label7.configure(text='Promo')
        label7.pack(ipady=8, side="top")
        labelframe8.grid(column=6, row=0, sticky="nsew")
        labelframe9 = tk.LabelFrame(labelframe1)
        labelframe9.configure(height=200, width=200)
        label8 = tk.Label(labelframe9)
        label8.configure(text='Date')
        label8.pack(ipady=8, side="top")
        labelframe9.grid(column=7, row=0, sticky="nsew")
        labelframe10 = tk.LabelFrame(labelframe1)
        labelframe10.configure(height=200, width=200)
        label9 = tk.Label(labelframe10)
        label9.configure(text='Item Bought')
        label9.pack(ipady=8, side="top")
        labelframe10.grid(column=8, row=0, sticky="nsew")
        labelframe11 = tk.LabelFrame(labelframe1)
        labelframe11.configure(height=200, width=200)
        label10 = tk.Label(labelframe11)
        label10.configure(text='Closed?')
        label10.pack(ipady=8, side="top")
        labelframe11.grid(column=9, row=0, sticky="nsew")

        # fill data from database
        row = 1
        column = 0
        for i in data:
            for j in i:
                labelframe = tk.LabelFrame(labelframe1, height=200, width=200)
                labelframe.grid(column=column, row=row, sticky="nsew")
                label = tk.Label(labelframe, text=j)
                label.pack(ipady=0, side="top")
                column += 1
            column = 0
            row += 1

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = CryptoshopviewerApp(find_all("Compras.id", 0))
    app.run()

