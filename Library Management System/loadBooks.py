import csv


def loadBooks(books):
    try:
        with open('books.csv', 'r') as file:
            myFile = csv.reader(file)
            for book in myFile:
                mybook = {
                    'title': book[0],
                    'author': book[1],
                    'isbn': book[2],
                    'publishing_year': book[3],
                    'price': book[4],
                    'quantity': book[5]
                }
                books.append(mybook)
    except FileNotFoundError:
        books = []
    return books
