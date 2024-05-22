import sqlite3 as sql
# sql connection and cursor identf
conn = sql.connect("Cafe.db")
cursor = conn.cursor()

# coffee class identification (according to coffee ingredients)
class Coffee(): 
    
    __doc__  = "This Class created for coffe type"

    def __init__(self,coffeeName,price,coffeeRate,water=0,milk = 0,milkFoam = 0,chocolate = 0,ice = 0 ):
        self.coffeeName = coffeeName
        self.price = price
        self.coffeeRate = coffeeRate
        self.water = water
        self.milk = milk
        self.milk_foam = milkFoam
        self.chocolate = chocolate
        self.ice = ice
        
# insert coffes in database

    def insertCoffees(self): 
        cursor.execute("""CREATE TABLE IF NOT EXISTS Coffees(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    CoffeeName TEXT,
                    Price INTEGER,                
                    CoffeeRate INTEGER,
                    WaterRate INTEGER,
                    MilkRate INTEGER,
                    MilkFoamRate INTEGER,
                    ChocolateRate INTEGER,
                    Ice BOOLEAN
        )""")
        for coffee in coffees:
            cursor.execute("""INSERT INTO Coffees(CoffeeName,Price,CoffeeRate,WaterRate,MilkRate,MilkFoamRate,ChocolateRate,Ice) VALUES (?,?,?,?,?,?,?,?)""",
                        (coffee.coffeeName,coffee.price,coffee.coffeeRate,coffee.water,coffee.milk,coffee.milk_foam,coffee.chocolate,coffee.ice))
        conn.commit()

    # percentage representation of ingredients in coffees
    def coffeeIngredients(self):
        cursor.execute("""SELECT * FROM Coffees""")
        coffees = cursor.fetchall()
        print("Coffee Menu And Ingredients")
        for coffee in coffees:
            print(f"""
    Name : {coffee[1]}
    Coofee Price : {coffee[2]}
    Coffee Rate : %{coffee[3]*100}
    Water  Rate : %{coffee[4]*100}
    Milk   Rate : %{coffee[5]*100}
    Milk Foam  Rate : %{coffee[6]*100}
    Chocolate  Rate : %{coffee[7]*100}
    ice  : {coffee[3] == True}
    """)
            print("-" * 40)



# coffee identification
espresso = Coffee("Espresso",30,0.8)                            
americano = Coffee("Americano",35,0.3,0.7)                      
iceAmericano = Coffee("Ice Americano",40,0.3,0.7,ice=1)       
latte = Coffee("Latte",45,0.2,0,0.6,0.2)                        
iceLatte = Coffee("Ice Latte",50,0.20,0.6,0.2,0,ice=1)             
cappucino = Coffee("Cappucino",42,0.2,0,0.2,0.6)                
mocha = Coffee("Mocha",55,0.3,0,0.4,0.1,0.2)                    

# create to list for loop
coffees  = [espresso,americano,iceAmericano,latte,iceLatte,cappucino,mocha]

