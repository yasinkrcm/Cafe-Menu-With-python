from BaseStructure import *

# percentage representation of ingredients in coffees
def coffeeIngredients():
    for coffee in getCoffeeIngredients():
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
    print("Returning to main menu...")

# Choice coffee for costumer
def coffeeChoice():  
    choiseCoffe = input("""
      _ _ _ _ _ _ _ _ _ _
    |                    |                   
    | - 1 Americano      |
    |                    |
    | - 2 Ice            |
    |     Americano      |
    |                    |
    | - 3 Latte          |
    |                    |
    | - 4 Ice            |
    |     Latte          |
    |                    |
    | - 5 Espresso       |
    |                    |
    | - 6 Cappuccino     |
    |                    |
    | - 7 Mocha          |
    | _ _ _ _ _ _ _ _ _ _|
    Please choice a coffee : """)

    if choiseCoffe == "1":
        return americanoRevenue.Revenue()
    if choiseCoffe == "2":
        return iceAmericanoRevenue.Revenue()
    if choiseCoffe == "3":
        return latteRevenue.Revenue()
    if choiseCoffe == "4":
        return icelatteRevenue.Revenue()
    if choiseCoffe == "5":
        return espressoRevenue.Revenue()
    if choiseCoffe == "6":
        return cappucinoRevenue.Revenue()
    if choiseCoffe == "7":
        return mochaRevenue.Revenue()
    else:
        print("\nPlease Choice a number on the table")
        return coffeeChoice()

# Main Menu And First Message
def firstMessage(result):
    day = 0 
    isContinue = True
    if isContinue:
        while True:

            choice = input("""
         _ _ _ _ _ _ _ _ _ _
        |                    |                   
        |    Welcome To My   |
        |        Cafe        |
        |                    |
        | - 1 Ingredients    |
        |       Coffees      |
        |                    |                
        | - 2 New Costumer   |
        |                    |
        | - 3 Daily          |
        |     Revenue        |
        |                    |
        | - 4 Weekly         |
        |     Revenue        |
        | _ _ _ _ _ _ _ _ _ _|
                        
        Please choice a menu : """)
            
            if choice == "1":
                coffeeIngredients()
            elif choice == "2":
                try :
                    howManyPeople = int(input("How many costumer : "))
                    while howManyPeople > 0:
                        result = coffeeChoice()
                        howManyPeople -= 1
                        revenue.bill(result)
                except : 
                    print("Please insert a number")

            elif choice == "3":
                day += 1 
                if day > 7:
                    print("Please Choice Weekly Revenue")
                else:
                    revenue.totalRevenue(day)
            elif choice == "4":
                getWeeklyRevenue()
                isContinue = False
                print("Program is closing...")
                break

            else:
                print("\nPlease Choice number on the Menu")

if __name__ == "__main__":
    result = 0 
    firstMessage(result)
