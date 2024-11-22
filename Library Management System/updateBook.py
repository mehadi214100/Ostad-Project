import csv
import loadBooks


def updateBooks():
    books = loadBooks.loadBooks([])

    if not books:
        print("No books available to update.")
        return

    print("Available Books:")
    for index, book in enumerate(books, start=1):
        print(f"{index}. {book}")

    try:
        choice = int(input("Select the book number you want to update: "))
        if choice < 1 or choice > len(books):
            print("Invalid selection. Please try again.")
            return

        selected_book = books[choice - 1]

        print("Selected Book:")
        print(selected_book)

        for field in selected_book:
            new_value = input(f"Update {field} (leave empty to keep current: {selected_book[field]}): ")
            if new_value.strip():
                selected_book[field] = new_value

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

        print("Book updated successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid book number.")
