import sqlite3 as sql

# sql connection and cursor identf
conn = sql.connect("Cafe.db")
cursor = conn.cursor()

def createSalesTable():

    cursor.execute("""CREATE TABLE IF NOT EXISTS Sales(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    CoffeeName TEXT,
                    CoffeePrice INTEGER  
                        )""")

def insertSales(result):
    # conn = sql.connect("Cafe.db")
    # cursor = conn.cursor()
    cursor.execute(f"""INSERT INTO Sales (CoffeePrice) VALUES ({result})""")
    conn.commit()

def dropSales():
    try:
        cursor.execute("""DROP TABLE Sales""")
        conn.commit()
        conn.close()
    except:
        print("Please Sale the Coffee")


def getCoffeeIngredients():
    cursor.execute("""SELECT * FROM Coffees""")
    coffees = cursor.fetchall()
    print("\nCoffee Menu And Ingredients")
    return coffees

# Fetch data for Total Price
def getDatas():
    try :
        cursor.execute("SELECT * FROM  Sales")
        datas = cursor.fetchall()
        return datas
    except:
        print("\nPlease Sale the Coffee")

def weeklyRevenue():
    cursor.execute("""CREATE TABLE IF NOT EXISTS WEEKLY(
                   DAY INTEGER,
                   PRICE INTEGER
    )""")
    conn.commit()

def insertDailyRevenue():
    cursor