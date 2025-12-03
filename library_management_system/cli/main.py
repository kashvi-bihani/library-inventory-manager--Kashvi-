from library_manager.inventory import LibraryInventory
from library_manager.book import Book


def main():
    inventory = LibraryInventory()
    inventory.load_from_file()

    while True:
        print("\n===== Library Management Menu =====")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        try:
            choice = input("Enter your choice (1–6): ").strip()
        except Exception:
            print("Input error! Try again.")
            continue

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter ISBN: ")
            inventory.add_book(Book(title, author, isbn))
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.is_available():
                book.issue()
                print("Book issued successfully!")
            else:
                print("Book unavailable or not found.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if book and not book.is_available():
                book.return_book()
                print("Book returned successfully!")
            else:
                print("Book not found or not issued.")

        elif choice == "4":
            inventory.display_all()

        elif choice == "5":
            keyword = input("Enter title or ISBN: ")
            book = inventory.search_by_title(keyword) or inventory.search_by_isbn(keyword)
            print(book if book else "No match found.")

        elif choice == "6":
            inventory.save_to_file()
            print("Bye! Data is saved successfully!.")
            break

        else:
            print("Invalid choice! Enter between 1–6.")


if __name__ == "__main__":
    main()
