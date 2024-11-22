import csv
import loadBooks


def removeBooks():
    books = loadBooks.loadBooks([])

    if not books:
        print("No books available to remove.")
        return

    print("Available Books:")
    for index, book in enumerate(books, start=1):
        print(f"{index}. {book}")

    try:
        choice = int(input("Select the book number you want to remove: "))
        if choice < 1 or choice > len(books):
            print("Invalid selection. Please try again.")
            return

        selected_book = books[choice - 1]
        print(f"Are you sure you want to delete this book? {selected_book}")
        confirm = input("Type 'yes' to confirm: ").strip().lower()

        if confirm == 'yes':
            books.pop(choice - 1)

            with open('books.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                for book in books:
                    writer.writerow([
                        book['title'],
                        book['author'],
                        book['isbn'],
                        book['publishing_year'],
                        book['price'],
                        book['quantity']
                    ])
            print("Book removed successfully!")
        else:
            print("Operation canceled.")

    except ValueError:
        print("Invalid input. Please enter a valid book number.")
