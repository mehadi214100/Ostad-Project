def searchDta(data):

    print('->1.Name')
    print('->2.Email')
    print('->3.Number')
    op = input('Search by : ')
    information = []
    try:
        if op == '1':
            name = input('Enter Name : ')
            for item in data:
                if item[0].lower().startswith(name.lower()):
                    information.append(item)
        elif op == '2':
            email = input('Enter Email : ')
            for item in data:
                if email in item:
                    information.append(item)
        elif op == '3':
            number = input('Enter Number : ')
            for item in data:
                if number in item:
                    information.append(item)
        else:
            print('Wrong Input')
            return
        if len(information) > 0:
            for info in information:
                print(info)
        else:
            print('No contact Found')

    except Exception as e:
        print(f'Error {e}')
