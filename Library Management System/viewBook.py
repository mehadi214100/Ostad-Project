import loadBooks


def viewBooks():
    books = loadBooks.loadBooks([])
    if books:
        sl = 1
        for book in books:
            print(sl, '.', book)
            sl = sl + 1
    else:
        print('Book List is Empty ....please add book ')
