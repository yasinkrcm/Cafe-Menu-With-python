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

class Coffee(): 

    def __init__(self,coffeeName,coffeeRate,price,water=0,milk = 0,milkFoam = 0,chocolate = 0,ice = 0 ):
        self.coffeeName = coffeeName
        self.coffeeRate = coffeeRate
        self.price = price
        self.water = water
        self.milk = milk
        self.milk_foam = milkFoam
        self.chocolate = chocolate
        self.ice = ice
        
espresso = Coffee("espresso",0.8,30)
americano = Coffee("americano",0.3,35,0.7)
iceAmericano = Coffee("Ice Americano",0.3,40,0.7,0,0,0,1)
latte = Coffee("latte",0.2,45,0,0.6,0.2)
iceLatte = Coffee("Ice Latte",0.2,50,0,0.6,0.2,0,1)
cappucino = Coffee("cappucino",0.2,42,0,0.2,0.6)
mocha = Coffee("mocha",0.3,55,0,0.4,0.1,0.2)

coffees  = [espresso,americano,iceAmericano,latte,iceLatte,cappucino,mocha]

cursor.execute("""CREATE TABLE IF NOT EXISTS Coffees(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               CoffeeRate INTEGER,
               Price INTEGER,
               WaterRate INTEGER,
               MilkRate INTEGER,
               MilkFoamRate INTEGER,
               ChocolateRate INTEGER,
               Ice BOOLEAN
)""")
for coffee in coffees:
    cursor.execute("""INSERT INTO Coffees(CoffeeRate,Price,WaterRate,MilkRate,MilkFoamRate,ChocolateRate,Ice) VALUES (?,?,?,?,?,?,?)""",
                   (coffee.coffeeName,coffee.price,coffee.water,coffee.milk,coffee.milk_foam,coffee.chocolate,coffee.ice))

conn.commit()
conn.close()

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
                   
Please select an choise   : """)
    
    if choice == "-1" :
        print(choice)
        break
    # if 