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
    private String author;
    private String genre;
    private boolean available;
    public Book(String id, String title, String author, String genre) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.genre = genre;
        this.available = true;
    }
    public String getId() { return id; }
    public boolean isAvailable() { return available; }
    public void setAvailable(boolean available) { this.available = available; }
    @Override
    public String toString() {
        return id + ": \"" + title + "\" by " + author + " (" + genre + ") - " +
                (available ? "Available" : "Unavailable");
    }
}
class Borrower {
    private String id;
    private String name;
    private String contactInfo;
    private List<String> borrowedBooks;
    public Borrower(String id, String name, String contactInfo) {
        this.id = id;
        this.name = name;
        this.contactInfo = contactInfo;
        this.borrowedBooks = new ArrayList<>();
    }
    public void borrowBook(String bookId) throws LibraryException {
        if (borrowedBooks.size() >= 5) {
            throw new LibraryException("Cannot borrow more than 5 books.");
        }
        borrowedBooks.add(bookId);
    }
    public void returnBook(String bookId) throws LibraryException {
        if (!borrowedBooks.remove(bookId)) {
            throw new LibraryException("This book was not borrowed by the borrower.");
        }
    }
    public String getId() { return id; }
    public List<String> getBorrowedBooks() { return borrowedBooks; }
}
class LibrarySystem {
    private List<Book> books;
    private List<Borrower> borrowers;
    public LibrarySystem() {
        books = new ArrayList<>();
        borrowers = new ArrayList<>();
    }
    public void addBook(Book book) {
        books.add(book);
    }
    public void updateBook(String bookId, String title, String author, String genre) throws LibraryException {
        Book book = findBookById(bookId);
        if (book == null) {
            throw new LibraryException("Book not found.");
        }
    }
    public List<Book> displayAvailableBooks() {
        List<Book> availableBooks = new ArrayList<>();
        for (Book book : books) {
            if (book.isAvailable()) {
                availableBooks.add(book);
            }
        }
        return availableBooks;
    }
    public void registerBorrower(Borrower borrower) {
        borrowers.add(borrower);
    }
    public Borrower viewBorrowerHistory(String borrowerId) throws LibraryException {
        Borrower borrower = findBorrowerById(borrowerId);
        if (borrower == null) {
            throw new LibraryException("Borrower not found.");
        }
        return borrower;
    }
    public void borrowBook(String borrowerId, String bookId) throws LibraryException {
        Borrower borrower = findBorrowerById(borrowerId);
        Book book = findBookById(bookId);
        if (book == null || !book.isAvailable()) throw new LibraryException("Book is not available.");
        if (borrower == null) throw new LibraryException("Borrower not found.");
        borrower.borrowBook(bookId);
        book.setAvailable(false);
    }
    public void returnBook(String borrowerId, String bookId) throws LibraryException {
        Borrower borrower = findBorrowerById(borrowerId);
        Book book = findBookById(bookId);
        if (book == null) throw new LibraryException("Book not found.");
        if (borrower == null) throw new LibraryException("Borrower not found.");
        borrower.returnBook(bookId);
        book.setAvailable(true);
    }
    private Book findBookById(String bookId) {
        for (Book book : books) {
            if (book.getId().equals(bookId)) return book;
        }
        return null;
    }
    private Borrower findBorrowerById(String borrowerId) {
        for (Borrower borrower : borrowers) {
            if (borrower.getId().equals(borrowerId)) return borrower;
        }
        return null;
    }
    public void saveData() throws IOException {
    }
    public void loadData() throws IOException, ClassNotFoundException {
    }
}
public class LibraryApp {
    public static void main(String[] args) {
        LibrarySystem library = new LibrarySystem();
        try {
            library.loadData();
            library.addBook(new Book("101", "Effective Java", "Joshua Bloch", "Programming"));
            library.registerBorrower(new Borrower("B001", "Bob Johnson", "bob@example.com"));
            library.borrowBook("B001", "101");
            library.returnBook("B001", "101");
            library.saveData();
            for (Book book : library.displayAvailableBooks()) {
                System.out.println(book);
            }
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }
}