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
    private boolean isAvailable;
    public Book(String id, String title) {
        this.id = id;
        this.title = title;
        this.isAvailable = true;
    }
    public String getId() { return id; }
    public String getTitle() { return title; }
    public boolean isAvailable() { return isAvailable; }
    public void setAvailable(boolean available) { isAvailable = available; }
    @Override
    public String toString() {
        return id + ": \"" + title + "\" - " + (isAvailable ? "Available" : "Unavailable");
    }
}
class Borrower {
    private String id;
    private String name;
    private List<String> borrowedBooks;
    public Borrower(String id, String name) {
        this.id = id;
        this.name = name;
        borrowedBooks = new ArrayList<>();
    }
    public void borrowBook(String bookId) {
        borrowedBooks.add(bookId);
    }
    public void returnBook(String bookId) {
        borrowedBooks.remove(bookId);
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
    public void updateBook(String bookId, String newTitle) throws LibraryException {
        Book book = books.get(bookId);
        if (book == null) {
            throw new LibraryException("Book ID does not exist.");
        }
        book.setAvailable(book.isAvailable());
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
        Book book = books.get(bookId);
        if (book == null) throw new LibraryException("Book not found.");
        if (!book.isAvailable()) throw new LibraryException("Book is not available.");
        Borrower borrower = borrowers.get(borrowerId);
        if (borrower == null) throw new LibraryException("Borrower not found.");
        borrower.borrowBook(bookId);
        book.setAvailable(false);
    }
    public void returnBook(String borrowerId, String bookId) throws LibraryException {
        Book book = books.get(bookId);
        if (book == null) throw new LibraryException("Book not found.");
        Borrower borrower = borrowers.get(borrowerId);
        if (borrower == null) throw new LibraryException("Borrower not found.");
        borrower.returnBook(bookId);
        book.setAvailable(true);
    }
    public void saveData() throws IOException {
        try (ObjectOutputStream oosBooks = new ObjectOutputStream(new FileOutputStream("books.dat"));
             ObjectOutputStream oosBorrowers = new ObjectOutputStream(new FileOutputStream("borrowers.dat"))) {
            oosBooks.writeObject(books);
            oosBorrowers.writeObject(borrowers);
        }
    }
    public void loadData() throws IOException, ClassNotFoundException {
        File bookFile = new File("books.dat");
        if (bookFile.exists()) {
            try (ObjectInputStream oisBooks = new ObjectInputStream(new FileInputStream(bookFile))) {
                books = (Map<String, Book>) oisBooks.readObject();
            }
        }
        File borrowerFile = new File("borrowers.dat");
        if (borrowerFile.exists()) {
            try (ObjectInputStream oisBorrowers = new ObjectInputStream(new FileInputStream(borrowerFile))) {
                borrowers = (Map<String, Borrower>) oisBorrowers.readObject();
            }
        }
    }
}
public class LibraryApp {
    public static void main(String[] args) {
        LibrarySystem library = new LibrarySystem();
        try {
            library.loadData();
            library.addBook(new Book("101", "Java Basics"));
            library.addBook(new Book("102", "Advanced Java"));
            library.registerBorrower(new Borrower("B001", "Alice Smith"));
            library.registerBorrower(new Borrower("B002", "Bob Johnson"));
            library.borrowBook("B001", "101");
            library.borrowBook("B002", "102");
            library.returnBook("B001", "101");
            library.saveData();
            for (Book book : library.displayAvailableBooks()) {
                System.out.println(book);
            }
            Borrower borrower = library.viewBorrowerHistory("B001");
            System.out.println("Borrowed Books by " + borrower.getName() + ": " + borrower.getBorrowedBooks());
        } catch (LibraryException | IOException | ClassNotFoundException e) {
            System.err.println(e.getMessage());
        }
    }
}