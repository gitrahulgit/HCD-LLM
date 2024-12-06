import java.io.*;
import java.util.*;
class LibraryException extends Exception {
    public LibraryException(String message) {
        super(message);
    }
}
abstract class LibraryItem {
    protected String id;
    protected String name;
    public LibraryItem(String id, String name) {
        this.id = id;
        this.name = name;
    }
    public String getId() { return id; }
    public String getName() { return name; }
}
class Book extends LibraryItem {
    private String author;
    private String genre;
    private boolean isAvailable;
    public Book(String id, String name, String author, String genre) {
        super(id, name);
        this.author = author;
        this.genre = genre;
        this.isAvailable = true;
    }
    public String getAuthor() { return author; }
    public String getGenre() { return genre; }
    public boolean isAvailable() { return isAvailable; }
    public void setAvailable(boolean available) { isAvailable = available; }
    @Override
    public String toString() {
        return id + ": \"" + name + "\" by " + author + " (" + genre + ") - " +
                (isAvailable ? "Available" : "Unavailable");
    }
}
class Borrower extends LibraryItem {
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
    private Map<String, Book> books;
    private Map<String, Borrower> borrowers;
    public LibrarySystem() {
        books = new HashMap<>();
        borrowers = new HashMap<>();
    }
    public void addBook(Book book) {
        books.put(book.getId(), book);
    }
    public void updateBook(String bookId, String title, String author, String genre) throws LibraryException {
        Book book = books.get(bookId);
        if (book == null) {
            throw new LibraryException("Book ID does not exist.");
        }
        book.name = title;
        book.author = author;
        book.genre = genre;
    }
    public List<Book> displayAvailableBooks() {
        List<Book> availableBooks = new ArrayList<>();
        for (Book book : books.values()) {
            if (book.isAvailable()) {
                availableBooks.add(book);
            }
        }
        return availableBooks;
    }
    public void registerBorrower(Borrower borrower) {
        borrowers.put(borrower.getId(), borrower);
    }
    public Borrower viewBorrowerHistory(String borrowerId) throws LibraryException {
        Borrower borrower = borrowers.get(borrowerId);
        if (borrower == null) {
            throw new LibraryException("Borrower ID does not exist.");
        }
        return borrower;
    }
    public void borrowBook(String borrowerId, String bookId) throws LibraryException {
        Borrower borrower = borrowers.get(borrowerId);
        Book book = books.get(bookId);
        if (borrower == null) throw new LibraryException("Borrower not found.");
        if (book == null) throw new LibraryException("Book not found.");
        if (!book.isAvailable()) throw new LibraryException("Book is not available.");
        borrower.borrowBook(bookId);
        book.setAvailable(false);
    }
    public void returnBook(String borrowerId, String bookId) throws LibraryException {
        Borrower borrower = borrowers.get(borrowerId);
        Book book = books.get(bookId);
        if (borrower == null) throw new LibraryException("Borrower not found.");
        if (book == null) throw new LibraryException("Book not found.");
        borrower.returnBook(bookId);
        book.setAvailable(true);
    }
    public void saveData() throws IOException {
        saveBooks();
        saveBorrowers();
    }
    private void saveBooks() throws IOException {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("books.dat"))) {
            oos.writeObject(books);
        }
    }
    private void saveBorrowers() throws IOException {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("borrowers.dat"))) {
            oos.writeObject(borrowers);
        }
    }
    public void loadData() throws IOException, ClassNotFoundException {
        loadBooks();
        loadBorrowers();
    }
    private void loadBooks() throws IOException, ClassNotFoundException {
        File file = new File("books.dat");
        if (file.exists()) {
            try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(file))) {
                books = (Map<String, Book>) ois.readObject();
            }
        }
    }
    private void loadBorrowers() throws IOException, ClassNotFoundException {
        File file = new File("borrowers.dat");
        if (file.exists()) {
            try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(file))) {
                borrowers = (Map<String, Borrower>) ois.readObject();
            }
        }
    }
}
public class LibraryApplication {
    public static void main(String[] args) {
        LibrarySystem library = new LibrarySystem();
        try {
            library.loadData();
            library.addBook(new Book("101", "Introduction to Java", "John Doe", "Programming"));
            library.registerBorrower(new Borrower("B001", "Alice Smith", "alice@example.com"));
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