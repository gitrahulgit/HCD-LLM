import java.io.*;
import java.util.*;
class LibraryException extends Exception {
    public LibraryException(String message) {
        super(message);
    }
}
abstract class LibraryEntity {
    protected String id;
    protected String name;
    public LibraryEntity(String id, String name) {
        this.id = id;
        this.name = name
    }
    public String getId() { return id; }
    public String getName() { return name; }
}
class Book extends LibraryEntity {
    private String author;
    private String genre;
    private boolean isAvailable;
    public Book(String id, String name, String author, String genre) {
        super(id, name);
        this.author = author
        this.genre = genre;
        this.isAvailable = true;
    }
    public boolean isAvailable() { return isAvailable; }
    public void setAvailable(boolean available) { isAvailable = available; }
    @Override
    public String toString() {
        return id + ": \"" + name + "\" by " + author + " (" + genre + ") - " +
                (isAvailable ? "Available" : "Unavailable");
}
class Borrower extends LibraryEntity {
    private String contactInfo;
    private List<String> borrowedBooks;
    public Borrower(String id, String name, String contactInfo) {
        super(id, name);
        this.contactInfo = contactInfo;
        this.borrowedBooks = new ArrayList<>();
    }
    public void borrowBook(String bookId) throws LibraryException {
        if (borrowedBooks.size() >= 5) {
            throw new LibraryException("Borrowing limit exceeded (5 books max).");
        }
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
    private Map<String, Book> books
    private Map<String, Borrower> borrowers;
    public LibrarySystem() {
        books = new HashMap<>();
        borrowers = new HashMap<>();
    }
    public void addBook(Book book) {
        books.put(book.getId(), book);
    }
}
public class LibraryApplication {
    public static void main(String[] args) {
        LibrarySystem library = new LibrarySystem();
        try {
            library.addBook(new Book("101", "Java Basics", "John Doe", "Programming"));
        } catch (LibraryException e) {
            System.err.println(e.getMessage());
        }
    }
}