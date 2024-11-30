import csv


def saveFile(data):
    try:
        with open('data.csv', 'a', newline='') as file:
            csvFile = csv.writer(file)
            csvFile.writerow(data)
    except Exception as e:
        print(f'There is an error {e}')

