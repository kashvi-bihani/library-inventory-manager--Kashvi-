import unittest
from library_manager.inventory import LibraryInventory
from library_manager.book import Book

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        inv = LibraryInventory()
        inv.add_book(Book("ABC", "XYZ", "123"))
        self.assertEqual(len(inv.books), 1)

if __name__ == "__main__":
    unittest.main()

