import java.io.*;
import java.util.*;
interface LibraryOperations {
    void addBook(Book book);
    void registerBorrower(Borrower borrower);
    void borrowBook(String borrowerId, String bookId) throws LibraryException;
    void returnBook(String borrowerId, String bookId) throws LibraryException;
    void displayAvailableBooks();
    void viewBorrowerHistory(String borrowerId) throws LibraryException;
    void saveData() throws IOException;
    void loadData() throws IOException, ClassNotFoundException;
}
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
    private boolean isAvailable;
    public Book(String id, String title, String author, String genre) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.genre = genre;
        this.isAvailable = true;
    }
    public String getId() { return id; }
    public boolean isAvailable() { return isAvailable; }
    public void setAvailable(boolean available) { isAvailable = available; }
    @Override
    public String toString() {
        return id + ": \"" + title + "\" by " + author + " (" + genre + ") - " +
                (isAvailable ? "Available" : "Unavailable");
    }
}
class Borrower {
    private String id;
    private String name;
    private String contactInfo;
    private LinkedList<String> borrowedBooks;
    public Borrower(String id, String name, String contactInfo) {
        this.id = id;
        this.name = name;
        this.contactInfo = contactInfo;
        this.borrowedBooks = new LinkedList<>();
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
    public LinkedList<String> getBorrowedBooks() { return borrowedBooks; }
    @Override
    public String toString() {
        return id + ": " + name + " - Borrowed Books: " + borrowedBooks;
    }
}
class LibraryManager implements LibraryOperations {
    private LinkedList<Book> books;
    private LinkedList<Borrower> borrowers;
    public LibraryManager() {
        books = new LinkedList<>();
        borrowers = new LinkedList<>();
    }
    @Override
    public void addBook(Book book) {
        books.add(book);
    }
    @Override
    public void registerBorrower(Borrower borrower) {
        borrowers.add(borrower);
    }
    @Override
    public void borrowBook(String borrowerId, String bookId) throws LibraryException {
        Borrower borrower = findBorrowerById(borrowerId);
        Book book = findBookById(bookId);
        if (borrower == null) throw new LibraryException("Borrower not found.");
        if (book == null) throw new LibraryException("Book not found.");
        if (!book.isAvailable()) throw new LibraryException("Book is not available.");
        borrower.borrowBook(bookId);
        book.setAvailable(false);
    }
    @Override
    public void returnBook(String borrowerId, String bookId) throws LibraryException {
        Borrower borrower = findBorrowerById(borrowerId);
        Book book = findBookById(bookId);
        if (borrower == null) throw new LibraryException("Borrower not found.");
        if (book == null) throw new LibraryException("Book not found.");
        borrower.returnBook(bookId);
        book.setAvailable(true);
    }
    @Override
    public void displayAvailableBooks() {
        for (Book book : books) {
            if (book.isAvailable()) {
                System.out.println(book);
            }
        }
    }
    @Override
    public void viewBorrowerHistory(String borrowerId) throws LibraryException {
        Borrower borrower = findBorrowerById(borrowerId);
        if (borrower == null) throw new LibraryException("Borrower not found.");
        System.out.println(borrower);
    }
    @Override
    public void saveData() throws IOException {
        BufferedWriter bookWriter = new BufferedWriter(new FileWriter("books.txt"));
        for (Book book : books) {
            bookWriter.write(book.getId() + "," + book.toString());
            bookWriter.newLine();
        }
        BufferedWriter borrowerWriter = new BufferedWriter(new FileWriter("borrowers.txt"));
        for (Borrower borrower : borrowers) {
            borrowerWriter.write(borrower.getId() + "," + borrower.toString());
            borrowerWriter.newLine();
        }
    }
    @Override
    public void loadData() throws IOException, ClassNotFoundException {
        BufferedReader bookReader = new BufferedReader(new FileReader("books.txt"));
        String line;
        while ((line = bookReader.readLine()) != null) {
            String[] parts = line.split(",");
        }
        BufferedReader borrowerReader = new BufferedReader(new FileReader("borrowers.txt"));
        while ((line = borrowerReader.readLine()) != null) {
            String[] parts = line.split(",");
        }
    }
    private Borrower findBorrowerById(String borrowerId) {
        for (Borrower borrower : borrowers) {
            if (borrower.toString().contains(borrowerId)) return borrower;
        }
        return null;
    }
    private Book findBookById(String bookId) {
        for (Book book : books) {
            if (book.toString().contains(bookId)) return book;
        }
        return null;
    }
}
public class LibraryApp {
    public static void main(String[] args) {
        LibraryManager library = new LibraryManager();
        try {
            library.loadData();
            library.addBook(new Book("101", "Effective Java", "Joshua Bloch", "Programming"));
            library.registerBorrower(new Borrower("B001", "Alice Smith", "alice@example.com"));
            library.borrowBook("B001", "101");
            library.returnBook("B001", "101");
            library.saveData();
            library.displayAvailableBooks();
            library.viewBorrowerHistory("B001");
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }
}