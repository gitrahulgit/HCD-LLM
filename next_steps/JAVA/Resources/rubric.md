  #### **1. Implementation of Core Functionalities (25 Marks)**  
  This section evaluates the correct implementation of the key requirements.

  1.1 **Book Management (10 Marks)**  
  - Correctly implements functionality to add books with all required fields (Book ID, title, author, genre, availability). Validation of inputs and duplicate prevention adds value. *(4 Marks)*  
  - Accurately retrieves and displays only books that are marked as available. *(3 Marks)*  
  - Allows modification of existing book details using a valid Book ID. Proper validation of ID is essential. *(3 Marks)*  

  1.2 **Borrower Management (7 Marks)**  
  - Implements functionality to add borrowers with all required fields (Borrower ID, name, contact). Prevents duplicate IDs. *(4 Marks)*  
  - Displays all books borrowed and returned by a specific borrower. Correctly retrieves data based on Borrower ID. *(3 Marks)*  

  1.3 **Transaction Handling (8 Marks)**  
  - Handles borrowing operations by updating availability and borrower records. Validates constraints such as book availability and borrower’s borrowing limit (maximum 5 books). *(5 Marks)*  
  - Handles return operations by marking books as available and updating borrower records. Validates that the book was borrowed by the specified borrower. *(3 Marks)*  

  ---

  #### **2. Use of OOP Principles (10 Marks)**  
  This section evaluates adherence to object-oriented programming principles.

  2.1 **Classes and Objects (3 Marks)**  
  - Properly models the system using appropriate classes (`Book`, `Borrower`, `Library`). Uses objects to represent entities and manage their state.  

  2.2 **Inheritance (3 Marks)**  
  - Demonstrates inheritance effectively, e.g., using a base class (`Entity`) for common attributes and derived classes for specialization (`Book`, `Borrower`).  

  2.3 **Polymorphism (2 Marks)**  
  - Demonstrates polymorphism through overridden methods or method overloading (e.g., different implementations of `toString()` or behavior changes in inherited classes).  

  2.4 **Encapsulation (2 Marks)**  
  - Uses private fields to restrict direct access. Implements getters and setters to control access to attributes.  

  ---

  #### **3. Exception Handling (5 Marks)**  
  This section evaluates the robustness of the program in handling errors gracefully.

  3.1 **Use of Try-Catch Blocks (2 Marks)**  
  - Implements appropriate `try-catch` blocks to handle runtime exceptions (e.g., invalid input, file errors).  

  3.2 **Custom Exception Class (2 Marks)**  
  - Creates and uses a domain-specific custom exception class (e.g., `LibraryException`) to handle errors like borrowing limit exceeded or book unavailability.  

  3.3 **Edge Case Handling (1 Mark)**  
  - Handles specific edge cases, such as invalid Book or Borrower IDs, non-numeric inputs, and attempts to borrow unavailable books.  

  ---

  #### **4. File I/O Implementation (5 Marks)**  
  This section evaluates the ability to persist and retrieve data using file handling.

  4.1 **Saving Data (2 Marks)**  
  - Correctly saves data (books, borrowers, transactions) to files using `ObjectOutputStream` or other file-handling mechanisms.  

  4.2 **Loading Data (2 Marks)**  
  - Accurately loads data from files into memory when the program starts. Handles cases where files do not exist or are corrupted.  

  4.3 **File Handling Robustness (1 Mark)**  
  - Ensures proper file handling by avoiding overwrites and using exception handling for potential file I/O errors.  

  ---

  #### **5. Code Efficiency and Quality (5 Marks)**  
  This section evaluates the overall efficiency, maintainability, and quality of the code.

  5.1 **Efficient Algorithms (3 Marks)**  
  - Implements efficient and logically sound algorithms for book and borrower management, transaction handling, and data storage/retrieval. Avoids unnecessary computations or iterations.  

  5.2 **Adherence to Java Naming Conventions (2 Marks)**  
  - Uses appropriate class names (PascalCase), variable/method names (camelCase), and constants (UPPER_CASE).  

  ---

  #### **6. Documentation and Code Formatting (5 Marks)**  
  This section evaluates clarity, maintainability, and presentation of the code.

  6.1 **Code Readability and Indentation (5 Marks)**  
  - Ensures consistent indentation, proper spacing, and overall readability of the code.  

  ---

  #### **7. Flexibility for Alternative Approaches**

  7.1 **Valid Alternative Solutions**  
  - Full marks are awarded for any solution that meets the requirements and constraints, even if the approach differs from the model solution. Examples include:  
    - Using `List` instead of `Map` for managing borrowers or books, provided the functionality is correct.  
    - Using text-based file handling (e.g., `BufferedWriter`/`BufferedReader`) instead of `ObjectOutputStream` if data is saved and retrieved correctly.  

  7.2 **Partial Implementations**  
  - Award partial marks for incomplete implementations if students demonstrate a clear understanding of the problem requirements and implement key concepts correctly.  

  7.3 **Uncommon Approaches**  
  - Evaluate uncommon or innovative methods positively if they adhere to the problem constraints, even if they deviate from traditional solutions.  

  ---

  ### **8. Examiners' Notes**
  8.1 Focus on conceptual understanding, correctness, and adherence to requirements.  
  8.2 Avoid penalizing minor deviations in logic or style if the solution fulfills the core functionality and meets the constraints.  
  8.3 Provide constructive feedback to highlight strengths and areas for improvement in the solution.  