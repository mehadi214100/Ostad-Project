import csv


def saveBook(book):
    with open('books.csv', 'a', newline='') as fp:
        writer = csv.writer(fp)
        myBook = [
            book['title'],
            book['author'],
            book['isbn'],
            book['publishing_year'],
            book['price'],
            book['quantity']
        ]
        writer.writerow(myBook)

