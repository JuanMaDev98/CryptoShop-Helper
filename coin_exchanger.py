import tkinter as tk
import requests
from tkinter import messagebox
from version import version

url = "https://api.coingecko.com/api/v3/simple/price"
coins_dict = {
    "gamepass": "GPN",
    "neoxa": "NEOX",
    "satoxcoin": "SATOX"
}
class CoinExchanger:
    def __init__(self, pos, master=None):
        # build ui
        self.master = master
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.configure(height=200, width=200)
        self.toplevel1.geometry(pos)
        self.toplevel1.title("Coin Exchanger")
        self.toplevel1.protocol("WM_DELETE_WINDOW", self.close_wind)
        self.labelframe1 = tk.LabelFrame(self.toplevel1)
        self.labelframe1.configure(
            height=200, padx=5, text='TO USD', width=200)
        self.entry1 = tk.Entry(self.labelframe1)
        self.entry1.grid(column=0, row=0)
        self.button1 = tk.Button(self.labelframe1)
        self.button1.configure(text='GPN', width=8, command=lambda: self.to_usd("gamepass"))
        self.button1.grid(column=0, pady="5 0", row=1)
        self.button2 = tk.Button(self.labelframe1)
        self.button2.configure(text='NEOX', width=8, command=lambda: self.to_usd("neoxa"))
        self.button2.grid(column=0, pady="5 0", row=2)
        self.button3 = tk.Button(self.labelframe1)
        self.button3.configure(text='SATOX', width=8, command=lambda: self.to_usd("satoxcoin"))
        self.button3.grid(column=0, pady=5, row=3)
        self.labelframe1.grid(column=0, padx=3, pady=3, row=0)
        self.labelframe2 = tk.LabelFrame(self.toplevel1)
        self.labelframe2.configure(
            height=200, padx=5, text='FROM USD', width=200)
        self.entry3 = tk.Entry(self.labelframe2)
        self.entry3.pack(side="top")
        self.button4 = tk.Button(self.labelframe2)
        self.button4.configure(text='GPN', width=8, command= lambda: self.from_usd("gamepass"))
        self.button4.pack(pady="5 0", side="top")
        self.button5 = tk.Button(self.labelframe2)
        self.button5.configure(text='NEOX', width=8, command= lambda: self.from_usd("neoxa"))
        self.button5.pack(pady="5 0", side="top")
        self.button6 = tk.Button(self.labelframe2)
        self.button6.configure(text='SATOX', width=8, command= lambda: self.from_usd("satoxcoin"))
        self.button6.pack(pady=5, side="top")
        self.labelframe2.grid(column=1, padx=3, pady=3, row=0)
        
        label1 = tk.Label(self.toplevel1)
        label1.configure(text=version)
        label1.grid(column=1, row=1, sticky="e")

        # Main widget
        self.mainwindow = self.toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def close_wind(self):
        self.master.destroy()
        
    def to_usd(self, coin):
        global url
        global coins_dict
        params = {  
                "ids": f"{coin}",
                "vs_currencies": "USD"
        }
        response = requests.get(url, params = params)    
        
        if response.status_code == 200:
            data = response.json()
            coin_price = data[f"{coin}"]["usd"]
            messagebox.showinfo(f"{coins_dict[coin]} to USD", f"{coins_dict[coin]} = ${coin_price} \n{self.entry1.get()} {coins_dict[coin]} = {coin_price * float(self.entry1.get())}")
        else:
            messagebox.showerror("Internet Error", "Failed to retrieve data from the API")
    
    
    def from_usd(self, coin):
        global url
        global coins_dict
        params = {  
                "ids": f"{coin}",
                "vs_currencies": "USD"
        }
        response = requests.get(url, params = params)    
        
        if response.status_code == 200:
            data = response.json()
            coin_price = data[f"{coin}"]["usd"]
            messagebox.showinfo(f"USD to {coins_dict[coin]}", f"{coins_dict[coin]} = ${coin_price} \n{self.entry3.get()} USD = {float(self.entry3.get()) /coin_price} {coins_dict[coin]}")
        else:
            messagebox.showerror("Internet Error", "Failed to retrieve data from the API")
                
                


