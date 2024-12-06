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
        this.name = name;
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
class LibrarySystem {
    private Map<String, Book> books;
    public LibrarySystem() {
        books = new HashMap<>();
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
    public void saveData() throws IOException {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("books.dat"))) {
            oos.writeObject(books);
        }
    }
    public void loadData() throws IOException, ClassNotFoundException {
        File file = new File("books.dat");
        if (file.exists()) {
            try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(file))) {
                books = (Map<String, Book>) ois.readObject();
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
            library.addBook(new Book("102", "Data Structures", "Jane Smith", "Computer Science"));
            library.updateBook("101", "Advanced Java", "John Doe", "Programming");
            library.saveData();
            for (Book book : library.displayAvailableBooks()) {
                System.out.println(book);
            }
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }
}