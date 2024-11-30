import saveFile


def addContact(data):
    name = input('Enter Name : ').strip()
    email = input('Enter Mail : ')
    phone = input('Enter Phone Number : ')
    address = input('Enter Address : ')
    errors = []
    if name[0].isdigit():
        errors.append('The contact name must be a string. ')
    if not email.endswith('@gmail.com'):
        errors.append('Enter Valid Gmail')
    if not phone.isdigit():
        errors.append('The phone number must be an integer. ')
    for item in data:
        if phone in item:
            errors.append('Phone Number Already Exists')

    if len(errors) > 0:
        for error in errors:
            print(error)
    else:
        data = [name, email, phone, address]
        saveFile.saveFile(data)
        print('Contact added Successfully !!!')
