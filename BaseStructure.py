# database ve giriş menüsünü farklı modüle al , günsonu tablosuna tarih ekle eğer gün adedi 7yi geçerse silsin 
# 3 - e bastığında kasayı kapat müşteri ismi istesin  farklı bir tabloya işlesin 

from dataBaseConnection import *
import datetime

# coffee class identification (according to coffee ingredients)
class Coffee(): 
    __doc__  = "This Class created for coffe type"
    
    def __init__(self,coffeeName,price,coffeeRate,water=0,milk = 0,milkFoam = 0,chocolate = 0,ice = 0):
        self.coffeeName = coffeeName
        self.price = price
        self.coffeeRate = coffeeRate
        self.water = water
        self.milk = milk
        self.milk_foam = milkFoam
        self.chocolate = chocolate
        self.ice = ice

    # Return Coffee size and price for bill 
    def cupSizeForPrice(self):
        price = self.price
        while True:
            # try:
                size = int(input(f"""
                Size For Cup                 
                {"-"*28}                            
                1- Tall (355ml)   : {self.price}
                                            
                2- Grande (473ml) : {self.price*1.15}
                                                
                3- Venti (591ml ) : {self.price*1.27}   
                
                Please choice for size : """))
                if size == 1:
                    return price
                if size == 2:
                    price *= 1.15
                    return price
                if size == 3:
                    price *= 1.27
                    return price
            # except:
            #     print("\nInvalid size Please choice from table ")

class Revenue(Coffee):
    __doc__ = "This Class Created For End of day Revenue"
    
    def __init__(self,coffeeName,price,revenue):

        self.revenue = revenue
        self.result = 0
        super().__init__(coffeeName,price,revenue)
    
    # Customer is Pay the Bill
    def isPaying(self):
        beenpaid = input("Has money been paid (Y/N):")
        while True :
            if beenpaid.capitalize() == "Y":
                print("""
        Payment Successful
        Returning to main menu...""")
                
                self.costumerName = input("please enter  customer name: ")
                return True
            if beenpaid.capitalize() == "N":
                print("""
        Payment Failed
        Returning to main menu... """)
                return False
            else: 
                print("\nPlease Select Y or N")
                return self.isPaying()



    # function to print bill on display
    def bill(self,result):
        conn
        VAT = 18
        print("-"*50)
        print(f"""
                Your Bill:      
                {result}     
                without VAT(Value-Added Tax ) : 
                {result/(1+VAT/100)}    
                """)
        print("-"*50)

        if self.isPaying():
            insertSales(result)

    # function that pulls prices from database and calculates total revenue 
    def revenueCalcuate(self): 
        # from cafeMenu import datas
        for data in getDatas():
            self.revenue += data[2]

        return self.revenue
    
    # Create table , Run CupSizeForPrice Function and return  
    def Revenue(self):
        createSalesTable()
        self.result = self.cupSizeForPrice()
        return self.result
       
    # Function to print Total End of Day Revenue to Display  
    def totalRevenue(self):
        print(f"""
     _ _ _ _ _ _ _ _ _ _ _ _ _ 
    |
    | DAILY TOTAL : {self.revenueCalcuate()}
    |_ _ _ _ _ _ _ _ _ _ _ _ _
""")
    dropSales()


# coffee identification for Ingredients  
espresso = Coffee("Espresso",30,0.8)
americano = Coffee("Americano",35,0.3,0.7)
iceAmericano = Coffee("Ice Americano",40,0.3,0.7,ice=1) 
latte = Coffee("Latte",45,0.2,0,0.6,0.2)       
iceLatte = Coffee("Ice Latte",50,0.2,0,0.6,0.2,ice=1)
cappucino = Coffee("Cappucino",42,0.2,0,0.2,0.6)   
mocha = Coffee("Mocha",55,0.3,0,0.4,0.1,0.2) 

# Coffe identification for Revenue (Total Price)
revenue = Revenue("",0,0)
espressoRevenue = Revenue(espresso.coffeeName,espresso.price,0)                          
americanoRevenue = Revenue(americano.coffeeName,americano.price,0)                    
latteRevenue = Revenue(latte.coffeeName,latte.price,0)                  
iceAmericanoRevenue = Revenue(iceAmericano.coffeeName,iceAmericano.price,0)       
icelatteRevenue = Revenue(iceLatte.coffeeName,iceLatte.price,0)              
cappucinoRevenue = Revenue(cappucino.coffeeName,cappucino.price,0)              
mochaRevenue = Revenue(mocha.coffeeName,mocha.price,0) 