import java.io.*;
import java.util.*;

// Custom Exception for Library Management
class LibraryException extends Exception {
    public LibraryException(String message) {
        super(message);
    }
}

// Base class for common attributes
abstract class Entity {
    protected String id;
    protected String name;

    public Entity(String id, String name) {
        this.id = id;
        this.name = name;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}

// Book class
class Book extends Entity {
    private String author;
    private String genre;
    private boolean available;

    public Book(String id, String name, String author, String genre, boolean available) {
        super(id, name);
        this.author = author;
        this.genre = genre;
        this.available = available;
    }

    public String getAuthor() {
        return author;
    }

    public String getGenre() {
        return genre;
    }

    public boolean isAvailable() {
        return available;
    }

    public void setAvailable(boolean available) {
        this.available = available;
    }

    @Override
    public String toString() {
        return id + ": \"" + name + "\" by " + author + " (" + genre + ") - " +
                (available ? "Available" : "Unavailable");
    }
}

// Borrower class
class Borrower extends Entity {
    private List<String> borrowedBooks = new ArrayList<>();

    public Borrower(String id, String name) {
        super(id, name);
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

    public List<String> getBorrowedBooks() {
        return borrowedBooks;
    }

    @Override
    public String toString() {
        return id + ": " + name + " - Borrowed books: " + borrowedBooks;
    }
}

// Library Management System
class Library {
    private Map<String, Book> books = new HashMap<>();
    private Map<String, Borrower> borrowers = new HashMap<>();

    // Add a new book
    public void addBook(Book book) {
        books.put(book.getId(), book);
    }

    // Display available books
    public List<Book> getAvailableBooks() {
        List<Book> availableBooks = new ArrayList<>();
        for (Book book : books.values()) {
            if (book.isAvailable()) {
                availableBooks.add(book);
            }
        }
        return availableBooks;
    }

    // Register a new borrower
    public void registerBorrower(Borrower borrower) {
        borrowers.put(borrower.getId(), borrower);
    }

    // Borrow a book
    public void borrowBook(String borrowerId, String bookId) throws LibraryException {
        Borrower borrower = borrowers.get(borrowerId);
        Book book = books.get(bookId);

        if (borrower == null) throw new LibraryException("Borrower not found.");
        if (book == null || !book.isAvailable()) throw new LibraryException("Book unavailable.");

        borrower.borrowBook(bookId);
        book.setAvailable(false);
    }

    // Return a book
    public void returnBook(String borrowerId, String bookId) throws LibraryException {
        Borrower borrower = borrowers.get(borrowerId);
        Book book = books.get(bookId);

        if (borrower == null) throw new LibraryException("Borrower not found.");
        if (book == null) throw new LibraryException("Book not found.");

        borrower.returnBook(bookId);
        book.setAvailable(true);
    }

    // Save data to files
    public void saveData() throws IOException {
        saveToFile("books.txt", books.values());
        saveToFile("borrowers.txt", borrowers.values());
    }

    // Load data from files
    public void loadData() throws IOException, ClassNotFoundException {
        books = loadFromFile("books.txt");
        borrowers = loadFromFile("borrowers.txt");
    }

    // Save helper
    private <T> void saveToFile(String fileName, Collection<T> items) throws IOException {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName))) {
            oos.writeObject(new ArrayList<>(items));
        }
    }

    // Load helper
    @SuppressWarnings("unchecked")
    private <T> Map<String, T> loadFromFile(String fileName) throws IOException, ClassNotFoundException {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName))) {
            List<T> items = (List<T>) ois.readObject();
            Map<String, T> map = new HashMap<>();
            for (T item : items) {
                Entity entity = (Entity) item;
                map.put(entity.getId(), (T) entity);
            }
            return map;
        }
    }
}

// Unit Tests
public class LibraryTest {
    public static void main(String[] args) {
        try {
            Library library = new Library();

            // Add Books
            library.addBook(new Book("101", "Java Programming", "John Doe", "Programming", true));
            library.addBook(new Book("102", "Data Structures", "Jane Smith", "Computer Science", true));

            // Register Borrowers
            library.registerBorrower(new Borrower("B001", "Alice Smith"));
            library.registerBorrower(new Borrower("B002", "Bob Johnson"));

            // Borrow a Book
            library.borrowBook("B001", "101");

            // Return a Book
            library.returnBook("B001", "101");

            // Save and Load Data
            library.saveData();
            library.loadData();

            // Display Available Books
            for (Book book : library.getAvailableBooks()) {
                System.out.println(book);
            }

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
