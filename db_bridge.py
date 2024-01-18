import sqlite3
from date_time_parser import date_time_decode, date_time_encode

'''
cursor.execute("""
        SELECT Compras.id, Compras.wallet, Compras.tlg_user, Compras.cantidad, Compras.precio_original, 
        Compras.precio_pagado, Promos.promo, Compras.fecha, Compras.completada FROM Compras JOIN Promos ON 
        Compras.promo_id = Promos.id
    """)
'''

def add_buy(wallet, tlg_user, cantidad, precio_original, precio_pagado, promo_id, fecha, item_id, completada):
    conn = sqlite3.connect('Cryptoshop.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Compras(wallet, tlg_user, cantidad, precio_original, precio_pagado, promo_id, fecha, item_id, completada) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (wallet, tlg_user, cantidad, precio_original, precio_pagado, promo_id, fecha, item_id, completada))
    
    conn.commit()
    conn.close()


def add_promo(value):
    conn = sqlite3.connect('Cryptoshop.db')
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO Promos(promo) VALUES (?)", (value,))

    conn.commit()
    conn.close()


def get_promo_list():
    conn = sqlite3.connect('Cryptoshop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT promo FROM Promos")
    promos = cursor.fetchall()
    
    data = []
    for promo in promos:
        data.append(promo[0])

    conn.close()
    return data

def get_promo_id(value):
    conn = sqlite3.connect('Cryptoshop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Promos WHERE promo = ? LIMIT 1", (value,))
    promo_id = cursor.fetchone()
    conn.close()
    return promo_id[0]

    
    
def add_item(value):
    conn = sqlite3.connect('Cryptoshop.db')
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO Items(item) VALUES (?)", (value,))

    conn.commit()
    conn.close()


def get_item_list():
    conn = sqlite3.connect('Cryptoshop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT item FROM Items")
    items = cursor.fetchall()
    
    data = []
    for item in items:
        data.append(item[0])

    conn.close()
    return data


def get_item_id(value):
    conn = sqlite3.connect('Cryptoshop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Items WHERE item = ? LIMIT 1", (value,))
    item_id = cursor.fetchone()
    conn.close()
    return item_id[0]


def find_all(order_key, order=0):
    order = "DESC" if order else "ASC"
    conn = sqlite3.connect('Cryptoshop.db')
    cursor = conn.cursor()
    cursor.execute(f"""SELECT Compras.id, Compras.wallet, Compras.tlg_user, Compras.cantidad, Compras.precio_original, 
        Compras.precio_pagado, Promos.promo, Compras.fecha, Items.item, Compras.completada FROM Compras JOIN Promos JOIN Items ON 
        Compras.promo_id = Promos.id AND Compras.item_id = Items.id ORDER BY {order_key} {order}""")
    items = cursor.fetchall()

    data = []
    for item in items:
        item = list(item)
        item[7] = date_time_decode(item[7])
        item[9] = "YES" if item[9] == 1 else "NO"
        data.append(item)
        
    conn.close()
    return data


def find_value(value, value_type, order_key, order=0):
    order = "DESC" if order else "ASC"
    conn = sqlite3.connect('Cryptoshop.db')
    cursor = conn.cursor()
    cursor.execute(f"""SELECT Compras.id, Compras.wallet, Compras.tlg_user, Compras.cantidad, Compras.precio_original, 
        Compras.precio_pagado, Promos.promo, Compras.fecha, Items.item, Compras.completada FROM Compras JOIN Promos JOIN Items ON 
        Compras.promo_id = Promos.id AND Compras.item_id = Items.id WHERE {value_type} LIKE (?) ORDER BY {order_key} {order}""", (value,))
    items = cursor.fetchall()

    data = []
    for item in items:
        item = list(item)
        item[7] = date_time_decode(item[7])
        item[9] = "YES" if item[9] == 1 else "NO"
        data.append(item)
    
    conn.close()
    return data

def total_profit():
    data = find_all("Compras.id")
    original_price = 0
    paid_price = 0
    for sell in data:
        original_price += sell[4]
        paid_price += sell[5]
    return paid_price - original_price


def complete_transaction(id):
    conn = sqlite3.connect('Cryptoshop.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Compras SET completada = 1 WHERE id = ? AND completada = 0", (id,))
    conn.commit()
    conn.close()
    return cursor.rowcount














