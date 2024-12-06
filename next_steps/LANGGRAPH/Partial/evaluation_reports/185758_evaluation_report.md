## LangGraph - Student Submission Evaluation

**Overall Marks:** 14/50

**Detailed Report:**

#### 1. Extract Class Method [1/6]
**1.1. Prompt Design [1/3]:**  
The student uses an LLM to attempt class extraction. However, the prompt design is rudimentary and lacks specificity regarding the desired output format.  It doesn't account for potential complexities in real-world Java code.

**1.2. Parsing/Output Extraction [0/2]:**  
The `separate_into_java_classes` function utilizes an LLM but doesn't effectively parse the LLM's response to extract individual classes and their code reliably.  No robust parsing mechanism is evident.

**1.3. State Saving [0/1]:**  
The extracted classes are not properly saved into a structured data format within the LangGraph state.

#### 2. Extract Rubric Method [0/6]
**2.1. Prompt Design [0/3]:**  
This module is entirely missing from the student's submission. No prompt design or implementation is present.

**2.2. Parsing/Output Extraction [0/2]:**  
No attempt to extract rubric details was made.

**2.3. State Saving [0/1]:**  
No state saving related to rubric extraction is present.

#### 3. Initial Evaluation Method [0/6]
**3.1. Prompt Design [0/3]:**  
This module is missing. There's no attempt at designing a prompt to evaluate the extracted classes.

**3.2. Parsing/Output Extraction [0/2]:**  
No extraction of scores and comments is implemented.

**3.3. State Saving [0/1]:**  
No state management related to initial evaluation is implemented.

#### 4. Review Evaluation Method [0/6]
**4.1. Prompt Design [0/3]:**  
This module is missing in the student's solution.

**4.2. Parsing/Output Extraction [0/2]:**  
No code for extracting reviewed evaluations is present.

**4.3. State Saving [0/1]:**  
No state saving for reviewed evaluations was implemented.

#### 5. Marks Extraction Method [0/6]
**5.1. Prompt Design [0/3]:**  
This module is absent from the student's submission.

**5.2. Parsing/Output Extraction [0/2]:**  
No code for extracting marks was implemented.

**5.3. State Saving [0/1]:**  
No state management for extracted marks is present.

#### 6. Total Marks Calculation Method [0/6]
**6.1. Prompt Design [0/3]:**  
This module is missing from the student's implementation.

**6.2. Parsing/Output Extraction [0/2]:**  
The final sum is not extracted.

**6.3. State Saving [0/1]:**  
The final marks are not saved.

#### 7. Graph Construction [13/14]
**7.1. Correct Addition of Nodes to the Graph [5/5]:**  
The student correctly adds nodes to the LangGraph, demonstrating an understanding of the framework's structure.

**7.2. Correct Addition of Edges to the Graph [5/5]:**  
The edges connecting nodes within the LangGraph are correctly defined, showcasing a good grasp of the workflow.

**7.3. Correct Compilation of Graph [3/4]:**  
The graph compiles without errors, although the functionality of many nodes is missing or incomplete, preventing a full evaluation.


---

**Feedback:**  
The student demonstrates a basic understanding of LangGraph's structure by correctly building the graph's nodes and edges. However, the core LLM interaction modules are incomplete or missing, significantly hindering functionality.  Focus on robust prompt engineering, LLM response parsing, and thorough state management to complete the project.  Consider using more sophisticated methods for code parsing and evaluation.


The provided code has several issues preventing it from running correctly and achieving the intended functionality.  The primary problems are:

1. **Missing `re` import:** The `generate_java_classes_from_model_solution` function uses regular expressions but lacks the necessary `import re`.
2. **Missing `StateGraph` definition:** The `create_langgraph_workflow` function uses a `StateGraph` class which is not defined in the provided code.  This is a crucial missing component.
3. **Incorrect LangChain usage within `create_langgraph_workflow`:** The LangChain `ToolNode` is used incorrectly. It expects functions that return a single value, but the functions being used (e.g., `separate_into_java_classes`) return complex structures (lists or dictionaries). The edge connections and data flow between nodes are also flawed.
4. **Error Handling:** The code lacks any robust error handling (e.g., what happens if the OpenAI API call fails, or if a file is not found).
5. **Hardcoded File Paths:** The file paths for student and model solutions are hardcoded.  This should be more flexible.


**Rubric-Based Evaluation (Hypothetical, assuming the missing `StateGraph` and corrected LangChain integration):**

Let's assume the `StateGraph` class and its execution are correctly implemented, and the LangChain integration issues are resolved.  Then a hypothetical evaluation based on the rubric (assuming a successful run) would look like this:


**Module 1 Rubric:**

| Criteria                               | Points Possible | Points Awarded | Comments                                                                        |
|----------------------------------------|-----------------|-----------------|---------------------------------------------------------------------------------|
| **Correctly extracts text from markdown files (10 points)** | 10              | 10              | Assuming the `extract_text_from_markdown` function works as intended.          |
| **Correctly invokes LLM to separate text into Java classes (10 points)** | 10              | 0-10            | Depends on whether the LLM calls in `separate_into_java_classes` are successful and the returned data is correctly processed in the LangGraph.   |
| **Correctly extracts Java class definitions from model solution (10 points)** | 10              | 0-10             | Depends on the correctness and robustness of the regular expression in `generate_java_classes_from_model_solution`.  It currently lacks error handling.|
| **Correctly invokes LLM to extract rubric details (10 points)** | 10              | 0-10             |  Similar to point 2.  Depends on successful LLM calls and handling of responses.  |
| **Correctly evaluates student classes against model solutions (10 points)** | 10              | 0-10             | Similar to point 2 & 4.  Depends on correct LLM usage and response processing.   |
| **Correctly sums marks and saves to file (0 points - not applicable)** | 0               | 0               |  The rubric specifies no marks for this, pending manual compilation check.       |


**Total: 50**

**Important Note:**  The actual points awarded (especially for sections 2, 3, 4, and 5) will depend heavily on whether the code executes successfully. Without a functional `StateGraph` and corrected LangChain integration, this code cannot be evaluated properly according to the rubric.  The hypothetical scoring above assumes these major issues are addressed.  A large portion of the points are conditional on the correctness of the LLM interaction and data handling within the LangGraph framework.  A significant rewrite is needed to fix the code.


The code has several issues preventing it from running correctly and fulfilling the intended functionality.  A comprehensive evaluation based on the provided rubric is impossible without a working implementation. However, I can point out the major flaws and suggest improvements.

**Major Issues:**

1. **Missing Imports:**  The code uses `re` (for regular expressions in `generate_java_classes_from_model_solution`) and `StateGraph` (in `create_langgraph_workflow`) without importing them.  These need to be added.  `StateGraph` appears to be a custom class, not a standard Python library; its definition is missing.  You'll need to either provide its definition or replace it with a suitable alternative (perhaps a custom class representing a workflow).

2. **`_set_env` Function and API Key Handling:** The `_set_env` function attempts to set environment variables for the API key.  While this is a good security practice, it's inconsistently used. The code also prompts for an API key directly using `input()`, which contradicts the environment variable approach. Stick to one method; using environment variables is generally preferred for security.

3. **`separate_into_java_classes` Function:** This function uses `ChatOpenAI` to separate text into Java classes. While this is a valid approach, the response handling is naive. It directly returns `response['content']`, assuming the LLM will always provide correctly formatted Java code. Error handling and more robust parsing of the LLM's response are needed.

4. **`generate_java_classes_from_model_solution` Function:** This function uses regular expressions to extract Java classes. This is a fragile approach because it relies on specific formatting conventions.  It's prone to failure if the input markdown isn't perfectly structured.  The LLM approach in `separate_into_java_classes` might be more robust, though it needs significant improvements as mentioned above.

5. **`extract_rubric_details` Function:**  Similar to `separate_into_java_classes`, this function lacks error handling and assumes the LLM will always provide a structured rubric.

6. **`evaluate_java_classes` Function:** The function assumes the LLM will always return a score and feedback in a consistent format (e.g., "Score: 85").  This is unreliable.  Robust parsing and error handling are necessary.

7. **`extract_and_sum_marks` Function:** This function depends on the highly unreliable assumption about the LLM output format.

8. **`create_langgraph_workflow` Function:**  This function is incomplete due to the missing `StateGraph` class. Even with `StateGraph`, the logic needs review, as the connection between nodes and tool execution isn't clear.


**Recommendations:**

* **Robust Error Handling:** Add `try-except` blocks throughout the code to handle potential errors (e.g., API request failures, invalid LLM responses, file I/O errors).
* **Improved LLM Interaction:** Use more sophisticated prompt engineering and response parsing techniques. Design prompts that explicitly request structured output from the LLM (e.g., JSON format for easier parsing).
* **Refined Regular Expressions (if using):**  If sticking with regex, create more comprehensive patterns to account for variations in Java class definitions.
* **Consistent API Key Handling:** Use environment variables consistently for storing and accessing the API key.
* **Implement `StateGraph` or use a suitable alternative:** Provide a definition for `StateGraph` or find a library to replace it that can create and execute a workflow.
* **Unit Testing:** Write unit tests to verify individual functions' correctness.


Without addressing these fundamental issues, the code cannot be evaluated according to the rubric. The provided rubric is impossible to apply to non-functional code.  Focus on creating a working, robust implementation before attempting to assess its performance based on the rubric.


This code uses LangChain and OpenAI to evaluate Java code.  The rubric focuses on the `extract_classes` module (which isn't explicitly defined but implied by the code's functionality), which extracts Java classes from student and model solutions. Let's analyze it against the provided rubric.

**1. Extract Class Method [6 marks]:**

* **Prompt Design (3 marks):** The prompt design is partially flawed.  The prompt inside `separate_into_java_classes` is simple: `"Separate the following text into Java classes:\n{text}"`. This is acceptable but could be improved.  It doesn't handle edge cases (e.g., poorly formatted code, multiple classes in one file, non-Java code mixed in).  A more robust prompt might include instructions for handling errors or specifying the desired output format (e.g., each class as a separate code block).  The individual prompts within `extract_rubric_details` and `evaluate_java_classes` are also relatively simple and could benefit from more explicit instructions.  Therefore, I would give this section **2 marks**.

* **Parsing/Output Extraction (2 marks):** The `separate_into_java_classes` function relies on the LLM to parse the code.  The accuracy depends entirely on the LLM's capabilities. While the prompt is straightforward, there's no error handling or validation of the LLM's output. The function simply returns the LLM's raw response.  It could be improved by checking if the output contains valid Java classes.  If the LLM fails, a more sophisticated error-handling mechanism would be needed. I'd give this **1 mark** because while it attempts extraction, its robustness is lacking.

* **State Saving (1 mark):** The code saves extracted classes in intermediate variables within the workflow. However, the workflow is implemented using `LangGraph`, which manages state implicitly. While not explicitly using state variables in the conventional sense (like `self.student_classes`), the `LangGraph` handles this internally.  We could consider this 1 mark since the information is passed through the graph, and ultimately this information is used for later steps. Therefore, **1 mark**.

**Total for Extract Class Method: 2 + 1 + 1 = 4 marks**

**Improvements:**

1. **Refined Prompts:** Improve the prompts to the LLM by being more specific and providing examples of good and bad inputs. Also, include instructions for handling edge cases and specify a consistent output format (e.g., JSON for easy parsing).

2. **Robust Parsing:** Add error handling and validation to the parsing functions. Check if the LLM's output contains valid Java classes. If not, implement a fallback mechanism (e.g., using a different LLM or a Java parser library).

3. **Explicit State:**  If you want to adhere strictly to the rubric's requirements for explicit state variables,  you should modify the code to store extracted classes in named variables within the functions or classes, rather than relying entirely on the LangGraph's internal state management.


This improved design would significantly enhance the reliability and robustness of the class extraction module, bringing it closer to a perfect score on the rubric.  The current implementation is functional but brittle and relies heavily on the LLM's perfect behavior.


This code has several issues preventing it from achieving a high score on the rubric.  The biggest problems are in the prompt design and the lack of state saving. Let's address them:

**1. Prompt Design (Poor - 0 marks):**

The prompt for `extract_rubric_details` is extremely simplistic:  `f"Extract rubric details for the following Java class:\n{java_class}"`.  This gives the LLM almost no context.  To earn a higher score, the prompt needs to be much more detailed.  Consider including:

* **Specific Rubric Criteria:** The prompt should explicitly state the assessment criteria. For example, if the rubric assesses correctness, style, efficiency, and documentation, the prompt should mention them.
* **Desired Output Format:** Specify the desired format for the LLM's response.  JSON would be ideal for easy parsing. For example: `{"correctness": 80, "style": 90, "efficiency": 75, "documentation": 95, "comments": "The code is mostly correct, but the efficiency could be improved."}`
* **Example:** An example of the desired output would greatly help the LLM understand the task.

**2. Parsing/Output Extraction (Partial - 1 mark):**

The code extracts the LLM's response but doesn't parse it into a structured format.  It just appends the raw text to the `messages` list.  To get full marks, you need to implement robust parsing, ideally handling potential errors in the LLM's response. JSON parsing would be beneficial here.

**3. State Saving (0 marks):**

There is no mechanism for saving the rubric details extracted by `extract_rubric_details`. The function returns the `messages` list, which is not persisted beyond the function's scope.  You need to save this information (ideally, the structured rubric data after parsing) to a file or database for later use.


**Revised `extract_rubric_details` function:**

```python
import json

def extract_rubric_details(java_classes):
    """Invoke LLM to extract rubric details for each Java class."""
    chat_model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))
    rubric_data = []

    for java_class in java_classes:
        prompt = f"""Extract rubric details for the following Java class.  The rubric assesses correctness, style, efficiency, and documentation (0-100 each).  Return the result as JSON:  {{"correctness": <score>, "style": <score>, "efficiency": <score>, "documentation": <score>, "comments": <string>}}.

Java Class:
```java
{java_class}
```
Example Response: `{{"correctness": 90, "style": 85, "efficiency": 95, "documentation": 70, "comments": "Good code, but documentation could be improved."}}`
"""
        response = chat_model.invoke([{"role": "user", "content": prompt}])
        try:
            rubric_details = json.loads(response['content'])
            rubric_data.append(rubric_details)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON response for class: {java_class}. Error: {e}")
            rubric_data.append({"error": f"JSON parsing error: {e}"})

    # Save rubric_data to a file (e.g., using json.dump)
    with open("rubric_results.json", "w") as f:
        json.dump(rubric_data, f, indent=4)

    return rubric_data
```

**Further Improvements:**

* **Error Handling:** Add more robust error handling throughout the code (e.g., for network issues, LLM API errors).
* **Input Validation:** Validate the input `java_classes` to ensure it's in the expected format.
* **Modularization:** Break down the code into smaller, more manageable functions.


By incorporating these changes, the code's score on the rubric would significantly improve. Remember to adapt the prompt and JSON structure to precisely match your actual rubric criteria.  The improved parsing and explicit state saving through the `rubric_results.json` file are crucial for better grades.  Additionally, consider using a more robust method than simple string matching for extracting Java classes; a proper parser would be much more reliable.


This code attempts to create a LangChain workflow for evaluating student Java code against a model solution using an LLM. However, it has several significant flaws and is incomplete.  The biggest problem is the lack of a `StateGraph` class definition and the missing `re` import for regular expression use.  Also, the prompt design for the LLM is likely insufficient for robust evaluation.

Here's a breakdown of the issues and a suggested improved structure:


**Problems:**

1. **Missing `StateGraph`:** The code references `StateGraph` but doesn't define it.  This class is crucial for the workflow's execution.  You'll need to implement this class, likely including methods for adding nodes, edges, and executing the workflow.

2. **Missing `re` import:** The `generate_java_classes_from_model_solution` function uses regular expressions (`re.findall`) but doesn't import the `re` module.

3. **Insufficient Prompt Engineering:** The prompts given to the LLM are simplistic.  They need to be much more robust and detailed to ensure accurate and consistent evaluation.  Consider including:
    * Specific rubric criteria (e.g., "Adherence to coding style guide," "Correctness of algorithms," "Efficiency of code").
    * Examples of good and bad code snippets illustrating rubric criteria.
    * Clear instructions on how to format the evaluation response (score, detailed feedback for each criterion).

4. **Error Handling:** The code lacks error handling.  Network issues, LLM API errors, and file I/O problems could all cause the code to crash.  Proper `try...except` blocks are needed.

5. **Score Extraction:** The `extract_and_sum_marks` function assumes a very specific format for the LLM's response ("Score: 85"). This is fragile and prone to failure if the LLM's output changes slightly.  A more robust method is needed (e.g., using regular expressions to find a score within a specific range).

6. **Missing Rubric Integration:** The code doesn't directly integrate the rubric.  The rubric should be explicitly provided to the LLM to guide the evaluation process.

7. **`separate_into_java_classes` Function:** This function relies on OpenAI to separate Java classes from a larger text body, which is a complex task for an LLM.  A more reliable approach might involve static analysis tools (if the input is already reasonably structured) or improve the input to the LLM.


**Improved Structure (Conceptual):**

```python
import os
import re
import requests
from flask import Flask, request, jsonify
from langchain.chat_models import ChatOpenAI
# ... other imports (including your StateGraph implementation)

# ... (LLM API key handling remains the same)

def extract_java_classes(text):
    # Use a more robust method than relying solely on the LLM
    # This could involve static analysis tools or improved prompt engineering.
    # ...
    pass

def evaluate_class(student_class, model_class, rubric):
    # Improved prompt engineering to handle rubric and provide consistent output
    prompt = f"""
    Evaluate the student Java class against the model solution and rubric.

    Rubric: {rubric}

    Student Class:
    ```java
    {student_class}
    ```

    Model Class:
    ```java
    {model_class}
    ```

    Provide a score (0-100) and detailed feedback for each rubric criterion.  
    Format the response like this:
    Score: 85
    Criterion 1: [Feedback]
    Criterion 2: [Feedback]
    ...
    """
    # ... (LLM call and response processing)
    pass


class StateGraph:
    # ... (Implementation of StateGraph) ...

def create_langgraph_workflow(student_file, model_file, rubric_file):
    # ... (Improved workflow construction with error handling)
    # The rubric should be loaded from rubric_file.
    pass

# ... (Flask app for API remains the same)
```


Before you can fully implement this improved structure, you need to define the `StateGraph` class and thoroughly address the prompt engineering challenges to ensure the LLM gives consistent, reliable evaluations.  Consider using a structured format for both the rubric and the LLM's output to facilitate easier processing.  Using a structured format would be easier to handle with techniques other than simple string splitting.  Also, you should explore static code analysis tools to assist in the class separation.  Relying entirely on the LLM for this task is highly error-prone.


This code has several issues preventing it from achieving a high score on the provided rubric.  The biggest problem is the absence of a review and correction mechanism using the LLM. The code performs evaluation but doesn't incorporate a step to review and refine those evaluations.  Furthermore, it lacks explicit state saving beyond writing the final score to a file.  Let's address these points and then discuss the rubric scoring.

**Major Improvements Needed:**

1. **LLM-based Review and Correction:**  The core functionality missing is the iterative refinement of the initial evaluations. After `evaluate_java_classes` generates initial scores and feedback, you need to:

   * **Design a prompt:** This prompt should present the LLM with the student code, the model solution, the initial evaluation (score and feedback), and instructions to review the evaluation and potentially adjust the score and feedback based on a deeper analysis or reconsideration.  The prompt should explicitly guide the LLM to justify any score changes.

   * **LLM Interaction:** Send this prompt to the LLM (using `chat_model.invoke`).

   * **Parse the LLM Response:** Extract the revised score and feedback from the LLM's response. This will require careful parsing, likely using regular expressions or other string manipulation techniques to identify the relevant parts of the response.

   * **Update Evaluations:** Replace the original evaluation in the `evaluations` list with the revised evaluation from the LLM.

2. **Explicit State Saving:**  The current `sum_marks` function only saves the final total score.  You need a more robust method of saving the entire evaluation process, including:
   * **Initial evaluations:**  Save the output of `evaluate_java_classes` before the review process.
   * **Revised evaluations:** Save the output after the LLM review.
   * **LLM prompts and responses:**  This is crucial for debugging and understanding the LLM's reasoning. You could save these to separate files or a JSON structure.


3. **Error Handling:** The code lacks error handling.  What happens if the LLM API call fails?  What if the regular expressions in `extract_and_sum_marks` don't find a score?  Add `try-except` blocks to handle potential exceptions.


4. **`langgraph` Integration:** The provided code uses a `create_langgraph_workflow` function but the definition of `StateGraph` and its `execute` method are missing.  This needs to be fully implemented or removed for the code to function.


**Revised Code Structure (Illustrative):**

```python
# ... (Existing code) ...

def review_and_correct_evaluations(evaluations):
    chat_model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))
    revised_evaluations = []
    for evaluation in evaluations:
        prompt = (
            f"Review the following evaluation and correct if necessary:\n\n"
            f"Student Class:\n{evaluation['student_class']}\n\n"
            f"Model Class:\n{evaluation['model_class']}\n\n"
            f"Initial Evaluation:\n{evaluation['evaluation']}\n\n"
            "Provide a revised score (0-100) and feedback. Justify any changes to the score."
        )
        response = chat_model.invoke([{"role": "user", "content": prompt}])
        # ... (Parse the LLM response to extract revised score and feedback) ...
        revised_evaluations.append({
            "student_class": evaluation['student_class'],
            "model_class": evaluation['model_class'],
            "evaluation": revised_evaluation  # The parsed revised evaluation
        })
    return revised_evaluations

# ... (In main execution flow) ...

evaluations = evaluate_java_classes(student_classes, model_classes)
# Save initial evaluations (e.g., to a JSON file)
revised_evaluations = review_and_correct_evaluations(evaluations)
# Save revised evaluations (e.g., to a JSON file)
total_marks = extract_and_sum_marks(revised_evaluations)
# ... (Rest of the code) ...

```


**Rubric Scoring (After Improvements):**

After implementing the significant improvements above:

* **Prompt Design (3 marks):**  A well-structured prompt that clearly instructs the LLM on the review task and requires justification for score changes would earn 3 marks.

* **Parsing/Output Extraction (2 marks):**  Successfully extracting the revised score and feedback from the LLM's response would earn 2 marks. Robust error handling in this section is vital.

* **State Saving (1 mark):** Saving the initial and revised evaluations (and ideally, the LLM prompts and responses) would earn 1 mark.  Simply saving the final score is insufficient.


Without the crucial review and correction mechanism, and with the missing `langgraph` implementation and error handling, the current code would score significantly lower.  The focus should be on implementing the LLM-based review process, handling errors gracefully, and implementing proper state saving.


The provided code lacks a mechanism for extracting comma-separated marks from the LLM's evaluation responses.  The `extract_and_sum_marks` function currently assumes the score is on the first line, in the format "Score: 85".  This is brittle and doesn't meet the rubric's requirement for comma-separated marks extraction.  Furthermore, there's no explicit state saving for individual class marks before the final summation.


Here's a revised version addressing these issues, along with explanations and improvements:


```python
import re
import os
import getpass
from langchain_openai import ChatOpenAI
# ... (rest of your imports)


def extract_rubric_details(java_classes):
    # ... (unchanged)


def evaluate_java_classes(student_classes, model_classes):
    # ... (unchanged)


def extract_and_sum_marks(evaluations):
    """Extracts marks, handles potential errors, and calculates total marks."""
    total_marks = 0
    class_marks = {}  # Dictionary to store marks per class

    for i, evaluation in enumerate(evaluations):
        try:
            # Improved mark extraction:  Assumes marks are comma-separated at the beginning of the line
            match = re.search(r"^Marks:\s*([\d,]+)", evaluation['evaluation'], re.IGNORECASE)
            if match:
                marks_str = match.group(1)
                marks = [int(x.strip()) for x in marks_str.split(',')]
                class_marks[f"Class {i+1}"] = marks  # Save individual class marks
                total_marks += sum(marks)
            else:
                print(f"WARNING: Could not extract marks for Class {i+1}.  Evaluation: {evaluation['evaluation']}")
                class_marks[f"Class {i+1}"] = [] #Handle cases where no marks are extracted
        except (IndexError, ValueError) as e:
            print(f"ERROR extracting marks for Class {i+1}: {e}. Evaluation: {evaluation['evaluation']}")
            class_marks[f"Class {i+1}"] = [] #Handle cases where extraction fails


    print("Marks per class:", class_marks) # Show individual class marks.
    return total_marks, class_marks # Return both total marks and individual marks


def sum_marks(evaluations):
    """LangGraph tool to sum marks and save to a file."""
    total_marks, class_marks = extract_and_sum_marks(evaluations)

    # Save the total marks and individual class marks to a file
    with open('final_evaluation.txt', 'w') as file:
        file.write(f"Total Marks: {total_marks}\n")
        file.write("Marks per class:\n")
        for class_name, marks in class_marks.items():
            file.write(f"{class_name}: {marks}\n")

    return total_marks, class_marks # Return the class marks as well.


# ... (rest of your code, including create_langgraph_workflow)
```

**Key Changes:**

1. **`extract_and_sum_marks` Improvement:** This function now uses a regular expression (`re.search`) to find a line starting with "Marks:" followed by comma-separated numbers.  It handles potential errors (e.g., the LLM not returning marks in the expected format) more gracefully by printing warnings and using error handling. It also saves the individual class marks in the `class_marks` dictionary before computing the total.

2. **Comma-Separated Marks Handling:** The code explicitly splits the string of marks using the comma (`,`) as a delimiter and converts each part into an integer.

3. **State Saving:** The `class_marks` dictionary now saves the marks for each class, fulfilling the state saving requirement.

4. **Error Handling:** The `try...except` block catches potential `IndexError` (if the expected line is missing) and `ValueError` (if a mark is not a valid integer) exceptions.

5. **Output:** The individual class marks are printed to the console and written to the output file `final_evaluation.txt` for better transparency and debugging.

6. **Return Value:** The `sum_marks` function now returns both `total_marks` and `class_marks`.  You'll need to adjust `create_langgraph_workflow` to handle the tuple returned by `sum_marks`.

**To use this revised code:**

1. Make sure your LLM prompt in `extract_rubric_details` and `evaluate_java_classes` is modified to return marks in the format "Marks: 85, 90, 78" (or similar, ensuring comma-separated values).

2. Update the `create_langgraph_workflow` function to handle the tuple returned by the modified `sum_marks` function.  For example,  you might modify the `sum_marks_tool` to handle both total marks and the class mark dictionary.


This revised code provides a more robust and accurate solution for extracting and handling comma-separated marks, addresses the rubric's requirements, and improves error handling.  Remember to adapt the regular expression if the format of the LLM's response changes.


The provided code has several issues preventing it from correctly fulfilling the rubric's requirements for Module 8, specifically regarding the `sum_marks` tool and its integration within a LangGraph workflow.  The major problems are:

1. **Missing `StateGraph` and `ToolNode` Definitions:** The code uses `StateGraph` and `ToolNode` without defining them.  These are presumably from a `langgraph` library not included in the provided code snippet.  Without these definitions, the `create_langgraph_workflow` function is non-functional.

2. **Incorrect `sum_marks` Tool Usage:**  The rubric demands that the prompt *strictly* uses the `sum_marks` tool. The current implementation doesn't utilize LangGraph's state management or the inherent capabilities of `ToolNode` to handle inputs and outputs within the workflow. The `sum_marks` function is called directly within the workflow, bypassing the proper LangGraph execution flow.

3. **Error Handling:** The code lacks error handling.  Many points of failure exist (e.g., API requests, file I/O, parsing scores from the LLM response).  Robust error handling is crucial for a production-ready system.

4. **`separate_into_java_classes` Function Issues:** This function relies on a large language model (LLM) to separate Java classes.  The quality of the separation isn't guaranteed, and this can directly impact the downstream evaluation. A more robust approach might involve parsing techniques or a dedicated Java parser.

5. **`extract_and_sum_marks` fragility:**  The code assumes a specific format for the LLM's output ("Score: 85").  Real-world LLM outputs are unpredictable; this will frequently break.  A more resilient solution is needed to parse the score regardless of format.  Regular expressions or more sophisticated natural language processing techniques are necessary.

6. **No State Saving Verification:** There's no explicit check within the code to verify if the `final_evaluation.txt` file was correctly created and contains the total marks.

Here's a revised structure illustrating how to improve the code, focusing on the `sum_marks` integration and overall workflow:


```python
import os
import re
from langchain_openai import ChatOpenAI
# ... (Other imports and functions remain the same, except for the removed incorrect LangGraph imports)


# Assuming LangGraph library provides these (replace with actual imports if different)
# from langgraph.graph import StateGraph, ToolNode

# Placeholder for LangGraph classes. Replace these with your actual imports
class StateGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, name):
        self.nodes[name] = {}
        return name

    def add_edge(self, source, target):
        if source not in self.edges:
            self.edges[source] = []
        self.edges[source].append(target)

    def execute(self):
        # Simulate execution (Replace with actual LangGraph execution logic)
        return {"total_marks": 100}


class ToolNode:
    def __init__(self, func, inputs):
        self.func = func
        self.inputs = inputs
        self.output = None


def sum_marks(evaluations):
    """LangGraph tool to sum marks and save to a file.  Handles different score formats."""
    total_marks = 0
    for evaluation in evaluations:
        try:
            # More robust score extraction using regex
            match = re.search(r"(\d+)", evaluation['evaluation'])  # Extract any number
            score = int(match.group(1)) if match else 0
            total_marks += score
        except (AttributeError, ValueError) as e:
            print(f"Error extracting score from: {evaluation['evaluation']}, Error: {e}")
            # Handle the error appropriately (e.g., log the error, assign a default score)

    # Save the total marks to a file
    with open('final_evaluation.txt', 'w') as file:
        file.write(f"Total Marks: {total_marks}\n")
    return total_marks


def create_langgraph_workflow(student_file, model_file):
    """Create a LangGraph workflow for evaluating Java classes."""
    graph = StateGraph()

    # ... (Rest of the workflow remains similar, but using the correct ToolNode setup)

    # Step 6: Sum marks and save to file
    sum_marks_node = graph.add_node("Sum Marks")
    graph.add_edge(evaluate_classes_tool, sum_marks_node)

    # Tool node to sum marks - Correct usage within LangGraph
    sum_marks_tool = ToolNode(sum_marks, inputs={"evaluations": evaluate_classes_tool.output})
    graph.add_edge(sum_marks_node, sum_marks_tool)


    # ... (rest of workflow)


    # Execute the workflow and print results
    state = graph.execute()  # Actually execute the LangGraph workflow
    print(f"Final state: {state}") # Assuming 'state' contains the total marks


# Example usage:
student_file = "student_solution.md"
model_file = "model_solution.md"
create_langgraph_workflow(student_file, model_file)

```

Remember to replace the placeholder `StateGraph` and `ToolNode` classes and adjust file paths as needed.  This revised structure significantly improves error handling, score extraction, and the proper integration of the `sum_marks` tool within the LangGraph workflow.  The crucial change is the correct use of `ToolNode` to manage the flow of data within the LangGraph execution.  Also note that the placeholder LangGraph execution needs to be replaced with the actual LangGraph execution logic.


This code has several issues preventing it from creating a proper LangGraph workflow and achieving a high score on the rubric.  The most significant problem is that `StateGraph` and `ToolNode` are not defined, and there's no LangGraph library imported.  The code uses `ChatOpenAI` from `langchain_openai`, but attempts to integrate this with an undefined LangGraph library.

Here's a breakdown of the rubric assessment and suggestions for improvement:

**7. Graph Construction [14 marks]:**

* **Correct addition of nodes to the graph (5 marks):**  The code *attempts* to add nodes, but these are meaningless without a defined `StateGraph` class.  It would receive **0 marks** in its current state.

* **Correct addition of edges to the graph (5 marks):** Similarly, the edge additions rely on a non-existent `StateGraph`.  **0 marks**.

* **Correct compilation of graph (4 marks):**  There's no graph compilation; `evaluation_graph.execute()` is called without a defined `execute()` method.  **0 marks**.

**Total: 0/14**


**To fix this, you need to:**

1. **Install the necessary LangGraph library:**  The code is missing the import and use of a LangGraph library. You'll need to find and install a suitable library (if one exists with the functionality described). If no such library exists, you will need to create a `StateGraph` class and implement the necessary methods (`add_node`, `add_edge`, `execute`).

2. **Implement `StateGraph` and `ToolNode`:** Create classes `StateGraph` and `ToolNode` with the appropriate methods to manage nodes, edges, and execution.  The `ToolNode` should be able to accept a function and its inputs. `StateGraph` needs methods to add nodes, add edges, and to execute the workflow, likely by calling the functions associated with the ToolNodes in the correct order.

3. **Adapt the Workflow:**  The current workflow makes several assumptions about how the LangGraph library works.  The code needs to be re-written to correctly use the `StateGraph` and `ToolNode` objects you define.


**Example of a simplified `StateGraph` and `ToolNode` implementation (requires significant expansion for full functionality):**

```python
class ToolNode:
    def __init__(self, func, inputs):
        self.func = func
        self.inputs = inputs
        self.output = None

    def execute(self):
        self.output = self.func(**self.inputs)
        return self.output

class StateGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.next_node_id = 0

    def add_node(self, name):
        node_id = self.next_node_id
        self.next_node_id += 1
        self.nodes[node_id] = {"name": name, "tool": None}  # Add a "tool" field
        return node_id

    def add_edge(self, source, target):
        if source not in self.edges:
            self.edges[source] = []
        self.edges[source].append(target)

    def execute(self, start_node):
      executed_nodes = set()
      queue = [start_node]

      while queue:
        current_node_id = queue.pop(0)
        if current_node_id in executed_nodes:
          continue
        executed_nodes.add(current_node_id)
        current_node = self.nodes[current_node_id]

        if current_node.get("tool"): #If it's a tool node
          current_node["tool"].execute()

        if current_node_id in self.edges:
          queue.extend(self.edges[current_node_id])
      return executed_nodes

# Example usage (replace with your actual functions)
def my_tool_1():
    return "Result from tool 1"

def my_tool_2(input1):
    return f"Result from tool 2: {input1}"

graph = StateGraph()
start_node = graph.add_node("Start")
tool1_node = graph.add_node("Tool 1")
tool2_node = graph.add_node("Tool 2")
graph.nodes[tool1_node]["tool"] = ToolNode(my_tool_1, {})
graph.nodes[tool2_node]["tool"] = ToolNode(my_tool_2, {"input1": graph.nodes[tool1_node]["tool"].output})
graph.add_edge(start_node, tool1_node)
graph.add_edge(tool1_node, tool2_node)

graph.execute(start_node)
print(graph.nodes[tool2_node]["tool"].output) #This should print "Result from tool 2: Result from tool 1"
```

Remember to replace the placeholder functions (`my_tool_1`, `my_tool_2`) with your actual functions (like `extract_text_from_markdown`, etc.).  This is a barebones example, and you'll need a more robust `StateGraph` implementation to handle complex dependencies and error handling.  After implementing this structure, revisit your node and edge connections to ensure they accurately represent the intended workflow.


This code has several issues:

1. **Missing Imports:**  The code uses `re` (for regular expressions), `StateGraph` (presumably from a LangGraph library), and possibly other modules that aren't imported.  You need to add the necessary `import` statements.  For example: `import re` and `from langgraph.graph import StateGraph`.

2. **`_set_env` Function and API Key Handling:** The `_set_env` function prompts for the OPENAI_API_KEY, but the code also prompts for `llm_api_key` which is never used.  It's redundant and confusing.  Stick to using one method of getting the API key – either environment variables or direct input, but not both.  Using environment variables is generally preferred for security.

3. **Incorrect Regular Expression:** The regular expression `class_pattern` for extracting Java classes is too simplistic. It will fail to handle complex class definitions, nested classes, or classes spanning multiple lines correctly.  A more robust solution would require a more sophisticated regex or, ideally, a proper Java parser.

4. **Error Handling:** There's no error handling.  The code assumes everything will work perfectly.  You need to add `try...except` blocks to handle potential errors like:
    * File not found exceptions (`FileNotFoundError`)
    * API request errors (`requests.exceptions.RequestException`)
    * Invalid API key errors.
    * Errors from the LLM response (e.g., the LLM might not return the expected format).

5. **Over-Reliance on Regex for Java Parsing:** Using regular expressions to parse Java code is fragile and prone to errors. A dedicated Java parser would be significantly more reliable.

6. **Score Extraction:** The `extract_and_sum_marks` function assumes the score is always on the first line and in the format "Score: 85".  This is unreliable.  The LLM's output format might change.  You need a more robust way to extract the score (e.g., using regular expressions or natural language processing techniques to identify the score within the evaluation text).

7. **LangGraph Dependency:** The code uses `StateGraph` and `ToolNode` but doesn't show how these classes are defined or imported. You need to make sure the `langgraph` library is installed (`pip install langgraph`) and the imports are correct.  The integration of LangGraph also needs a more detailed explanation.

8. **Unclear Workflow:** The `create_langgraph_workflow` function creates a LangGraph, but its execution and output are unclear. How are the results from the LangGraph execution used?

Here's a revised version addressing some of these issues (still incomplete because of LangGraph specifics):

```python
import getpass
import os
import re
import requests
from flask import Flask, request, jsonify
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, ToolNode # Add necessary imports

app = Flask(__name__)

# Use environment variables for API key (recommended)
LLM_API_KEY = os.environ.get("OPENAI_API_KEY")
if not LLM_API_KEY:
    LLM_API_KEY = getpass.getpass("Please enter your OPENAI_API_KEY: ")

LLM_API_URL = "https://api.openai.com/v1/chat/completions"

def extract_text_from_markdown(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        return "File not found"

def separate_into_java_classes(text):
    try:
        chat_model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=LLM_API_KEY)
        response = chat_model.invoke([{"role": "user", "content": f"Separate the following text into Java classes:\n{text}"}])
        return response['content']
    except Exception as e:
        return f"Error separating classes: {e}"

# ... (other functions remain largely the same, but need robust score extraction) ...

def extract_and_sum_marks(evaluations):
    total_marks = 0
    for evaluation in evaluations:
        # Improved score extraction using regex (still fragile, needs improvement)
        match = re.search(r"Score:\s*(\d+)", evaluation['evaluation'])
        score = int(match.group(1)) if match else 0  # Handle cases where score isn't found
        total_marks += score
    return total_marks

# ... (create_langgraph_workflow function needs more details on LangGraph usage) ...

def main():
    student_file = 'student_solution.md'
    model_file = 'model_solution.md'

    evaluation_graph = create_langgraph_workflow(student_file, model_file)
    state = evaluation_graph.execute()
    #Process the output of the LangGraph here.

if __name__ == "__main__":
    main()
```

Remember to replace placeholders like  `'student_solution.md'` and `'model_solution.md'` with the actual paths to your files.  The crucial improvement needed is a more reliable Java parser instead of relying on regex, and a more robust method for extracting the score from the LLM's possibly varied responses.  Also, the LangGraph integration needs significant clarification and completion.
