## LangGraph - Student Submission Evaluation

**Overall Marks:** 14/50

**Detailed Report:**

#### 1. Extract Class Method [2/6]
**1.1. Prompt Design [1/3]:**  
The prompt attempts to extract classes but lacks specificity in handling multiple classes and diverse code structures. It's a basic approach that doesn't account for complexities in real-world Java code.  More specific instructions regarding output format are needed.

**1.2. Parsing/Output Extraction [1/2]:**  
The student's code partially extracts the class name. However, the parsing of the class code itself is incomplete and unreliable.  Error handling and robustness are absent.

**1.3. State Saving [0/1]:**  
The extracted information isn't properly saved into the LangGraph state; it's printed to the console rather than stored for subsequent steps.


#### 2. Extract Rubric Method [0/6]
**2.1. Prompt Design [0/3]:**  
No rubric extraction method is implemented.

**2.2. Parsing/Output Extraction [0/2]:**  
No rubric extraction is attempted, therefore no parsing or extraction.

**2.3. State Saving [0/1]:**  
No state saving related to rubric extraction as no rubric extraction was implemented.


#### 3. Initial Evaluation Method [0/6]
**3.1. Prompt Design [0/3]:**  
No initial evaluation method is implemented.

**3.2. Parsing/Output Extraction [0/2]:**  
No initial evaluation is attempted, thus no parsing or extraction.

**3.3. State Saving [0/1]:**  
No state saving related to initial evaluation is performed as no initial evaluation method was implemented.


#### 4. Review Evaluation Method [0/6]
**4.1. Prompt Design [0/3]:**  
No review evaluation method is implemented.

**4.2. Parsing/Output Extraction [0/2]:**  
No review evaluation is attempted, thus no parsing or extraction.

**4.3. State Saving [0/1]:**  
No state saving related to review evaluation is performed as no review evaluation was implemented.


#### 5. Marks Extraction Method [0/6]
**5.1. Prompt Design [0/3]:**  
No marks extraction method is implemented.

**5.2. Parsing/Output Extraction [0/2]:**  
No marks extraction was attempted, thus no parsing or extraction.

**5.3. State Saving [0/1]:**  
No state saving related to marks extraction is performed as no marks extraction was implemented.


#### 6. Total Marks Calculation Method [0/6]
**6.1. Prompt Design [0/3]:**  
No total marks calculation method is implemented.

**6.2. Parsing/Output Extraction [0/2]:**  
No total marks calculation was attempted, thus no parsing or extraction.

**6.3. State Saving [0/1]:**  
No state saving related to total marks calculation is performed as no total marks calculation was implemented.


#### 7. Graph Construction [12/14]
**7.1. Correct Addition of Nodes to the Graph [5/5]:**  
The student correctly adds the nodes for `extract`, `rubric`, `grader`, `extract_marks`, and `sum_using_tool` to the LangGraph.

**7.2. Correct Addition of Edges to the Graph [5/5]:**  
The student correctly adds the edges connecting the nodes in a sequential workflow.

**7.3. Correct Compilation of Graph [2/4]:**  
The graph compiles without errors, showing basic understanding of LangGraph structure. However, functionality of nodes is incomplete.


---

**Feedback:**  
The student demonstrates a basic understanding of LangGraph by constructing a workflow graph. However, the core functionality of extracting classes, rubric details, and evaluating code remains incomplete.  Focus on robust prompt engineering and accurate parsing of LLM outputs to improve the application's functionality.  Implement missing modules and improve error handling.


## Module 1 Rubric Assessment

Based on the provided notebook and the output, here's an assessment following the rubric's instructions.  Note that I cannot execute the code, so my evaluation is based solely on the printed output.  Compilation errors and runtime exceptions are not considered in this grading, as per the instructions.

**Understanding:** The code implements a Langchain-based workflow involving several stages: extracting classes from Java code, extracting relevant rubric sections, grading the code, extracting numerical scores from feedback, and finally, summing these scores.  The workflow uses OpenAI's ChatOpenAI model for several tasks.

**Evaluation:** The evaluation is entirely dependent on the output of the LLM. The LLM is responsible for:

1. **Code Transformation:**  The LLM successfully extracts the class and code blocks based on the provided format.
2. **Rubric Extraction:** The LLM extracts the relevant rubric portion for the "StringManipulator" class.
3. **Grading:** The LLM produces a grading response with a breakdown of marks for different aspects (compilation, input handling, string manipulation, code style, etc.).   Importantly, the LLM identifies several errors in the student code, as expected.
4. **Mark Extraction:**  The LLM extracts the numerical marks (25, 10, 10) from the generated feedback.
5. **Final Score Calculation:** The LLM sums up the marks and provides a final score (90).  This is likely based on the extracted marks, but the summation process seems not to reflect the obtained marks (25+10+10 = 45). There's a discrepancy here.

**Rubric Points Breakdown (Assuming 50 total marks):**

The rubric is not explicitly defined in the provided JSON, but it is dynamically generated by the LLM in the notebook.  Based on the LLM-generated rubric and the evaluation, let's assume a simplified rubric:

* **Functionality (30 marks):**  The LLM identifies and reports several functional errors in the student code, and properly assesses parts of functionality.
* **Code Style and Quality (10 marks):** The LLM correctly assesses various aspects of the code style and gives points based on those, even though the comments are missing.
* **LLM Usage and Workflow (10 marks):**  The workflow is well-structured, and the LLM is used appropriately for each stage, although one must consider the scoring issue mentioned.


**Detailed Marks Allocation (out of 50):**

* **Functionality (30 marks):**  Given the LLM's feedback, the student code shows some partial functionality.  Let's assign 15/30 based on the detected errors and the identified correct parts.
* **Code Style and Quality (10 marks):** LLM grading shows attention to style, giving 5/10 because of the identified lack of comments.
* **LLM Usage and Workflow (10 marks):** This aspect is generally very well implemented. 9/10 due to the final score discrepancy (90 instead of 45).


**Total Marks: 15 + 5 + 9 = 29 / 50**

**Areas for Improvement:**

* **Error Handling:** The code lacks explicit error handling. While the rubric doesn't deduct marks for this, it's crucial for robust code.
* **Input Validation:** The code should include input validation to prevent unexpected behavior with invalid inputs.
* **Final Score Calculation:** The discrepancy between the sum of extracted marks (45) and the LLM's final score (90) needs to be addressed. This could be due to an issue with the prompt or the LLM's interpretation of the "Final Score" from extracted marks.

**Note:** This assessment relies heavily on the accuracy and consistency of the LLM's responses.  Any inaccuracies in the LLM's grading or score calculation would directly affect the final assessment.  The final score discrepancy needs investigation to ensure the integrity of the LLM-based grading.


The provided notebook attempts to automate code grading using LangChain and OpenAI's large language models.  Let's evaluate its implementation based on a rubric.  Because I don't have access to external files ( `simple-scenario/student_solution.md`, `simple-scenario/rubric.md`, `simple-scenario/model_solution.md` ), I can only assess the code's structure and logic. I cannot provide a score as that depends on the contents of those missing files.

**Rubric-Based Evaluation:**

To properly evaluate this, we need a rubric for the Python code itself.  Since one isn't provided, I'll create a sample rubric focusing on clarity, functionality, and error handling.

**Rubric (Example):**

| Criterion | Excellent (4 points) | Good (3 points) | Fair (2 points) | Poor (1 point) |
|---|---|---|---|---|
| **Code Clarity and Readability:** | Code is well-commented, uses descriptive variable names, and is easy to understand. | Most code is well-commented and readable, but minor improvements could be made. | Some comments are present, but variable names or code structure could be improved for better readability. | Code is poorly commented and difficult to understand.  |
| **Functionality (Extract, Rubric, Grade, Marks, Sum):** | All functions work correctly and as intended.  Handles various inputs gracefully. | Most functions work correctly, but one or two minor issues exist. | Some functions work, but significant flaws are present in functionality. | Functions fail to perform their intended task. |
| **Error Handling:** | Robust error handling is present throughout.  Catches exceptions appropriately. | Most exceptions are handled, but some edge cases may be missed. | Basic error handling is present, but significant improvements are needed. | Little to no error handling is implemented. |
| **LLM Interaction:** | Effective prompting strategies are used to elicit accurate and useful responses from the LLM. | Prompting is generally effective but could be refined for better results. | Prompting strategies are somewhat unclear or ineffective. | Prompts are poorly designed and lead to inaccurate or unhelpful LLM responses. |
| **Regular Expression Usage:** | Regular expressions are used correctly and efficiently for string manipulation. | Regular expressions mostly work, but could be more concise or accurate. | Regular expressions are used but contain errors or inefficiencies. | Regular expressions are used incorrectly or not at all. |


**Evaluation of the Python Code:**

* **Code Clarity and Readability:** The code is reasonably well-structured, but could benefit from more detailed comments explaining the logic within the functions (especially the LLM interaction parts). The use of `pprint` for output makes debugging easier.

* **Functionality:** The individual functions (`extract`, `extrcat_rubric`, `grade`, `extract_marks`, `sum_using_tool`) appear to be logically designed, attempting to handle the different stages of the grading process. However, their actual functionality depends on the external files and the LLM's responses, which I cannot verify.

* **Error Handling:**  The code has minimal explicit error handling. It relies heavily on the LLM's ability to produce well-formed outputs.  More robust error checks (e.g., `try...except` blocks) would make it more resilient to unexpected LLM responses or file-reading failures.  The regular expression usage is also a potential point of failure if the LLM's output isn't perfectly formatted.

* **LLM Interaction:** The prompting strategies seem thoughtfully designed, attempting to guide the LLM toward specific outputs. However, their effectiveness in practice depends on the LLM's capabilities and the quality of the external files used.

* **Regular Expression Usage:** The regular expressions (`class_pattern`, marks extraction, score extraction) appear to be correctly constructed based on the expected output format. However, their robustness in the face of variations in LLM output needs to be carefully tested.


**Overall:**

The code shows a promising approach to automated code grading.  The modular structure is good, and the functions are well-organized.  However,  it needs more robust error handling, more comments for better clarity, and thorough testing to ensure reliability. The score cannot be determined without the content of the external files.  The functionality and effectiveness depend entirely on those files and the OpenAI model's accuracy.  The current state is more of a proof-of-concept than a fully functional system.


The provided code implements a Langchain workflow for grading Java code. Let's analyze its `extract` function concerning the rubric's "Extract Class Method" section.

**1. Prompt Design (3 marks):**

The prompt within the `extract` function is reasonably well-designed. It clearly instructs the LLM to:

* Extract class definitions from the provided Java code.
* Provide the class name and code for each class.
* Separate classes using "________end________".
* List all extracted class names at the end.
* Specifies an output format.


However, it could be improved:

* **Specificity:** While it mentions Java, it doesn't explicitly handle potential edge cases (e.g., nested classes, inner classes, comments within class definitions). A more robust prompt might anticipate these and instruct the LLM on how to handle them.  The prompt could also benefit from examples of the desired output.
* **Error Handling:** The prompt doesn't address what to do if no classes are found or if the input code is invalid Java. A more comprehensive prompt would include guidance for these situations.


Therefore, I'd give it **2 marks** because it's reasonable but lacks the completeness and robustness for a perfect score.


**2. Parsing/Output Extraction (2 marks):**

The `extract_classes` function uses regular expressions to extract the class names and code blocks.  This approach is relatively simple and works reasonably well *given the specific output format enforced by the prompt*.  However, it's fragile:  If the LLM's output deviates slightly from the expected format (e.g., extra whitespace, different delimiter), the parsing will likely fail.  The regex only works reliably if the LLM precisely adheres to the structure specified in the prompt.

Therefore, I'd award **1 mark**.  It achieves partial parsing but isn't robust enough. A more robust approach would use a parser that understands Java syntax rather than relying on a simple regex.


**3. State Saving (1 mark):**

The `extract` function correctly saves the extracted class information (`class_list` and `code_blocks`) to the `state` dictionary.  This is done properly.

Therefore, I'd give it **1 mark**.


**Overall Score for Extract Class Method:**

2 (Prompt Design) + 1 (Parsing/Output Extraction) + 1 (State Saving) = **4 marks out of 6**


The provided code implements a grading system using LangChain and OpenAI's LLMs. Let's analyze the `extract_rubric` function and evaluate it against the rubric provided.

**1. Prompt Design (3 marks):**

The prompt in `extrcat_rubric` (note the typo) is:

```
        You are provided with the following rubric:\n
        {rubric}\n
        \n
        Extract the relevant parts of the rubric that apply to the following class: {class_name}.\n
        The relevant rubric for the class should be extracted and summarized accordingly.\n
```

This prompt is reasonably good. It provides the full rubric and clearly instructs the LLM to extract the relevant sections for a specific class.  However, it lacks explicit instructions on the *format* of the extracted rubric.  The LLM might return it in a paragraph format, making further parsing difficult.  A more structured output format would improve the robustness.

Therefore, I would rate the prompt design as **2 marks**.  It's mostly complete, but lacks a critical detail for ease of parsing.


**2. Parsing/Output Extraction (2 marks):**

The code simply assigns the LLM's raw response to `extracted_rubric[class_name]`. No parsing is performed. This is highly dependent on the LLM consistently returning a structured and easily extractable format. If the LLM's response is not as expected, the extraction will fail.

I would rate this as **1 mark** (partial extraction), because it relies on implicit structure from the LLM and doesn't handle potential variations in the output.


**3. State Saving (1 mark):**

The `extracted_rubric` dictionary is correctly added to the `state` dictionary.  This ensures the rubric details are saved for later use in the grading process.

Therefore, I would rate this as **1 mark**.


**Overall Score for Extract Rubric Method:**

2 + 1 + 1 = **4 marks out of 6**


**Recommendations for Improvement:**

* **Structured Prompt:** Modify the prompt to explicitly request a structured output format (e.g., JSON, key-value pairs, or a specific markdown format).  This will make parsing much easier and less error-prone. Example:

```
        You are provided with the following rubric:\n
        {rubric}\n
        \n
        Extract the relevant parts of the rubric that apply to the class "{class_name}".  Return your answer as a JSON object with the following keys: "criteria", "points", "description". For example:
        ```json
        {
          "criteria": "Correctness",
          "points": 20,
          "description": "Program executes without errors and produces the correct output."
        }
        ```

        Provide one JSON object for each relevant rubric item.
```

* **Robust Parsing:** Implement proper parsing of the LLM's response. Instead of directly assigning the raw text, use a parser to extract the relevant information based on the expected structure defined in the prompt.  Libraries like `json` (if using JSON) or regular expressions can be useful for this.

* **Error Handling:** Add error handling to gracefully manage cases where the LLM's response is unexpected or the parsing fails.  This could include logging errors, returning default values, or raising exceptions depending on the desired behavior.


By addressing these points, the `extract_rubric` function can be made more robust and reliable, significantly improving its score.


This code implements a Langchain-based workflow for grading student code. Let's break down its functionality and then address the rubric evaluation.

**Code Functionality:**

The code defines a workflow using `langchain` and `langgraph` to automatically grade student Java code.  It goes through the following stages:

1. **`extract`:** Extracts class definitions from student code using a prompt sent to an LLM.  The extracted classes and code blocks are stored in the `AgentState`.  This part has a flaw; it uses `sc.next()` which only reads a single word instead of the whole line of user input.

2. **`extrcat_rubric`:** Extracts relevant rubric sections for each class identified in the previous step using another LLM prompt.

3. **`grade`:** Grades each code block against a model solution and the extracted rubric using an LLM.  The grading responses (feedback and scores) are stored in the `AgentState`.

4. **`extract_marks`:** Parses the LLM's grading feedback to extract numerical scores for each rubric section. This also appears to rely on a specific format within the LLM's output.

5. **`sum_using_tool`:** Finally, sums up the extracted scores to produce a final score, again using an LLM.


**Rubric Evaluation (Module 5):**

Let's evaluate the code based on the provided rubric:

**3. Initial Evaluation Method [6 marks]:**

* **Prompt Design (3 marks):** The prompts used within the functions (`extract`, `extrcat_rubric`, `grade`, `extract_marks`, `sum_using_tool`) are reasonably well-structured but have potential weaknesses:
    * The prompts heavily rely on the LLM's ability to understand specific output formats (e.g., "List of classes[...]", "Marks:[...]").  This makes the system fragile; slight changes in the LLM's response could break the parsing.
    * The prompts lack explicit instructions on handling edge cases (e.g., no classes found, rubric section not found, malformed feedback).  Robust prompts should anticipate and handle such scenarios.
    * The prompt in `extract` uses `sc.next()` which will fail for multi-word inputs, and the prompt would likely need to handle this appropriately.

    **Score:** 2/3.  Mostly structured, but lacks robustness and error handling in the prompt design.


* **Parsing/Output Extraction (2 marks):** The parsing relies heavily on regular expressions (`re.search`). While functional for the example, this is prone to failure if the LLM's output format varies even slightly.  Robust parsing should employ more sophisticated techniques or error handling to deal with unexpected output.

    **Score:** 1/2. Incomplete extraction due to fragility of regex-based parsing.


* **State Saving (1 mark):** The `AgentState` dictionary effectively stores intermediate results between nodes.

    **Score:** 1/1. Correct state management.


**Overall Score for Initial Evaluation Method:** 2 + 1 + 1 = 4/6

**Recommendations for Improvement:**

* **Robust Prompt Engineering:** Design prompts that are more resilient to variations in LLM output.  Include explicit instructions for handling edge cases and specify output formats more precisely.  Consider using structured output formats (like JSON) for easier parsing.

* **Improved Parsing:** Replace reliance on simple regular expressions with more robust parsing techniques that handle variations and potential errors in the LLM responses.  Consider using JSON output from the LLM or creating custom parsers.

* **Error Handling:** Implement error handling mechanisms throughout the workflow to gracefully handle unexpected situations (e.g., LLM errors, parsing errors).

* **Unit Testing:** Add comprehensive unit tests to verify the correctness of each function and the overall workflow.  This would make future maintenance and debugging much easier.

* **Refactor `extract`:** Correct the flawed use of `sc.next()` with `sc.nextLine()` for proper input capture.


By addressing these points, the code's robustness and reliability would significantly improve, leading to a higher score on the rubric.


The provided code implements a grading system using LangChain and OpenAI's LLM. Let's analyze it based on the rubric for Module 6, specifically focusing on the Review Evaluation Method.


**4. Review Evaluation Method:**

* **Prompt Design (3 marks):**

The prompts within the `extract_rubric`, `grade`, `extract_marks`, and `sum_using_tool` functions are reasonably well-structured. They clearly define the task for the LLM (extract rubric sections, grade code, extract marks, sum marks), provide necessary context (rubric, code, feedback), and specify the desired output format.  However, they could be improved with a few additions for more robust results:

   * **Error Handling:** The prompts don't explicitly instruct the LLM on how to handle cases where marks are missing or the format is unexpected. Adding instructions to return "0" or a specific error message for such cases would be beneficial.
   * **Specificity:** In the grading prompt, adding examples of good and bad code snippets related to specific rubric criteria would guide the LLM to a more accurate evaluation.
   * **Few-Shot Learning:** Providing a few examples of code snippets with their corresponding grades and feedback in the `grade` function's prompt could significantly improve the LLM's performance.

Therefore, I would give this section a **2 out of 3 marks**.


* **Parsing/Output Extraction (2 marks):**

The code uses regular expressions (`re.search`) to extract the relevant information (classes, marks, final score) from the LLM's responses. This approach is functional but fragile.  If the LLM's output format changes slightly, the regular expressions might fail.  

A more robust approach would involve using a structured output format from the LLM (e.g., JSON) and then parsing that structured data. This would make the code less prone to errors due to variations in the LLM's response.

Therefore, I would give this section a **1 out of 2 marks**.


* **State Saving (1 mark):**

The code uses a `TypedDict` (`AgentState`) effectively to maintain and update the program's state throughout the different stages (extraction, rubric application, grading, mark extraction, summation).  The state is correctly passed between functions and updated accordingly.

Therefore, I would give this section a **1 out of 1 mark**.



**Overall Score for Review Evaluation Method:**  2 + 1 + 1 = **4 out of 6 marks**


**Recommendations for Improvement:**

1. **Structured Output from LLM:**  Modify the prompts to encourage the LLM to return JSON or a similarly structured output to facilitate more reliable parsing.

2. **Robust Error Handling:** Include explicit instructions in the prompts for handling unexpected or missing data.

3. **Few-Shot Learning:** Incorporate few-shot learning examples into the prompts, especially the grading prompt.

4. **Input Validation:** Add validation to check the extracted data (marks, classes) for correctness before further processing.

5. **More descriptive variable names:** Some variable names could be more descriptive to increase readability (e.g., instead of `msg`, use `grading_prompt`).


By addressing these points, the code's reliability and robustness will be significantly enhanced.  The rubric's scoring is a guideline, and the actual scores might vary slightly depending on the specific implementation of these suggestions.


The code you provided is a complex Langchain-based workflow for grading code.  Let's analyze the `Marks Extraction Method` according to the rubric.

**1. Prompt Design (3 marks):**

The prompt design is good but could be improved.  The prompt in `extract_marks` is relatively clear: it instructs the LLM to extract marks in a specific format. However, it relies heavily on the LLM's ability to correctly identify and parse the grading feedback, which isn't guaranteed.  The feedback from the grader may not always consistently use the exact format "Marks:[<number>]". A more robust prompt would handle variations in formatting (e.g., using regular expressions within the prompt itself to guide extraction). Therefore, I'd give it a **2/3**.  A perfect 3 would require a more flexible and error-resistant prompt.

**2. Parsing/Output Extraction (2 marks):**

The `extract_marks` function uses regular expressions (`re.search`) to extract the marks. This is a good approach, but it's fragile.  If the format of the LLM's output changes slightly, the regular expression will fail.  The code *does* extract the marks from the *provided* output, but it lacks robustness for unexpected variations. Therefore, it gets **1/2**.  A perfect 2 requires more robust error handling and flexibility in parsing the LLM's response.

**3. State Saving (1 mark):**

The `extract_marks` function correctly updates the `state` dictionary with the extracted marks. This aspect is well-implemented.  Therefore, it receives **1/1**.


**Overall Marks Extraction Method Score: 4/6**

**Recommendations for Improvement:**

* **More Robust Prompting:**  Instead of a simple string template for the prompt, use a more sophisticated approach, potentially incorporating regular expressions directly into the prompt to make it more resilient to variations in the grader's output.  Example (Illustrative,  adapt to your specific needs):

```python
prompt = """
You are given feedback strings.  Extract all numerical scores representing marks.
The marks might be formatted in various ways, e.g., "Total: 25/70", "5/5", "25/100".
For each feedback string, extract *all* numbers that represent a score.  Return as a list of integers.

Feedback Strings:
{feedback_list}
"""

# ... later in the code ...
import re
matches = re.findall(r'\d+', response.content) #Find all digits
marks = [int(match) for match in matches]
```


* **Improved Parsing:**  Consider alternative parsing strategies besides regular expressions.  If the grader's output is structured (e.g., JSON or a more predictable format), consider JSON parsing or other structured data processing methods.  This will make the extraction much more reliable.

* **Error Handling:**  Add explicit error handling to gracefully deal with cases where the LLM's response is unexpected or the regular expression doesn't find any matches.  For example, include a `try-except` block to catch `IndexError` or `AttributeError` exceptions that might arise from unexpected LLM outputs.


By addressing these improvements, the robustness and reliability of the marks extraction process would significantly increase.


The provided code implements a LangChain workflow for grading code. Let's analyze its `sum_using_tool` function and assess it against the rubric.

**Rubric Criteria Assessment:**

* **Prompt Design (3 marks):**

The prompt in `sum_using_tool` is designed to extract numerical values from a list of strings, sum them, and provide the total.  It's relatively clear and instructs the LLM to provide output in a specific format. However, it relies on the input being perfectly formatted as "Marks:[<number>]".  Any deviation from this could lead to incorrect results.  This makes it *mostly* proper.

**Score: 2 marks**


* **Parsing/Output Extraction (2 marks):**

The code uses a regular expression (`re.search(r'Final Score:\s*\[(\d+)]', response.content)`) to extract the final score. This is a correct and robust approach for extracting the numerical score from the LLM's response, assuming the LLM adheres to the specified output format.

**Score: 2 marks**


* **State Saving (1 mark):**

The final score is correctly saved in the `state["final_score"]` dictionary.

**Score: 1 mark**


**Overall Score for Module 8 (Total Marks Calculation Method):**

2 + 2 + 1 = **5 marks out of 6**

**Improvements:**

1. **Prompt Robustness:** The prompt for `sum_using_tool` should be made more robust. It could include error handling for cases where the LLM doesn't return the expected format or contains multiple "Final Score" lines.  Consider adding explicit instructions to handle potential errors gracefully (e.g., return 0 if no score is found) or to only extract the first "Final Score" if multiple exist.


2. **Input Validation:**  Before using the `marks` list, the code should validate the input to ensure each element is in the expected format. This would catch errors earlier and improve reliability.  


3. **Logging:**  Adding logging statements would greatly improve debugging.  Log the `marks` list, the prompt sent to the LLM, and the LLM's response to help track down any issues.


4. **Error Handling:** The code assumes the regular expression will always find a match.  Wrap the `score_match.group(1)` line in a `try-except` block to handle cases where no match is found and prevent a program crash.



**Revised `sum_using_tool` function incorporating improvements:**


```python
import logging

def sum_using_tool(state: AgentState) -> AgentState:
    logging.info("Entering sum_using_tool function")
    marks = state.get("marks", [])
    logging.info(f"Marks received: {marks}")
    model = ChatOpenAI(temperature=0.3, model="gpt-4o-mini", streaming=True)

    prompt = """
    You are given a list of marks in string format.  Each mark should be a number.  If any input is not a number, ignore it.
    Sum the numbers and provide the final score.
    Marks List:
    {marks_list}
    Output Format:
    Final Score: <total_marks>
    """
    try:
        response = model.invoke([HumanMessage(content=prompt.format(marks_list=", ".join(marks)))])
        logging.info(f"LLM response: {response.content}")
        score_match = re.search(r"Final Score:\s*(\d+)", response.content)  #simplified regex
        final_score = int(score_match.group(1)) if score_match else 0
    except Exception as e:
        logging.exception(f"Error during score calculation: {e}")
        final_score = 0

    state["final_score"] = str(final_score)
    logging.info(f"Final Score: {final_score}")
    return state

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
```

This revised function adds logging, improves error handling and simplifies the regex to be more robust.  The prompt also explicitly instructs the LLM on how to handle non-numeric values. Remember to adjust the logging level as needed during development and testing.


The provided code implements a LangGraph workflow for grading Java code. Let's evaluate it against the rubric:

**7. Graph Construction [14 marks]**

* **Correct addition of nodes to the graph (5 marks):**  The code correctly adds five nodes: "extract," "rubric," "grader," "extract_marks," and "sum_using_tool."  These correspond to the distinct stages of the grading process.  **5/5**

* **Correct addition of edges to the graph (5 marks):** The code establishes the correct sequence of operations using edges.  The flow `START -> extract -> rubric -> grader -> extract_marks -> sum_using_tool -> END` is accurately represented. **5/5**

* **Correct compilation of graph (4 marks):** The line `graph = workflow.compile()` attempts to compile the graph.  The success of this compilation depends on the `langgraph` library's implementation. Assuming `langgraph` functions correctly, the compilation is successful.  However, without knowing the internal workings of the `compile()` method and error handling, we can't definitively confirm its correctness.  We'll assume it works as intended for now.  **4/4**

**Total for Graph Construction: 14/14**


**Overall Assessment:**

The code's graph construction aspect perfectly meets the rubric's criteria. The nodes and edges clearly define a functional workflow. The assumption of successful compilation is based on the provided code's structure and typical LangGraph functionality.  To make this assessment completely rigorous, more information about `langgraph`'s `compile()` method, particularly regarding its error-handling and internal logic, would be needed.  A test to verify the successful execution of the compiled graph would also improve certainty.


This Jupyter Notebook defines a workflow for automatically grading Java code using Langchain and OpenAI's language models.  Let's break down the code and address potential improvements.

**Code Breakdown:**

1. **Import Statements:** Imports necessary libraries including `langchain`, `openai`, `pydantic`, and regular expression tools.

2. **Environment Setup:** The `_set_env` function retrieves the OpenAI API key from the user and sets it as an environment variable.  This is crucial for interacting with the OpenAI API.

3. **`AgentState` Class:** Defines a `TypedDict` to structure the state of the grading agent.  It tracks messages, classes identified, code blocks, extracted rubric sections, graded responses, extracted marks, and the final score.

4. **`extract_classes` Function:**  This function uses regular expressions to extract class names and code blocks from the LLM's initial response. The delimiter `________end________` separates the code blocks.  It handles cases where no classes are found.

5. **`extract` Function:** This function forms the initial prompt for the LLM.  It reads a student's Java code from `simple-scenario/student_solution.md` and constructs a prompt that instructs the LLM to extract class definitions and format the output as specified.  The extracted classes and code blocks are added to the `AgentState`.

6. **`extrcat_rubric` Function:** Reads the rubric from `simple-scenario/rubric.md` and uses the LLM to extract rubric sections relevant to each identified class.

7. **`grade` Function:** This is a core function. It takes the extracted code blocks and rubric sections, reads a model solution from `simple-scenario/model_solution.md`, and constructs prompts for the LLM to grade each code block based on the rubric and model solution.  The graded responses are stored in the `AgentState`.

8. **`extract_marks` Function:** Parses the LLM's graded responses to extract the numerical marks awarded for each section.  It uses regular expressions to find marks in a specific format.

9. **`sum_using_tool` Function:** Uses the LLM to sum the extracted marks and determine the final score.

10. **Workflow Definition:** Creates a `StateGraph` using `langgraph` to define the workflow: `extract` -> `rubric` -> `grade` -> `extract_marks` -> `sum_using_tool`.

11. **Workflow Execution:**  The code initializes an `AgentState`, then streams the execution of the workflow, printing the output from each node.

**Potential Improvements:**

* **Error Handling:** The code lacks robust error handling.  For instance, what happens if the regular expressions don't find what they're looking for?  Adding `try-except` blocks to handle potential exceptions (e.g., `FileNotFoundError`, `IndexError`, `AttributeError`) would make it more resilient.

* **Input Validation:**  Sanitize user input before sending it to the LLM to prevent injection attacks or unexpected behavior.

* **More Sophisticated Marking:** The current marking scheme relies heavily on the LLM's ability to parse and extract numerical scores from free-form text. A more robust approach would involve a structured rubric where each criterion has a specific point value, and the LLM's task is to assess whether each criterion is met, rather than to extract numbers from a narrative.

* **LLM Model Selection:** The code uses `gpt-4o-mini`. Consider using a more powerful model (like `gpt-4`) for better accuracy and robustness, though this increases cost.

* **Code Formatting:** While indentation is generally good, consider using a consistent style guide (like PEP 8 for Python) to improve readability.

* **Modularization:**  Break down the code into smaller, more manageable modules for better organization and reusability.  For example, separate functions for reading files, parsing LLM responses, and handling rubric data would improve clarity.

* **Testing:** Implement unit tests to verify the correctness of individual functions and the overall workflow.

* **Logging:** Add logging to track the execution flow and any errors encountered.


**Example of Improved Error Handling (in `extract_marks`):**

```python
def extract_marks(state: AgentState) -> AgentState:
    print("---EXTRACT MARKS FROM FEEDBACK---")
    graded_responses = state.get("graded_responses", [])
    model = ChatOpenAI(temperature=0.3, model="gpt-4o-mini", streaming=True)
    marks = []

    prompt = """
    You are given a list of feedback strings. For each feedback, extract the marks awarded. 
    The marks will be provided in the format: Marks:[<number>].
    Extract the marks and provide them in a list format.
    Feedback List:
    {feedback_list}
    Output Format:
    Marks: [<mark1>, <mark2>, ...]
    """

    feedback_list = [response["feedback"] for response in graded_responses]
    try:
        response = model.invoke([HumanMessage(content=prompt.format(feedback_list=feedback_list))])
        marks_match = re.search(r'Marks:\s*\[(.*?)\]', response.content)
        if marks_match:
            marks_str = marks_match.group(1)
            marks = [mark.strip() for mark in marks_str.split(',')]
        else:
            print("Warning: Could not extract marks from LLM response.")
    except Exception as e:
        print(f"Error extracting marks: {e}")

    state["marks"] = marks
    for key, value in state.items():
        print(f"{key}: {value}")
    return state
```

By addressing these points, you can create a more robust and reliable automated code grading system. Remember to adapt the file paths (`simple-scenario/student_solution.md`, etc.) to your actual file locations.
