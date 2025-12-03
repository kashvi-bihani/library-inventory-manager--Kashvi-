import json
import logging
from pathlib import Path
from library_management_system.library_manager.book import Book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LibraryInventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        return [book for book in self.books if book.title.lower() == title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        if not self.books:
            print("No books in the inventory.")
        else:
            for book in self.books:
                print(book)

    def save_to_file(self, filename="library_data.json"):
        try:
            with open(filename, "w") as f:
                json.dump([book.to_dict() for book in self.books], f, indent=4)
            print("Books saved successfully!")
            logging.info("Library data saved to file.")
        except Exception as e:
            print("Error while saving file.")
            logging.error(f"Error saving file: {e}")
        finally:
            print("Save attempt complete.")

    def load_from_file(self, filename="library_data.json"):
        try:
            if not Path(filename).exists():
                print("No previous data found — starting fresh.")
                logging.info("Started with a new empty library.")
                return
            with open(filename, "r") as f:
                data = json.load(f)
                self.books = [Book(**item) for item in data]
            print("Data loaded successfully!")
            logging.info("Library data loaded from file.")
        except Exception as e:
            print("Error while loading file — starting with empty library.")
            logging.error(f"Error loading file: {e}")
        finally:
            print("Load attempt complete.")
