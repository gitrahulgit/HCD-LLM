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
    public Book(String id, String title, String author, String genre) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.genre = genre;
    }
    public String getId() { return id; }
    public String getTitle() { return title; }
    @Override
    public String toString() {
        return id + ": \"" + title + "\" by " + author + " (" + genre + ")";
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
    public void registerBorrower(Borrower borrower) {
        borrowers.put(borrower.getId(), borrower);
    }
    public void borrowBook(String borrowerId, String bookId) throws LibraryException {
        Borrower borrower = borrowers.get(borrowerId);
        Book book = books.get(bookId);
        if (borrower == null) throw new LibraryException("Borrower not found.");
        if (book == null) throw new LibraryException("Book not found.");
        borrower.borrowBook(bookId);
        books.remove(bookId);
    }
    public void returnBook(String borrowerId, String bookId) throws LibraryException {
        Borrower borrower = borrowers.get(borrowerId);
        if (borrower == null) throw new LibraryException("Borrower not found.");
        borrower.returnBook(bookId);
    }
    public void saveData() throws IOException {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("books.dat"))) {
            oos.writeObject(books);
        }
        try (ObjectOutputStream oosBorrowers = new ObjectOutputStream(new FileOutputStream("borrowers.dat"))) {
            oosBorrowers.writeObject(borrowers);
        }
    }
    public void loadData() throws IOException, ClassNotFoundException {
        File bookFile = new File("books.dat");
        if (bookFile.exists()) {
            try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(bookFile))) {
                books = (Map<String, Book>) ois.readObject();
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
            library.addBook(new Book("101", "Java Programming", "John Doe", "Programming"));
            library.registerBorrower(new Borrower("B001", "Alice Smith"));
            library.borrowBook("B001", "101");
            library.returnBook("B001", "101");
            library.saveData();
            for (Book book : library.books.values()) {
                System.out.println(book);
            }
        } catch (LibraryException | IOException | ClassNotFoundException e) {
            System.err.println(e.getMessage());
        }
    }
}