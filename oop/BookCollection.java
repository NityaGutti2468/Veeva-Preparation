import java.util.HashMap;
import java.util.Map;

public class BookCollection {
    static class Book {
        private final String isbn;
        private final String title;
        private final String author;
        private final double price;

        Book(String isbn, String title, String author, double price) {
            this.isbn = isbn;
            this.title = title;
            this.author = author;
            this.price = price;
        }

        @Override
        public String toString() {
            return "ISBN: " + isbn + ", Title: " + title
                    + ", Author: " + author + ", Price: " + price;
        }
    }

    private final Map<String, Book> booksByIsbn = new HashMap<>();

    public void addBook(Book book) {
        if (booksByIsbn.putIfAbsent(book.isbn, book) != null) {
            throw new IllegalArgumentException("Duplicate ISBN: " + book.isbn);
        }
    }

    public Book findByIsbn(String isbn) {
        return booksByIsbn.get(isbn);
    }
}
