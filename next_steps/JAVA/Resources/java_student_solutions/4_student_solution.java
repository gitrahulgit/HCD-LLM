import java.io.*;
import java.util.*;
class LibraryException extends Exception {
    public LibraryException(String message) {
        super(message);
    }
}
class Book {
    private String id;
    private String title;
    private boolean available;
    public Book(String id, String title) {
        this.id = id;
        this.title = title;
        this.available = true;
    }
    public String getId() { return id; }
    public boolean isAvailable() { return available; }
    public void setAvailable(boolean available) { this.available = available; }
    @Override
    public String toString() {
        return id + ": \"" + title + "\" - " + (available ? "Available" : "Unavailable");
    }
}
class Borrower {
    private String id;
    private String name;
    private List<String> borrowedBooks;
    public Borrower(String id, String name) {
        this.id = id;
        this.name = name;
        this.borrowedBooks = new ArrayList<>();
    }
    public void borrowBook(String bookId) {
        borrowedBooks.add(bookId);
    }
    public void returnBook(String bookId) throws LibraryException {
        if (!borrowedBooks.remove(bookId)) {
            throw new LibraryException("Book not borrowed by this borrower.");
        }
    }
    public List<String> getBorrowedBooks() { return borrowedBooks; }
}
class LibrarySystem {
    private Map<String, Book> books;
    private Map<String, Borrower> borrowers;
    public LibrarySystem() {
        books = new HashMap<>();
        borrowers = new HashMap<>();
    }
    public void borrowBook(String borrowerId, String bookId) throws LibraryException {
        Borrower borrower = borrowers.get(borrowerId);
        Book book = books.get(bookId);
        if (borrower == null) throw new LibraryException("Borrower not found.");
        if (book == null) throw new LibraryException("Book not found.");
        borrower.borrowBook(bookId);
        book.setAvailable(false);
    }
}
public class LibraryApp {
    public static void main(String[] args) {
        LibrarySystem library = new LibrarySystem();
        try {
            library.addBook(new Book("101", "Data Structures"));
            library.registerBorrower(new Borrower("B001", "Charlie Brown"));
            library.borrowBook("B001", "101");
        } catch (LibraryException e) {
            System.err.println(e.getMessage());
        }
    }
}