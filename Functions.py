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
# create table and insert variable 
    def insertDatabase(self): 
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
        cursor.execute("""INSERT INTO Coffees(CoffeeName,Price,CoffeeRate,WaterRate,MilkRate,MilkFoamRate,ChocolateRate,Ice) VALUES (?,?,?,?,?,?,?,?)""",
                (self.coffeeName,self.price,self.coffeeRate,self.water,self.milk,self.milk_foam,self.chocolate,self.ice))
        conn.commit()



    # Return Coffee size and price for bill 
    def cupSizeForPrice(self):
        while True:
            size = input(f"""
            Size For Cup                 
            {"-"*28}                            
            1- Tall (355ml)   : {self.price}
                                        
            2- Grande (473ml) : {self.price*1.15}
                                              
            3- Venti (591ml ) : {self.price*1.27}   
            
            Please choice for size : """)
            if size == "1":
                return self.price
            if size == "2":
                self.price*=1.15
                return self.price
            if size == "3":
                self.price*=1.27
                return self.price
            else:
                print("Invalid size Please choice from table ")

# insert coffee in database       
def insertCoffees():
    coffees  = [espresso,americano,iceAmericano,latte,iceLatte,cappucino,mocha]
    for coffee in coffees:
            coffee.insertDatabase()
    print("Coffees insert to database successfully! ")

# percentage representation of ingredients in coffees
def coffeeIngredients():
    cursor.execute("""SELECT * FROM Coffees""")
    coffees = cursor.fetchall()
    print("\nCoffee Menu And Ingredients")
    for coffee in coffees:
        print(f"""
    Name : {coffee[1]}
    Coofee Price : {coffee[2]}
    Coffee Rate : %{coffee[3]*100}
    Water  Rate : %{coffee[4]*100}
    Milk   Rate : %{coffee[5]*100}
    Milk Foam  Rate : %{coffee[6]*100}
    Chocolate  Rate : %{coffee[7]*100}
    ice  : {coffee[8] == True}
    """)
        print("-" * 40)

# function to print bill on display
def bill(result):
    VAT = 18
    print("-"*50)
    print(f"""
            Your Bill:      
            {result}     
            without VAT(Value-Added Tax ) : 
            {result/(1+VAT/100)}    
            """)
    print("-"*50)

# coffee identification
espresso = Coffee("Espresso",30,0.8)                            
americano = Coffee("Americano",35,0.3,0.7)                      
iceAmericano = Coffee("Ice Americano",40,0.3,0.7,ice=1)       
latte = Coffee("Latte",45,0.2,0,0.6,0.2)                        
iceLatte = Coffee("Ice Latte",50,0.2,0,0.6,0.2,ice=1)             
cappucino = Coffee("Cappucino",42,0.2,0,0.2,0.6)                
mocha = Coffee("Mocha",55,0.3,0,0.4,0.1,0.2) 

#result for bill
result = 0 