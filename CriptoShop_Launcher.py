import tkinter
import Database_Insert_GUI, Database_Read_GUI, coin_exchanger

main_window = tkinter.Tk()
main_window.title("CryptoShop Helper")
main_window.withdraw()
windows1 = Database_Insert_GUI.DatabaseInsert("+600+300", main_window)
windows2 = Database_Read_GUI.DatabaseReader("+1000+300", main_window)
windows3 = coin_exchanger.CoinExchanger("+800+100", main_window)
main_window.mainloop()