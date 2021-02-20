import service1 as ser
print('CONTACT LIST APP')
print('\n')
print("1.Show all contacts")
print("2.Add contact")
print("3.Update contact")
print("4.Remove contact")

opt = int(input('Select your option:'))
if opt == 1:
    contacts = ser.allContacts()
    for contact in contacts:
        print(contact)

elif opt == 2:
    print('Enter contact details')
    fn = input('Enter first name: ')
    ln = input('Enter last name: ')
    no = input('Enter contact number: ')
    em = input('Enter email: ')
    ty = input('Enter type: ')
    ser.addContact(fn, ln, no, em, ty)

elif opt == 3:
    print('Which field do you want to update:')
    print("1.Contact number \t2.Email \t3.Type")
    field_no = int(input('Your selection: '))
    fn = input('Enter first name related to contact: ')
    ln = input('Enter last name related to contact: ')
    if field_no == 1:
        field = input('Enter new contact number: ')
    elif field_no == 2:
        field = input('Enter new email id: ')
    elif field_no == 3:
        field = input('Enter new type for contact: ')
    ser.updateContact(fn, ln, field, field_no)

elif opt == 4:
    fn = input('Enter first name of contact: ')
    ln = input('Enter last name of contact: ')
    ser.removeContact(fn, ln)

else:
    print('No valid option selected !')