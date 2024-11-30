import csv

import Viewdata


def remove(data):
    print('Available data')
    print('---------------')
    Viewdata.view(data)
    op = input('Choose which contact want to delete : ')
    if op.isdigit():
        try:
            op = int(op)
            info = data[op - 1]
            confirm = input(f'Your data is {info}\nAre Your confirm (y/n) : ')
            if confirm.lower() == 'y':
                data.pop(op - 1)
                with open('data.csv', 'w', newline='') as file:
                    csvFile = csv.writer(file)
                    csvFile.writerows(data)
                print('Remove Successful !!!')
        except Exception as e:
            print(f'Error {e}')

    else:
        print('Wrong Input')
    return data
