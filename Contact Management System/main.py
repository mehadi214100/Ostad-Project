import addContact
import loadData
import Viewdata
import search
import remove

data = loadData.load([])
while True:
    print('--------------------------')
    print('Contact Management System')
    print('--------------------------')
    print('1.Add Contacts')
    print('2.View Contacts')
    print('3.Search Contacts')
    print('4.Remove Contacts')
    print('5.Exit')
    op = input('Select a Option : ')
    if op == '1':
        addContact.addContact(data)
        data = loadData.load([])
    elif op == '2':
        Viewdata.view(data)
    elif op == '3':
        search.searchDta(data)
    elif op == '4':
        data = remove.remove(data)

    elif op == '5':
        print('Thanks for using our system')
        break
    else:
        print('Wrong input Please try again')
