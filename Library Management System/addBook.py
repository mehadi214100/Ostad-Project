import savebook


def bookAdd():
    title = input('Book Title : ')
    author = input('Author Name : ')
    isbn = int(input('ISBN No : '))
    publishing_year = int(input('Publish Year : '))
    price = float(input('Price : '))
    quantity = int(input('Quantity : '))
    book = {
        'title': title,
        'author': author,
        'isbn': isbn,
        'publishing_year': publishing_year,
        'price': price,
        'quantity': quantity
    }
    savebook.saveBook(book)
    print('Book Added Successfully !!!')

