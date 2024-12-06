import java.io.*;
import java.nio.file.*;
import java.util.*;
import com.google.gson.*;
import com.google.gson.reflect.TypeToken;
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
    public String getTitle() { return title; }
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
    private Set<String> borrowedBooks;
    public Borrower(String id, String name, String contactInfo) {
        this.id = id;
        this.name = name;
        this.contactInfo = contactInfo;
        this.borrowedBooks = new HashSet<>();
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
    public String getId() { return id; }
    public Set<String> getBorrowedBooks() { return borrowedBooks; }
}
class LibrarySystem {
    private Set<Book> books;
    private Set<Borrower> borrowers;
    private Gson gson;
    public LibrarySystem() {
        books = new HashSet<>();
        borrowers = new HashSet<>();
        gson = new GsonBuilder().setPrettyPrinting().create();
    }
    public void addBook(Book book) {
        books.add(book);
    }
    public void updateBook(String bookId, String title, String author, String genre) throws LibraryException {
        Book book = findBookById(bookId);
        if (book == null) {
            throw new LibraryException("Book ID does not exist.");
        }
        books.remove(book);
        books.add(new Book(bookId, title, author, genre));
    }
    public Set<Book> displayAvailableBooks() {
        Set<Book> availableBooks = new HashSet<>();
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
            throw new LibraryException("Borrower ID does not exist.");
        }
        return borrower;
    }
    public void borrowBook(String borrowerId, String bookId) throws LibraryException {
        Borrower borrower = findBorrowerById(borrowerId);
        Book book = findBookById(bookId);
        if (borrower == null) throw new LibraryException("Borrower not found.");
        if (book == null) throw new LibraryException("Book not found.");
        if (!book.isAvailable()) throw new LibraryException("Book is not available.");
        borrower.borrowBook(bookId);
        book.setAvailable(false);
    }
    public void returnBook(String borrowerId, String bookId) throws LibraryException {
        Borrower borrower = findBorrowerById(borrowerId);
        Book book = findBookById(bookId);
        if (borrower == null) throw new LibraryException("Borrower not found.");
        if (book == null) throw new LibraryException("Book not found.");
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
        String booksJson = gson.toJson(books);
        Files.write(Paths.get("books.json"), booksJson.getBytes());
        String borrowersJson = gson.toJson(borrowers);
        Files.write(Paths.get("borrowers.json"), borrowersJson.getBytes());
    }
    public void loadData() throws IOException {
        Path booksPath = Paths.get("books.json");
        if (Files.exists(booksPath)) {
            String booksJson = new String(Files.readAllBytes(booksPath));
            Set<Book> loadedBooks = gson.fromJson(booksJson, new TypeToken<Set<Book>>(){}.getType());
            if (loadedBooks != null) books = loadedBooks;
        }
        Path borrowersPath = Paths.get("borrowers.json");
        if (Files.exists(borrowersPath)) {
            String borrowersJson = new String(Files.readAllBytes(borrowersPath));
            Set<Borrower> loadedBorrowers = gson.fromJson(borrowersJson, new TypeToken<Set<Borrower>>(){}.getType());
            if (loadedBorrowers != null) borrowers = loadedBorrowers;
        }
    }
}
public class LibraryApp {
    public static void main(String[] args) {
        LibrarySystem library = new LibrarySystem();
        try {
            library.loadData();
            library.addBook(new Book("101", "Introduction to Java", "John Doe", "Programming"));
            library.addBook(new Book("102", "Data Structures", "Jane Smith", "Computer Science"));
            library.registerBorrower(new Borrower("B001", "Alice Smith", "alice@example.com"));
            library.borrowBook("B001", "101");
            library.returnBook("B001", "101");
            library.saveData();
            for (Book book : library.displayAvailableBooks()) {
                System.out.println("{");
                System.out.println("  \"Book ID\": \"" + book.getId() + "\",");
                System.out.println("  \"Title\": \"" + book.getTitle() + "\",");
                System.out.println("  \"Author\": \"" + book.getAuthor() + "\",");
                System.out.println("  \"Genre\": \"" + book.getGenre() + "\",");
                System.out.println("  \"Status\": \"" + (book.isAvailable() ? "Available" : "Unavailable") + "\"");
                System.out.println("}");
            }
            Borrower borrower = library.viewBorrowerHistory("B001");
            System.out.println("{");
            System.out.println("  \"Borrower ID\": \"" + borrower.getId() + "\",");
            System.out.println("  \"Name\": \"" + borrower.getName() + "\",");
            System.out.println("  \"Borrowed Books\": " + borrower.getBorrowedBooks());
            System.out.println("}");
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }
}