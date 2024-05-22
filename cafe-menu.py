from Functions import *

#Cafe Main Menu
while True:
    choice = input("""
      _ _ _ _ _ _ _ _ _ _
    |                    |                   
    |    Welcome To My   |
    |        Cafe        |
    |                    |                   
    | - 0 Insert Coffees |
    |     Database       |
    |                    |
    | - 1 Ingredients    |
    |       Coffees      |
    |                    |
    | - 2 Americano      |
    |                    |
    | - 3 Ice            |
    |     Americano      |
    |                    |
    | - 4 Latte          |
    |                    |
    | - 5 Ice            |
    |     Latte          |
    |                    |
    | - 6 Espresso       |
    |                    |
    | - 7 Cappuccino     |
    |                    |
    | - 8 Mocha          |
    |                    |
    |    -1 for quit     |
    |       and your     |
    |         bill       |
    | _ _ _ _ _ _ _ _ _ _|
                   
Please select an choise   : """)
    if choice == "0":
        insertCoffees() 
    if choice == "1":
        coffeeIngredients()
    if choice == "2":
        result += americano.cupSizeForPrice()
    if choice == "3":
        result += iceAmericano.cupSizeForPrice()
    if choice == "4":
        result+=latte.cupSizeForPrice()
    if choice == "5":
        result+=iceLatte.cupSizeForPrice()
    if choice == "6":
        result+=espresso.cupSizeForPrice()
    if choice == "7":
        result+=cappucino.cupSizeForPrice()
    if choice == "8":
        result+=mocha.cupSizeForPrice()    
    if choice == "-1" :
        bill(result)
        break