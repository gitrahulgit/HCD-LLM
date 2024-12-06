### JAVA Lab Examination  

---

#### **Problem Statement**:  
**Library Management System (LMS)**  

You are tasked with creating a simplified **Library Management System** for a university using Core Java. This system will allow library staff to manage books, borrowers, and transactions efficiently.  

---

#### **Scenario**:  
The university library has the following requirements:  
1. **Book Management**: Library staff should be able to add new books, display a list of available books, and update book information.  
2. **Borrower Management**: Staff can register borrowers and view their borrowing history.  
3. **Transaction Handling**: Borrowers can borrow and return books. The system should ensure a borrower cannot borrow more than 5 books at a time.  
4. **Error Handling**: The system must handle errors such as invalid input, book unavailability, and exceeding the borrowing limit gracefully.  
5. **Data Persistence**: All data (books, borrowers, and transactions) must be saved and retrieved from files.  

---

### **Modules and Sub-Modules**  

#### **Module 1: Book Management**  
**Objective**: Handle operations related to books in the library.  
- **Sub-Module 1.1**: Add a Book  
   - Input: Book details (ID, title, author, genre, availability status).  
   - Output: Confirmation message if the book is added successfully.  
- **Sub-Module 1.2**: Display Available Books  
   - Input: None.  
   - Output: List of books available for borrowing (excluding borrowed books).  
- **Sub-Module 1.3**: Update Book Details  
   - Input: Book ID and updated details.  
   - Output: Confirmation message or error if the book ID does not exist.  

---

#### **Module 2: Borrower Management**  
**Objective**: Manage borrower information and history.  
- **Sub-Module 2.1**: Register Borrower  
   - Input: Borrower details (ID, name, contact information).  
   - Output: Confirmation message.  
- **Sub-Module 2.2**: View Borrower History  
   - Input: Borrower ID.  
   - Output: List of books borrowed and returned by the borrower.  

---

#### **Module 3: Transaction Management**  
**Objective**: Manage book borrowing and return operations.  
- **Sub-Module 3.1**: Borrow Book  
   - Input: Borrower ID and Book ID.  
   - Output: Confirmation or error message (e.g., book unavailable, borrowing limit exceeded).  
- **Sub-Module 3.2**: Return Book  
   - Input: Borrower ID and Book ID.  
   - Output: Confirmation or error message if the book was not borrowed by the borrower.  

---

#### **Module 4: Exception Handling**  
**Objective**: Gracefully handle system errors.  
- Examples of scenarios:  
  - Invalid inputs (e.g., non-numeric IDs, empty fields).  
  - Borrowing a book that is unavailable.  
  - Borrower exceeds the maximum borrowing limit.  

---

#### **Module 5: File I/O**  
**Objective**: Persist data in text files for future use.  
- **Sub-Module 5.1**: Save Data  
   - Save books, borrowers, and transaction information in separate files.  
- **Sub-Module 5.2**: Load Data  
   - Load data from files when the system starts.  

---

### **Input and Output Requirements**  

#### **Input Examples**  
1. Book Details:  
   ```
   Book ID: 101  
   Title: "Introduction to Java"  
   Author: "John Doe"  
   Genre: "Programming"  
   Availability: true  
   ```  

2. Borrower Details:  
   ```
   Borrower ID: B001  
   Name: "Alice Smith"  
   Contact: "alice@example.com"  
   ```  

3. Borrow Transaction:  
   ```
   Borrower ID: B001  
   Book ID: 101  
   ```  

#### **Output Examples**  
1. **Add Book Confirmation**:  
   ```
   Book added successfully!  
   ```  

2. **Borrow Book Error**:  
   ```
   Error: Borrowing limit exceeded (5 books max).  
   ```  

3. **View Borrower History**:  
   ```
   Borrower ID: B001  
   Books Borrowed:  
   - 101: "Introduction to Java" (Borrowed: 2024-11-01, Returned: 2024-11-15)  
   ```  

---

### **Assumptions and Constraints**  
1. Each book has a unique ID.  
2. Each borrower has a unique ID.  
3. Borrowers cannot borrow more than 5 books at a time.  
4. File paths are predefined and accessible (e.g., `books.txt`, `borrowers.txt`, `transactions.txt`).  
5. Use standard Java libraries for implementation.  

---