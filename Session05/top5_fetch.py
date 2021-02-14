import mysql.connector as mysql
try:
    con = mysql.connect(user = 'root', password = 'mysql27', host = '127.0.0.1', database = 'world_x')
    print("Connected:", str(con.is_connected))

except Exception as exc:
    print(exc)

mycursor = con.cursor()
mycursor.execute('''SELECT COUNTRYCODE, 
                    CO.NAME, 
                    SUM(INFO->'$.Population') 
                    FROM CITY CT, COUNTRY CO 
                    WHERE CT.COUNTRYCODE = CO.CODE 
                    GROUP BY COUNTRYCODE 
                    ORDER BY SUM(INFO->'$.Population') 
                    DESC LIMIT 5''')
res = mycursor.fetchall()
for x in res:
    print(x)

if con.is_connected:
    con.close
print('Connection closed. Exit')
