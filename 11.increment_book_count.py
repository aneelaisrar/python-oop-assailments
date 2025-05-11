class Book:
    total_books = 0  # Class variable to keep track of total books

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Increment the total book count

# Adding books and incrementing count
book1 = Book()
book1.increment_book_count()

book2 = Book()
book2.increment_book_count()

# Display the total number of books
print("Total Books:", Book.total_books)
