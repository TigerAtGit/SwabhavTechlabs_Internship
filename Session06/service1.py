import mysql.connector as mysql
try:
    mydb = mysql.connect(user = 'root', password = 'mysql27', host = '127.0.0.1', database = 'contactlist_app')
    print("Connected:", str(mydb.is_connected))

except Exception as exc:
    print('Not able to connect to database!')
    print('Exception occured :', exc)

def allContacts():
    '''Shows the list 
    of all contacts or 
    to retrieve all contacts'''
    mycursor = mydb.cursor()
    mycursor.execute('''SELECT * 
                        FROM CONTACT''')
    res = mycursor.fetchall()
    return res

def addContact(fname, lname, num, email, type):
    '''Add contact to 
    the database'''
    mycursor = mydb.cursor()
    sql = """INSERT INTO CONTACT 
            (FirstName, LastName, Contact_no, Email, Contact_type) 
            VALUES (%s, %s, %s, %s, %s)"""
    val = (fname, lname, num, email, type)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record successfully inserted.")

def removeContact(fname, lname):
    '''Remove contact from 
    the database'''
    mycursor = mydb.cursor()
    sql = "DELETE FROM CONTACT WHERE FirstName = %s AND LastName = %s"
    val = (fname, lname)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted.")

def updateContact(fname, lname, field, fno):
    '''Update contact'''
    mycursor = mydb.cursor()
    sql = ''
    val = ''
    if fno == 1:
        sql = "UPDATE CONTACT SET Contact_no = %s WHERE FirstName = %s AND LastName = %s"
        val = (field, fname, lname)
    elif fno == 2:
        sql = "UPDATE CONTACT SET Email = %s WHERE FirstName = %s AND LastName = %s"
        val = (field, fname, lname)
    elif fno == 3:
        sql = "UPDATE CONTACT SET Type = %s WHERE FirstName = %s AND LastName = %s"
        val = (field, fname, lname)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected.")


