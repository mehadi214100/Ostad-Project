import addBook
import loadBooks
import viewBook
import updateBook
import delete

books = []
books = loadBooks.loadBooks(books)
while True:
    print('----------------------------')
    print('| Library Management System |')
    print('----------------------------')
    print('0. Exit')
    print('1. Add Book')
    print('2. View All Books')
    print('3. Update Books')
    print('4. Remove Books')
    op = int(input('Select your option : '))
    if op == 0:
        print('Thanks for using Library Management System')
        break
    elif op == 1:
        addBook.bookAdd()
    elif op == 2:
        viewBook.viewBooks()
    elif op == 3:
        updateBook.updateBooks()
    elif op == 4:
        delete.removeBooks()
    else:
        print('Invalid Option Select. Try again please ..!')
