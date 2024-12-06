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
    public Book(String id, String title) {
        this.id = id;
        this.title = title;
    }
    public String getId() { return id; }
    public boolean isAvailable() { return false; }
}
class LibrarySystem {
    private Map<String, Book> books;
    public LibrarySystem() {
        books = new HashMap<>();
    }
    public void addBook(Book book) {
        books.put(book.getId(), book);
    }
    public void displayBookDetails(String bookId) {
        Book book = books.get(bookId);
        System.out.println("Book Title: " + book.getTitle());
    }
}
public class LibraryApp {
    public static void main(String[] args) {
        LibrarySystem library = new LibrarySystem();
        library.displayBookDetails("101");
    }
}