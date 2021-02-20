import service2 as ser2
print('CONTACT and ADDRESS LIST APP')
print('\n')
print("1.Show all contacts and their address(s)")
print("2.Add contact")
print("3.Add address")
print("4.Update contact")
print("5.Remove contact and its asscociated address")

opt = int(input('Select your option:'))

if opt == 1:
    contacts = ser2.showAllContacts()
    for contact in contacts:
        print(contact)

elif opt == 2:
    print('Enter contact details')
    fn = input('Enter first name: ')
    ln = input('Enter last name: ')
    no = input('Enter contact number: ')
    em = input('Enter email: ')
    ty = input('Enter type: ')
    ser2.addContact(fn, ln, no, em, ty)

elif opt == 3:
    print('Enter contact details and address details')
    fn = input('Enter first name: ')
    ln = input('Enter last name: ')
    addr = input('Enter address: ')
    city = input('Enter city name: ')
    pinc = input('Enter pincode: ')
    ser2.addAddress(fn, ln, addr, city, pinc)

elif opt == 4:
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
    ser2.updateContact(fn, ln, field, field_no)

elif opt == 5:
    print('Enter details of contact to be deleted')
    fn = input('Enter first name of contact: ')
    ln = input('Enter last name of contact: ')
    ser2.removeContact(fn, ln)

else:
    print('No valid option selected !')

