import mysql.connector as mysql
try:
    mydb = mysql.connect(user = 'root', password = 'mysql27', host = '127.0.0.1', database = 'contactlist_app')
    print("Connected:", str(mydb.is_connected))

except Exception as exc:
    print('Not able to connect to database!')
    print('Exception occured :', exc)

def showAllContacts():
    '''Show all contacts 
    with address info'''
    mycursor = mydb.cursor()
    mycursor.execute('''SELECT FirstName,
                        LastName,
                        Contact_no,
                        Address,
                        City,
                        `Pin Code` 
                        FROM CONTACT CON,
                        CONTACT_ADDRESS CADD 
                        WHERE CON.ContactID = CADD.CID 
                        ORDER BY FirstName''')
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

def addAddress(fname, lname, address, city, pin):
    '''Add address(s) for 
    particular contact'''
    mycursor = mydb.cursor()
    sql1 = """SELECT @ID := ContactID 
            FROM CONTACT 
            WHERE FirstName = %s 
            AND LastName = %s"""
    val1 = (fname, lname)
    mycursor.execute(sql1, val1)
    res = mycursor.fetchall()
    sql2 = """INSERT INTO 
            CONTACT_ADDRESS
            VALUES(%s, %s, %s, %s)"""
    val2 = (res[0][0], address, city, pin)
    mycursor.execute(sql2, val2)
    mydb.commit()
    print(mycursor.rowcount, "record successfully inserted.")

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

def removeContact(fname, lname):
    '''Remove contact and 
    associated address'''
    mycursor = mydb.cursor()
    sql1 = """SELECT @ID := ContactID 
            FROM CONTACT 
            WHERE FirstName = %s 
            AND LastName = %s"""
    val1 = (fname, lname)
    mycursor.execute(sql1, val1)
    res = mycursor.fetchall()
    sql2 = """DELETE FROM 
            CONTACT_ADDRESS WHERE CID = %s"""
    val2 = (res[0][0],)
    mycursor.execute(sql2, val2)
    mydb.commit()
    print(mycursor.rowcount, "Address deleted successfully.")
    sql3 = """DELETE FROM CONTACT 
            WHERE FirstName = %s 
            AND LastName = %s"""
    val3 = (fname, lname)
    mycursor.execute(sql3, val3)
    mydb.commit()
    print(mycursor.rowcount, "Contact deleted successfully.")