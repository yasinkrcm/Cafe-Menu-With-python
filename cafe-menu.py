# Python'da class yapısı kullanarak ,

# DB VE CLASS KULLAN

# Kafe'de self-servis bir menü oluştur; Kahve satan bir Kafe oluştur , 

# Fiş ile hesabı oluştur.

# İçeceklerin boyutu olacak

# İçeceklerin Tür , Sıcak veya soğukluğu 

# Süt'ün türleri 

# Krema vs 

# *   5 çeşit kahvesi var
#     (class ve kalıtım)

# Ammericano 
# latte
# espresso
# cappucino
# mocha

# *   kişi menüden bir kahve alarak kasa hesap yapıp fiş kesecek  
#     (alınan kahve - fiyatı - fiş oluştur - fişe brüt ve net fiyatı [KDVLİ - KDVSİZ])

import sqlite3 as sql

conn = sql.connect("Cafe.db")
cursor = conn.cursor()

while True:
    choice = input("""
      _ _ _ _ _ _ _ _ _ _
    |                    |                   
    |    Welcome To My   |
    |        Cafe        |                   
    |                    |
    | - 1 Americano      |
    | - 2 Latte          |
    | - 3 Espresso       |
    | - 4 Cappuccino     |
    | - 5 Mocha          |
    |                    |
    |   -1 for quit      |
    | _ _ _ _ _ _ _ _ _ _|
                   
Please select an choise   : 
""")
    