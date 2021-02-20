import mysql.connector as mysql
try:
    con = mysql.connect(user = 'root', password = 'mysql27', host = '127.0.0.1', database = 'world_x')
    print("Connected:", str(con.is_connected))
    code = input('Enter country code:')
    query = "SELECT * FROM COUNTRY WHERE CODE = '" + code +"'"
    print(query)
    mycursor = con.cursor()
    mycursor.execute(query)
    records = mycursor.fetchall()
    for row in records:
        print(row[0], row[1])

except Exception as exc:
    print(exc)

finally:
    if con.is_connected:
        con.close
    print('Connection closed')

print('Exit')