import csv


def load(data):
    try:
        with open('data.csv', 'r') as file:
            csvData = csv.reader(file)
            for info in csvData:
                data.append(info)
        return data
    except Exception as e:
        print(f'Error {e}')
    return data
