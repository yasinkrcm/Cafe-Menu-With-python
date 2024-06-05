import sqlite3 as sql

# Connection For Database
def connectDatabase():
    conn = sql.connect("Cafe.db")
    cursor = conn.cursor()
    return conn, cursor

# Show Coffee Ingredients
def getCoffeeIngredients():
    conn, cursor = connectDatabase()
    cursor.execute("""SELECT * FROM Coffees""")
    coffees = cursor.fetchall()
    print("\nCoffee Menu And Ingredients")
    conn.close()
    return coffees

# Create Table For Daily and Weekly Revenue
def createTable():
    conn, cursor = connectDatabase()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Daily(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    CoffeeName TEXT,
                    CoffeePrice INTEGER  
                        )""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS WEEKLY(
                   DAY INTEGER,
                   REVENUE INTEGER
    )""")

    conn.commit()
    conn.close()

# Add Daily sale
def insertDaily(result):
    conn, cursor = connectDatabase()
    cursor.execute(f"""INSERT INTO Daily (CoffeePrice) VALUES ({result})""")
    conn.commit()
    conn.close()

# Show Daily Datas
def getDailyDatas():
        conn, cursor = connectDatabase()
        cursor.execute("SELECT * FROM Daily")
        datas = cursor.fetchall()
        conn.close()
        return datas

# Daily Table Delete
def dropDaily():
    conn, cursor = connectDatabase()
    try:
        cursor.execute("""DROP TABLE Daily""")
        conn.commit()
    except:
        print("Please Sale the Coffee")
    finally:
        conn.close()

# Insert Daily Sales For Weekly
def insertDailyRevenue(datas, dailyRevenue,day):
    try:
        conn, cursor = connectDatabase()
        for data in datas:
            dailyRevenue += data[2]
        dailyRevenue = dailyRevenue/2
        cursor.execute("""INSERT INTO WEEKLY (DAY,REVENUE) VALUES (?,?) """ , (day, dailyRevenue))   
        conn.commit()
        conn.close()
    except:
        print("Please Choice Daily Revenue")

# Get Weekly Revenue
def getWeeklyRevenue():
    try:
        TotalRevenue = 0 
        conn, cursor = connectDatabase()
        cursor.execute("""SELECT * FROM WEEKLY WHERE REVENUE""")
        weeklyRevenue = cursor.fetchall()
        for data in weeklyRevenue:
            TotalRevenue += data[1]
        print(f"""
            
             _ _ _ _ _ _ _ _ _ _ _ _
            |
            |   
            |  TOTAL WEEKLY REVENUE : {TotalRevenue}
            |       
            |_ _ _ _ _ _ _ _ _ _ _ _
    """)
        cursor.execute("""DROP TABLE WEEKLY""")
        conn.commit()
        conn.close()
    except:
        print("Please Choice Daily Revenue")