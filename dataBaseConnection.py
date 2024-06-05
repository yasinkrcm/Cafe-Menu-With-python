import sqlite3 as sql

# Veritabanı bağlantısı oluşturma
def connectDatabase():
    conn = sql.connect("Cafe.db")
    cursor = conn.cursor()
    return conn, cursor

# Tablo oluşturma
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

# Günlük satış ekleme
def insertDaily(result):
    conn, cursor = connectDatabase()
    cursor.execute(f"""INSERT INTO Daily (CoffeePrice) VALUES ({result})""")
    conn.commit()
    conn.close()

# Günlük tablosunu silme
def dropDaily():
    conn, cursor = connectDatabase()
    try:
        cursor.execute("""DROP TABLE Daily""")
        conn.commit()
    except:
        print("Please Sale the Coffee")
    finally:
        conn.close()

# Kahve İçeriklerini Getirme
def getCoffeeIngredients():
    conn, cursor = connectDatabase()
    cursor.execute("""SELECT * FROM Coffees""")
    coffees = cursor.fetchall()
    print("\nCoffee Menu And Ingredients")
    conn.close()
    return coffees
    
# Günlük Verileri Getirme
def getDailyDatas():
        conn, cursor = connectDatabase()
        cursor.execute("SELECT * FROM Daily")
        datas = cursor.fetchall()
        conn.close()
        return datas

    
# Günlük Geliri Ekleme
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
# Haftalık Geliri Getirme
def getWeeklyRevenue():
    try:
        TotalRevenue = 0 
        conn, cursor = connectDatabase()
        cursor.execute("""SELECT * FROM WEEKLY WHERE REVENUE""")
        weeklyRevenue = cursor.fetchall()
        for data in weeklyRevenue:
            print(data[1])
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


# import sqlite3 as sql

# # sql connection and cursor identf
# def connectDatabase(conn=None,cursor=None):
#     if conn:
#         conn = sql.connect("Cafe.db")
#         return conn
#     if cursor :
#         conn = sql.connect("Cafe.db")
#         cursor = conn.cursor()
#         return cursor

        
    


# def createTable():
#     conn = connectDatabase(True)
#     cursor = connectDatabase(cursor=True)
#     cursor.execute("""CREATE TABLE IF NOT EXISTS Daily(
#                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                     CoffeeName TEXT,
#                     CoffeePrice INTEGER  
#                         )""")
    
#     cursor.execute("""CREATE TABLE IF NOT EXISTS WEEKLY(
#                    DAY INTEGER,
#                    REVENUE INTEGER
#     )""")
#     conn.commit()
#     conn.close()

# def insertDaily(result):
#     conn = connectDatabase(True)
#     cursor = connectDatabase(cursor=True)
#     # conn = sql.connect("Cafe.db")
#     # cursor = conn.cursor()
#     cursor.execute(f"""INSERT INTO Daily (CoffeePrice) VALUES ({result})""")
#     print("result : ", result)
#     conn.commit()
#     conn.close()

# def dropDaily():
#     conn = connectDatabase(True)
#     cursor = connectDatabase(cursor=True)
#     try:
#         cursor.execute("""DROP TABLE daily""")
#         conn.commit()
#         conn.close()
#     except:
#         print("Please Sale the Coffee")


# def getCoffeeIngredients():
#     cursor = connectDatabase(cursor=True)
#     cursor.execute("""SELECT * FROM Coffees""")
#     coffees = cursor.fetchall()
#     print("\nCoffee Menu And Ingredients")
#     return coffees
    

# # Fetch data for Total Price
# def getDailyDatas():
#         conn = connectDatabase(True)
#         cursor = connectDatabase(cursor=True)
#         cursor.execute("SELECT * FROM  Sales")
#         datas = cursor.fetchall()
#         print(datas)
#         conn.commit()
#         conn.close()
#         return datas
    
# def insertDailyRevenue(datas,dailyRevenue,day):
#     cursor = connectDatabase(cursor=True)
#     for data in datas:
#         print("data1:",data[1])
#         dailyRevenue += data[1]
#     cursor.execute("""INSERT INTO WEEKLY (DAY,REVENUE) VALUES (?,?) """ , (day,dailyRevenue))   

# def getWeeklyRevenue():
#     conn = connectDatabase(True)
#     cursor = connectDatabase(cursor=True)
#     cursor.execute("""SELECT * FROM WEEKLY WHERE REVENUE""")
#     weeklyRevenue = cursor.fetchall()
#     print(weeklyRevenue)
#     conn.commit()
#     conn.close()

# # def insertDailyRevenue(daily):
# #     conn = connectDatabase(True)
# #     cursor = connectDatabase(cursor=True)

    
