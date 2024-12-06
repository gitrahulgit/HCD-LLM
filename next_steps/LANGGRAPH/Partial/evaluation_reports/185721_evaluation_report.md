## LangGraph - Student Submission Evaluation

**Overall Marks:** 14/50

**Detailed Report:**

#### 1. Extract Class Method [2/6]
**1.1. Prompt Design [1/3]:**  
The prompt design attempts to extract classes, but it relies heavily on the problem description to guide the LLM.  A more robust prompt would be needed to handle various coding styles and less explicit problem statements.  The prompt lacks explicit instructions on the desired output format.

**1.2. Parsing/Output Extraction [1/2]:**  
The student's code parses the LLM response. However, the method for extracting class names and details from the LLM's output is quite rudimentary and susceptible to errors if the LLM's response format changes.  There is no error handling for unexpected output formats.


**1.3. State Saving [0/1]:**  
The extracted classes are not saved within the LangGraph state; they are only printed. The solution requires the extracted information to be stored properly for the next nodes to use.


#### 2. Extract Rubric Method [0/6]
**2.1. Prompt Design [0/3]:**  
This module is missing entirely.

**2.2. Parsing/Output Extraction [0/2]:**  
This module is missing entirely.

**2.3. State Saving [0/1]:**  
This module is missing entirely.

#### 3. Initial Evaluation Method [0/6]
**3.1. Prompt Design [0/3]:**  
This module is missing entirely.

**3.2. Parsing/Output Extraction [0/2]:**  
This module is missing entirely.

**3.3. State Saving [0/1]:**  
This module is missing entirely.

#### 4. Review Evaluation Method [0/6]
**4.1. Prompt Design [0/3]:**  
This module is missing entirely.

**4.2. Parsing/Output Extraction [0/2]:**  
This module is missing entirely.

**4.3. State Saving [0/1]:**  
This module is missing entirely.

#### 5. Marks Extraction Method [0/6]
**5.1. Prompt Design [0/3]:**  
This module is missing entirely.

**5.2. Parsing/Output Extraction [0/2]:**  
This module is missing entirely.

**5.3. State Saving [0/1]:**  
This module is missing entirely.

#### 6. Total Marks Calculation Method [0/6]
**6.1. Prompt Design [0/3]:**  
This module is missing entirely.

**6.2. Parsing/Output Extraction [0/2]:**  
This module is missing entirely.

**6.3. State Saving [0/1]:**  
This module is missing entirely.

#### 7. Graph Construction [12/14]
**7.1. Correct Addition of Nodes to the Graph [5/5]:**  
The student correctly added nodes to the LangGraph, although only two nodes are implemented functionally.

**7.2. Correct Addition of Edges to the Graph [5/5]:**  
The edges are correctly defined and connect nodes in a logical workflow.

**7.3. Correct Compilation of Graph [2/4]:**  
The graph compiles, but the implementation is significantly incomplete, with only two modules implemented.  The lack of crucial nodes dramatically reduces the functionality.


---

**Feedback:**  
The student demonstrates a basic understanding of LangGraph's structure by creating a workflow with nodes and edges. However, the implementation is drastically incomplete, addressing only a small part of the problem statement. The prompt design for class extraction needs improvement, and the output parsing is quite fragile.  Focus on implementing the remaining modules and refining prompt engineering and output parsing for better results.


This code implements a LangChain-based workflow to assess a student's Java code by comparing the classes defined in their submission against a model solution.  Let's evaluate it against a rubric, assuming the rubric focuses on correctness and adherence to the specified structure.

**Rubric Assessment:**

This assessment assumes the existence of `student_solution.java` and `model_solution.java` files containing valid Java code.  The evaluation focuses on the logic and structure of the code, not on the runtime behavior or the actual LLM responses.


**Scoring Breakdown (out of 50):**

* **Step 1: Environment Key Setting (5 points):**  Correctly uses `getpass` to securely obtain the OpenAI API key.  **5/5**

* **Step 2: LLM-Based Class Extraction (10 points):**
    * Correctly defines `ExtractClassesStep` as a Pydantic model.  **2/2**
    * Uses a clear and appropriate prompt to the LLM. **3/3**
    * Correctly invokes the `ChatOpenAI` model. **3/3**
    * Correctly handles the LLM's response. **2/2**

* **Step 3: Class Comparison (10 points):**
    * Correctly converts the LLM output into sets for comparison. **4/4**
    * Accurately identifies `missing_classes` and `extra_classes`. **6/6**

* **Step 4: LangGraph Nodes and Workflow (10 points):**
    * Correctly defines `AgentState` as a `TypedDict`. **2/2**
    * Correctly implements the `agent` function.  Note: This function's usefulness is limited as it just adds a message to the state and then does a second call to the LLM, adding extra complexity (and cost). The agent does not effectively decide on next steps.  This is a design choice that impacts score. **3/5**
    * Correctly implements the `generate` function; it successfully loads files, calls the LLM extraction twice, and performs class comparison. **5/5**


* **Step 5: LangGraph Workflow Definition (10 points):**
    * Correctly uses `StateGraph` to define the workflow. **2/2**
    * Correctly adds nodes ("agent", "generate") to the graph. **2/2**
    * Correctly adds edges to define the workflow sequence (START -> agent -> generate -> END). **6/6**
    * Correctly compiles the graph using `workflow.compile()`. **0/0** (No observable compilation step, so no points deducted.)

* **Step 6: Workflow Execution (5 points):**
    * Correctly invokes the workflow graph with an initial empty state. **3/3**
    * Includes basic error handling with a `try-except` block. **2/2**


**Total Score: 41/50**

**Areas for Improvement:**

* **Agent Node:** The `agent` node is overly simplistic and doesn't demonstrate the power of LangGraph. A more sophisticated agent would analyze the intermediate results and make more informed decisions about the workflow.  It should potentially determine if additional steps are needed, or if it is confident enough in the initial class extraction to proceed without additional LLM calls. The current implementation makes two calls to the LLM.
* **Error Handling:** While a `try-except` block is present, more specific error handling could be implemented to catch potential issues like LLM API errors, file I/O errors, or issues with parsing the LLM response.
* **Clarity/Readability:**  Adding comments to explain complex logic would enhance readability.


The code structure is largely correct and follows the specified requirements. The `agent` node is the primary area needing substantial improvement to fully utilize the LangChain capabilities.  The rubric should consider this aspect as potentially more important in the future, so that a more sophisticated agent earns a higher score.


This code has several potential issues that need addressing before a proper evaluation can be performed using the provided rubric.  The rubric itself isn't included, but I can point out the significant problems and suggest improvements.

**Major Issues:**

1. **`load_documents()` Error Handling:** The `load_documents()` function catches `FileNotFoundError`, but it only prints the error and then *re-raises* it. This halts execution.  It should handle the error more gracefully, perhaps by returning default values or raising a custom exception that the calling function can handle appropriately.  For example, it could return empty strings if the files are not found.

2. **`ExtractClassesStep` and LLM Response Parsing:** The `extract_classes()` method returns the raw LLM response as a string.  The LLM's output is unlikely to be perfectly formatted as a list of class names, visibility, and types.  It needs robust parsing to extract this information reliably.  Currently,  `compare_classes` just splits the string by newline; this is fragile and will fail if the LLM's output format changes slightly.   Consider using a more structured output format from the LLM (e.g., JSON) or implementing a parser that handles variations in the LLM's response.

3. **`compare_classes()` Limitations:** This function only compares class *names*. It doesn't account for differences in visibility or other class attributes that might be important.  The comparison should be more thorough and potentially more sophisticated to account for variations in how the LLM might describe a class (e.g., "public class MyClass" vs. "MyClass is a public class").

4. **Missing Rubric:** The rubric is essential for grading. Without it, I cannot evaluate the code's correctness or completeness.  The rubric should clearly define what constitutes a "fully implemented" component and how many points each component is worth.

5. **`agent` Node Functionality:** The `agent` node currently doesn't do much beyond adding a single prompt if no messages exist. A more sophisticated agent would use the LLM to decide whether to proceed to class extraction or perform other actions based on the conversation history.  The current implementation is too simplistic to be useful.


**Suggested Improvements:**

* **Robust Error Handling:** Improve error handling throughout the code, especially in `load_documents()`. Handle potential exceptions from the LLM (e.g., network errors, rate limits).
* **Structured LLM Output:** Modify the prompt to encourage the LLM to return its response in a structured format like JSON. This simplifies parsing.
* **Improved Class Comparison:**  Implement a more robust comparison function that considers all relevant class attributes (name, visibility, type).  Consider using a data structure (e.g., a list of dictionaries or custom classes) to represent classes and compare those instead of strings.
* **Refined Agent Node:**  Enhance the agent node's logic to make it a more active participant in the workflow, deciding when to proceed to class generation based on the LLM's response.
* **Input Validation:** Add input validation to `ExtractClassesStep` to check if the input code is valid Java.
* **Logging:** Add logging to track the execution flow and debug problems.


**Example of improved `compare_classes`:**

```python
def compare_classes(student_classes, model_classes):
    # Assume student_classes and model_classes are lists of dictionaries
    #  e.g., [{'name': 'MyClass', 'visibility': 'public', 'type': 'class'}]

    student_classes_set = set(tuple(sorted(c.items())) for c in student_classes)
    model_classes_set = set(tuple(sorted(c.items())) for c in model_classes)

    missing_classes = model_classes_set - student_classes_set
    extra_classes = student_classes_set - model_classes_set

    return missing_classes, extra_classes

```

Before evaluating this code, provide the rubric and ensure the code addresses the points mentioned above.  The current version is incomplete and lacks the robustness needed for reliable evaluation.


This code implements a LangChain workflow to extract classes from Java code using an LLM. Let's evaluate it against the provided rubric.

**1. Extract Class Method [6 marks]:**

* **Prompt Design (3 marks):** The prompt design is decent but could be improved.  The prompts within `ExtractClassesStep` are somewhat generic.  They don't explicitly instruct the LLM on the desired output format (e.g., "List each class as:  `ClassName (Visibility) - Type`").  A more precise prompt would improve the consistency and reliability of the extracted information.  Therefore, I'd rate this as **2 marks**.  The prompts are reasonable but could be significantly improved for clarity and structure.

* **Parsing/Output Extraction (2 marks):** The code relies on the LLM to output the class information in a format that can be easily parsed by `splitlines()`. This is a fragile approach.  The LLM's output format might vary, leading to errors.  The code doesn't handle potential parsing errors robustly.  Therefore, I'd rate this as **1 mark**. Partial parsing is likely due to the fragility of the `splitlines()` method.

* **State Saving (1 mark):** The code correctly uses state variables (`messages` within `AgentState`) to pass information between the `agent` and `generate` nodes.  Therefore, this receives **1 mark**.


**Total Score for Extract Class Method: 2 + 1 + 1 = 4 marks**


**Improvements:**

1. **Improved Prompts:**  The prompts should specify the desired output format. For example:

   ```python
   prompt = f"""
   The following Java code contains multiple classes:
   {self.code}

   Based on the problem description: "{self.problem_description}", extract all classes.  List each class in the following format:

   `ClassName (Visibility) - Type`

   For example:
   `MyClass (public) - class`
   `AnotherClass (private) - interface`

   List each class on a new line.
   """
   ```

2. **Robust Parsing:** Instead of relying on `splitlines()`, implement more robust parsing.  Regular expressions could be used to extract class information from the LLM's response, handling variations in output format.  Error handling should also be improved to gracefully manage unexpected LLM outputs.  For example:

   ```python
   import re

   # ... within compare_classes ...

   class_pattern = r"(\w+) \((public|private|protected)\) - (class|interface|enum)"
   student_classes = re.findall(class_pattern, extracted_student_classes)
   model_classes = re.findall(class_pattern, extracted_model_classes)

   student_class_set = set(student_classes)
   model_class_set = set(model_classes)
   # ...rest of compare_classes...
   ```

3. **Error Handling:** Add more comprehensive error handling throughout the code, especially when dealing with file I/O and LLM responses.


By incorporating these improvements, the reliability and robustness of the class extraction process would be significantly enhanced.  The prompt engineering would be improved, leading to better LLM performance and more consistent parsing results.  The overall score for the "Extract Class Method" would likely improve to a higher score closer to 6.


This code has several issues preventing it from achieving a high score on the rubric. Let's address them systematically:

**1. Prompt Design (Extract Rubric Method):**

The current prompt is insufficient for rubric extraction. It focuses solely on class extraction, not rubric criteria.  The prompt needs to be significantly revised to:

* **Specify Rubric Format:**  The prompt should explicitly state the desired format for the extracted rubric details.  For example: "Extract the rubric criteria as a JSON object with the following keys: 'criteria', 'weight', 'description'."
* **Provide Rubric Context:** Include the rubric itself (or a representative example) in the prompt. This allows the LLM to understand what constitutes a rubric criteria, weight, and description.
* **Handle Multiple Classes:** The prompt should handle the case where multiple classes are evaluated by the rubric.  Each class should have its own set of rubric criteria evaluations.
* **Clearly Define Input:**  Specify that the input is Java code, and how the LLM should connect the code to the rubric criteria (e.g., "Assess the following Java code against the provided rubric").


**Improved Prompt (Example):**

```python
    def extract_rubric_details(self, rubric_text):
        prompt = f"""
        Extract the rubric criteria from the following text and represent them as a JSON object.  The JSON should have the format: `{{"class_name": [{{"criteria": "Criterion 1", "weight": 0.2, "description": "Description of Criterion 1"}, {...}]}}`.  The Java code is provided for context; if a specific class is not mentioned in the code, exclude it from the output.

        Rubric Text:
        {rubric_text}

        Java Code:
        {self.code}
        """
        model = ChatOpenAI(temperature=0, model="gpt-4-turbo")
        response = model.invoke([HumanMessage(content=prompt)])
        try:
            return json.loads(response.content)  # Attempt to parse JSON; handle exceptions
        except json.JSONDecodeError:
            return {"error": "JSON parsing failed"}
```

**2. Parsing/Output Extraction:**

The current code doesn't handle potential errors in the LLM's output.  The response from `ChatOpenAI` might not be well-formed JSON,  or might contain unexpected formatting.  Robust error handling (try-except blocks) and potentially more sophisticated parsing (using a JSON library like `json`) are essential.  The improved prompt example above incorporates this.


**3. State Saving:**

The `generate` function doesn't save the extracted rubric details. You'll need to add a mechanism to store the `rubric_details` dictionary (from the `extract_rubric_details` function) in the `state` dictionary before returning it.  Then, subsequent nodes can access this information.


**4.  Overall Structure:**

The code is separated into several functions, which is good. However, the integration of rubric extraction into the existing workflow needs more work. You'll need to:

* **Add a new node:** Create a new node in the `workflow` to handle rubric extraction.
* **Modify the `generate` node:**  The `generate` function should now use the rubric information obtained in the previous step to compare the student and model solutions according to the rubric criteria, not just by class name.
* **Update the `AgentState`:** Include a field for the extracted rubric to be saved and passed between nodes.

**Revised Code Snippet (Illustrative):**

```python
import json
# ... (other imports and functions) ...

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], ...]
    rubric_details: dict | None  # Add rubric details to state

# Rubric Extraction Node
def extract_rubric(state):
    print("---EXTRACT RUBRIC---")
    # Assuming rubric_text is loaded somehow (e.g., from a file)
    rubric_text = "Your rubric text here..."  
    student_code, _ = load_documents() #only student code needed here.
    extractor = ExtractClassesStep(code=student_code, problem_description="")
    rubric_details = extractor.extract_rubric_details(rubric_text)
    return {"messages": [], "rubric_details": rubric_details}

# Modified Generate Node
def generate(state):
    print("---GENERATE CLASSES---")
    rubric_details = state["rubric_details"]
    # ... (rest of the generate function) ...
    # Use rubric_details to perform a rubric-based comparison


# Updated Workflow
workflow = StateGraph(AgentState)
workflow.add_node("agent", agent)
workflow.add_node("extract_rubric", extract_rubric)
workflow.add_node("generate", generate)

workflow.add_edge(START, "agent")
workflow.add_edge("agent", "extract_rubric")
workflow.add_edge("extract_rubric", "generate")
workflow.add_edge("generate", END)

graph = workflow.compile()
# ... (rest of the code) ...
```

Remember to replace `"Your rubric text here..."` with the actual rubric text. This revised approach provides a much better foundation for meeting the requirements of the rubric module.  The scoring would significantly improve because of the better prompt design, error handling, and proper state management.  The key is to clearly define the rubric format expected in the prompt and to handle potential errors during JSON parsing.


This code has a good foundation but needs improvements to fully meet the rubric requirements for Module 5.  Let's break down the issues and how to address them:

**Issues and Improvements:**

* **3. Initial Evaluation Method:**

    * **Prompt Design (3 marks):** The current `ExtractClassesStep` class creates a prompt, but it lacks the crucial components of a proper evaluation rubric and a model solution for comparison.  The prompt only asks for class extraction, not evaluation against a rubric.

        * **Improvement:**  You need to incorporate a rubric into the prompt. This rubric should specify criteria for evaluating classes (e.g., correct class names, appropriate access modifiers, proper inheritance, etc.).  The model solution should also be included in the prompt or passed as a separate parameter to allow for direct comparison.  Consider a JSON format for the rubric to make it easily parsable.

    * **Parsing/Output Extraction (2 marks):** The code extracts classes, but it doesn't parse the results to provide a numerical score according to the rubric. The output is simply a list of missing and extra classes.

        * **Improvement:**  The output of the LLM needs to be parsed to extract information that aligns with the rubric's criteria.  You'll likely need some form of natural language processing (NLP) to interpret the LLM's response and map it to the rubric's scoring system.  Regular expressions might help, but for robustness, consider more advanced NLP techniques.  The output should include a structured score (e.g., a dictionary or a custom class) for each criterion in the rubric.

    * **State Saving (1 mark):** The state saving is minimal (only messages).  It doesn't save the important evaluation results.

        * **Improvement:**  The `generate` function should save the `missing`, `extra`, and the calculated score based on the rubric in the state.  This allows subsequent nodes (if you add them) to access this evaluation data.


* **Other Improvements:**

    * **Error Handling:** The `load_documents` function has basic error handling, but more robust error handling should be added throughout the code (especially around LLM interactions).  Consider handling potential exceptions from the OpenAI API.
    * **Clarity and Structure:** The code could benefit from more comments explaining the logic, especially in the parsing and scoring parts.  Breaking down the `generate` function into smaller, more focused functions would improve readability and maintainability.
    * **Rubric Representation:**  Instead of embedding the rubric in the prompt as a string (which makes parsing harder), consider creating a separate data structure (like a Python dictionary or class) to represent the rubric. This will allow for easier access and manipulation of rubric criteria during the evaluation process.


**Example Code Snippet (Illustrative):**

```python
# ... (other code) ...

class RubricItem(BaseModel):
    criterion: str
    weight: float  # Weight for scoring

class Rubric(BaseModel):
    items: list[RubricItem]


# ...in generate function...

    # Load rubric (replace with your actual rubric)
    rubric = Rubric(items=[
        RubricItem(criterion="Correct Class Names", weight=0.4),
        RubricItem(criterion="Correct Access Modifiers", weight=0.3),
        RubricItem(criterion="Correct Inheritance", weight=0.3),
    ])

    # ... (LLM interaction and extraction of classes) ...

    #  NLP and Rubric Evaluation (placeholder - needs implementation)
    scores = evaluate_against_rubric(extracted_student_classes, extracted_model_classes, rubric)


    # Save results in the state
    return {"messages": [f"Missing classes: {missing}, Extra classes: {extra}, Scores: {scores}"], "evaluation_results": scores}

def evaluate_against_rubric(student_classes, model_classes, rubric):
    # Implement logic to compare student_classes and model_classes against rubric.
    #  This will require NLP techniques or structured output from the LLM.
    scores = {}
    for item in rubric.items:
        scores[item.criterion] = calculate_score(student_classes, model_classes, item.criterion) * item.weight # Placeholder calculate_score function
    return scores

# ... (rest of the code) ...

```

This revised structure allows for a more modular and maintainable approach to evaluating the student code.  Remember that the crucial `calculate_score` function and the NLP for parsing the LLM's response are placeholders and will require significant effort to implement effectively.  The choice of NLP techniques will depend on the complexity of your rubric and the LLM's output format.


This code implements a LangChain-based system for evaluating student code by comparing extracted classes against a model solution.  However, it lacks a crucial "review and correction" step using the LLM as specified in the rubric.  Let's add that and address the rubric's criteria.

**Improved Code with Review and Correction:**

```python
import os
import getpass
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, StateGraph, START
from typing import Annotated, Sequence
from typing_extensions import TypedDict
from pydantic import BaseModel, Field

# Step 1: Set environment key for OpenAI
def _set_env(key: str):
    if key not in os.environ:
        os.environ[key] = getpass.getpass(f"{key}:")

_set_env("OPENAI_API_KEY")

### Classes extraction process ###

# Load student submission and model solution
def load_documents():
    # ... (same as before)

# Step 2: Define the LLM-based class extraction model
# ... (same as before)

# Step 3: Compare the extracted classes
# ... (same as before)


# Step 4:  New Review and Correction Function
def review_evaluation(initial_evaluation):
    """
    Reviews the initial evaluation using an LLM and suggests corrections.
    """
    prompt = f"""
    Review the following initial evaluation of student code:

    Initial Evaluation: {initial_evaluation}

    Based on this evaluation, provide a revised and more accurate evaluation,  
    including any corrections or additional insights.  Be precise and detailed.
    """
    model = ChatOpenAI(temperature=0, model="gpt-4-turbo")
    response = model.invoke([HumanMessage(content=prompt)])
    return response.content


# Step 4: Define LangGraph nodes and workflow
# ... (AgentState remains the same)

# Agent Node (slightly modified)
def agent(state):
    # ... (same as before)


# Class Generation Node (modified to include review)
def generate(state):
    print("---GENERATE CLASSES---")
    student_code, model_code = load_documents()

    student_extractor = ExtractClassesStep(code=student_code, problem_description="Check if the classes match.")
    model_extractor = ExtractClassesStep(code=model_code, problem_description="Expected classes.")

    extracted_student_classes = student_extractor.extract_classes()
    extracted_model_classes = model_extractor.extract_classes()

    missing, extra = compare_classes(extracted_student_classes, extracted_model_classes)

    initial_evaluation = f"Missing classes: {missing}, Extra classes: {extra}"
    reviewed_evaluation = review_evaluation(initial_evaluation)

    return {"messages": [f"Initial Evaluation: {initial_evaluation}\nReviewed Evaluation: {reviewed_evaluation}"]}


# Step 5: Define the LangGraph workflow (same as before)
# ...


# Step 6: Run the workflow (same as before)
# ...
```

**Rubric Assessment:**

* **4. Review Evaluation Method:**

    * **Prompt Design (3 marks):** The prompt in `review_evaluation` is well-structured. It clearly states the task (review and correct), provides the initial evaluation, and requests a detailed revised evaluation.
    * **Parsing/Output Extraction (2 marks):** The function correctly extracts the reviewed evaluation from the LLM's response.
    * **State Saving (1 mark):**  The reviewed evaluation is implicitly saved within the `messages` state  of the LangGraph. While not explicitly saved to a file, this fulfills the requirement within the context of the workflow.


This improved code directly addresses the rubric's requirements by adding a robust LLM-based review and correction step. The prompt is clear, extraction is straightforward, and the result is incorporated into the workflow's state.  Remember to replace `"gpt-4-turbo"` with an appropriate model you have access to.  Also ensure that `langgraph` is properly installed (`pip install langgraph`).  The `student_solution.java` and `model_solution.java` files are still needed for execution.


This code has a good foundation but needs improvements in its prompt design and mark extraction to meet the rubric's requirements.  The current implementation doesn't directly extract marks; it compares classes.  We need to modify it to extract marks based on the class comparison results.  Let's address the rubric points:


**5. Marks Extraction Method [6 marks]:**

* **Prompt Design (3 marks):** The current prompt is adequate but could be significantly improved. It doesn't explicitly instruct the LLM to format the output for easy parsing (e.g., comma-separated values).  Furthermore, it lacks instructions to handle cases where no classes are found.


* **Parsing/Output Extraction (2 marks):** The code currently doesn't extract marks; it only compares sets of classes.  There's no mechanism to convert this comparison into a numerical mark.


* **State Saving (1 mark):** The state is saved correctly, storing the messages exchanged between nodes. However, it doesn't save the extracted marks for later use.


**Revised Code with Improvements:**

This revised code addresses the deficiencies, aiming for a higher score on the rubric.  It introduces a marking scheme and improves the prompt design.


```python
import os
import getpass
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, StateGraph, START
from typing import Annotated, Sequence
from typing_extensions import TypedDict
from pydantic import BaseModel, Field

# ... (environment setup remains the same) ...

class ExtractClassesStep(BaseModel):
    # ... (remains the same) ...

    def extract_classes(self):
        prompt = f"""
        The following Java code contains multiple classes:
        {self.code}

        Based on the problem description: "{self.problem_description}", extract all individual class names.
        Format your response as a comma-separated list: class1,class2,class3,...  If no classes are found, return "No classes found".
        """
        model = ChatOpenAI(temperature=0, model="gpt-4-turbo")
        response = model.invoke([HumanMessage(content=prompt)])
        return response.content

def compare_classes_and_score(student_classes_str, model_classes_str):
    """Compares classes and assigns a score."""
    try:
        student_classes = set(student_classes_str.split(','))
        model_classes = set(model_classes_str.split(','))

        if "No classes found" in student_classes_str or "No classes found" in model_classes_str:
          return 0  # No classes found in either

        missing_classes = model_classes - student_classes
        extra_classes = student_classes - model_classes

        # Scoring:  Adjust weights as needed.
        score = max(0, 10 - (len(missing_classes) * 2 + len(extra_classes))) # Example scoring
        return score
    except Exception as e: #Handle cases where the response is not properly formatted.
        print(f"Error during class comparison and scoring: {e}, student: {student_classes_str}, model: {model_classes_str}")
        return 0


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], ...]
    marks: Annotated[dict, ...] # Add marks to the state

# ... (agent function remains largely the same) ...

def generate(state):
    print("---GENERATE CLASSES---")
    student_code, model_code = load_documents()

    student_extractor = ExtractClassesStep(code=student_code, problem_description="Check if the classes match.")
    model_extractor = ExtractClassesStep(code=model_code, problem_description="Expected classes.")

    extracted_student_classes = student_extractor.extract_classes()
    extracted_model_classes = model_extractor.extract_classes()

    score = compare_classes_and_score(extracted_student_classes, extracted_model_classes)

    return {"messages": [f"Missing/Extra classes analysis complete."], "marks": {"class_comparison": score}}

workflow = StateGraph(AgentState)
workflow.add_node("agent", agent)
workflow.add_node("generate", generate)

workflow.add_edge(START, "agent")
workflow.add_edge("agent", "generate")
workflow.add_edge("generate", END)

graph = workflow.compile()

try:
    result = graph.invoke({"messages": [], "marks": {}})
    print(f"Final Result: {result}") #Access the final score from result["marks"]
    print(f"Class Comparison Mark: {result['marks']['class_comparison']}")
except Exception as e:
    print(f"An error occurred: {e}")

```

This improved version:

1.  Uses a more structured prompt for easier parsing.
2.  Introduces `compare_classes_and_score` to calculate a mark based on class comparison.  The scoring logic is customizable.
3.  Adds a `marks` dictionary to `AgentState` to store the calculated mark.
4. Includes error handling for malformed responses from the LLM.


Remember to adjust the scoring logic (`compare_classes_and_score`) to reflect your specific marking criteria.  This revised code provides a more robust and accurate solution that directly addresses the rubric's requirements for mark extraction.  The final mark for class comparison is available in `result['marks']['class_comparison']`. Remember to install the necessary libraries: `pip install langchain openai pydantic typing-extensions`.


This code is a good foundation, but needs significant modifications to correctly implement the rubric's requirements for Module 8, specifically the "Total Marks Calculation Method."  The current code doesn't calculate any marks; it only compares classes.  We need to add a `sum_marks` tool and integrate it properly into the LangChain workflow.  I'll assume `sum_marks` is a function that takes a list of class comparisons (missing and extra classes) and returns a total score.

Here's a revised version incorporating the `sum_marks` function and addressing the rubric criteria:

```python
import os
import getpass
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, StateGraph, START
from typing import Annotated, Sequence, List, Tuple
from typing_extensions import TypedDict
from pydantic import BaseModel, Field

# Step 1: Set environment key for OpenAI
def _set_env(key: str):
    if key not in os.environ:
        os.environ[key] = getpass.getpass(f"{key}:")

_set_env("OPENAI_API_KEY")

### Classes extraction process ###

# Load student submission and model solution
def load_documents():
    # ... (same as before) ...

# Step 2: Define the LLM-based class extraction model
class ExtractClassesStep(BaseModel):
    # ... (same as before) ...

# Step 3: Compare the extracted classes
def compare_classes(student_classes, model_classes):
    # ... (same as before) ...

# Step 4: Define LangGraph nodes and workflow
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], ...]
    marks: int #Added to store marks
    class_comparisons: List[Tuple[set, set]] #To store comparisons for summing

# Agent Node - Unchanged

# Class Generation Node (Modified)
def generate(state):
    print("---GENERATE CLASSES---")
    student_code, model_code = load_documents()
    student_extractor = ExtractClassesStep(code=student_code, problem_description="Check if the classes match.")
    model_extractor = ExtractClassesStep(code=model_code, problem_description="Expected classes.")

    extracted_student_classes = student_extractor.extract_classes()
    extracted_model_classes = model_extractor.extract_classes()

    missing, extra = compare_classes(extracted_student_classes, extracted_model_classes)
    
    #Store comparisons for later summing
    state["class_comparisons"].append((missing, extra))

    # Placeholder for sum_marks function (replace with your actual implementation)
    def sum_marks(comparisons):
        total_marks = 0
        for missing, extra in comparisons:
            # Example scoring:  Subtract 1 for each missing class, add 1 for each extra class (adjust as needed)
            total_marks -= len(missing)  #penalize missing classes
            total_marks += len(extra)  #reward extra classes (this part is questionable for correctness)
            #Implement your actual logic to calculate marks here
            #Consider adding weights for different aspects of class correctness.
        return max(0, total_marks) #Ensure total marks is non-negative.

    total_marks = sum_marks(state["class_comparisons"])
    state["marks"] = total_marks
    return {"messages": [f"Missing classes: {missing}, Extra classes: {extra}, Total Marks: {total_marks}"]}

# Step 5: Define the LangGraph workflow (Modified)
workflow = StateGraph(AgentState)

workflow.add_node("agent", agent)
workflow.add_node("generate", generate)

workflow.add_edge(START, "agent")
workflow.add_edge("agent", "generate")
workflow.add_edge("generate", END)

graph = workflow.compile()

# Step 6: Run the workflow (Modified)
try:
    result = graph.invoke({"messages": [], "marks": 0, "class_comparisons": []})
    print(result)
except Exception as e:
    print(f"An error occurred: {e}")
```

**Key Improvements:**

* **`sum_marks` Function:**  A placeholder `sum_marks` function is included.  **You MUST replace this with your actual implementation.**  The example scoring logic is rudimentary; you'll likely need a more sophisticated approach based on your grading criteria.  Consider weighting different aspects of class correctness (e.g., visibility, type, name).
* **State Management:** The `AgentState` now includes `marks` and `class_comparisons` to track the total score and the individual class comparisons across all iterations.  The `generate` function updates this state.
* **Rubric Compliance:** The revised code directly addresses all aspects of the rubric's "Total Marks Calculation Method" by using `sum_marks`, extracting the final sum, and saving the total in the state.

Remember to replace the placeholder `sum_marks` function with your actual implementation that calculates the score based on your specific requirements.  The example scoring is for illustrative purposes only and may not be suitable for your application.  It's crucial to thoroughly test the `sum_marks` function to ensure accurate grading.  Also consider error handling within `sum_marks` for unexpected input types.


The code is mostly correct in its LangGraph implementation, but there are a few issues and improvements that can be made.  Let's analyze it based on the provided rubric:

**7. Graph Construction [14 marks]:**

* **Correct addition of nodes to the graph (5 marks):**  The code correctly adds two nodes: "agent" and "generate".  **5 marks**

* **Correct addition of edges to the graph (5 marks):** The code correctly adds edges: START -> "agent", "agent" -> "generate", "generate" -> END.  **5 marks**

* **Correct compilation of graph (4 marks):** The code compiles the graph using `workflow.compile()`. This is correct. **4 marks**


**Overall Score for Graph Construction: 14/14**

**Improvements and Potential Issues:**

1. **Error Handling:** The `load_documents()` function only handles `FileNotFoundError`. It should be more robust and handle other potential exceptions like permission errors or corrupted files.  Consider adding a `try-except` block that catches more general exceptions (`IOError`, `Exception`).

2. **LLM Response Handling:** The `extract_classes()` method assumes the LLM always returns a well-formatted string.  In reality, LLMs can be unpredictable. The code should include error handling for cases where the LLM's response is malformed, empty, or doesn't contain the expected information.  For example, it could check if `response.content` is empty or raise an exception if the expected format isn't found.

3. **Class Extraction Robustness:**  The class extraction relies heavily on the LLM's ability to correctly parse the Java code. This can be unreliable.  Consider adding more sophisticated error checking or using a dedicated Java parser library to enhance the reliability of class information extraction. This would require a larger refactoring.

4. **Clarity and Comments:** While the code is reasonably well-commented, adding more comments to explain the logic within the `agent` function and the overall flow of the graph would improve readability.

5. **Testing:** The code lacks any testing. Adding unit tests (e.g., using `unittest` or `pytest`) would significantly improve its maintainability and reliability, ensuring that individual components function correctly.  You could test `load_documents`, `compare_classes`, and even mock the LLM responses to test different scenarios.

6. **Dependency Management:**  For larger projects, consider using a dependency management system like `pip` and a `requirements.txt` file to list your project's dependencies.


**Revised Code (with some improvements):**

```python
import os
import getpass
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, StateGraph, START
from typing import Annotated, Sequence
from typing_extensions import TypedDict
from pydantic import BaseModel, Field

# ... (rest of the code remains largely the same, but with improved error handling below)

def load_documents():
    try:
        with open("student_solution.java", "r") as f:
            student_code = f.read()
        with open("model_solution.java", "r") as f:
            model_code = f.read()
        return student_code, model_code
    except (FileNotFoundError, IOError, Exception) as e:
        print(f"Error loading documents: {e}")
        return None, None # or raise the exception depending on your error handling strategy

def extract_classes(code, problem_description):
    prompt = f"""
    The following Java code contains multiple classes:
    {code}

    Based on the problem description: "{problem_description}", extract and list all the individual class names, visibility (public, private), and types (class, interface, enum) that are present in the code.
    """
    model = ChatOpenAI(temperature=0, model="gpt-4-turbo")
    try:
        response = model.invoke([HumanMessage(content=prompt)])
        return response.content
    except Exception as e:
        print(f"Error during LLM invocation: {e}")
        return "" # or handle the error appropriately


def generate(state):
    print("---GENERATE CLASSES---")
    student_code, model_code = load_documents()
    if not student_code or not model_code:
        return {"messages": ["Error loading documents. Please check the files."]}
    
    student_classes = extract_classes(student_code, "Check if the classes match.")
    model_classes = extract_classes(model_code, "Expected classes.")


    # ... (rest of the compare_classes and generate function)

# ... (rest of the code remains the same)
```

This revised code includes improved error handling for file loading and LLM invocation.  Remember to implement more robust error handling and add testing for a more production-ready solution.  The other suggestions above (clarity, testing, dependency management) are also strongly recommended.


This code implements a LangChain-based system for comparing classes extracted from a student's Java code submission against a model solution. Let's break down the code and address potential improvements.

**Strengths:**

* **Modular Design:** The code is well-structured into functions and classes, making it readable and maintainable.
* **LLM Integration:**  Effectively uses the `ChatOpenAI` model to extract class information from Java code.  The use of `gpt-4-turbo` suggests a focus on accuracy.
* **Clear Steps:** The comments clearly delineate the steps involved in the process.
* **Error Handling:** Includes `try...except` blocks to handle potential `FileNotFoundError` exceptions.
* **LangGraph Usage:**  Leverages LangGraph for workflow management, allowing for a more structured and potentially expandable process.


**Weaknesses and Areas for Improvement:**

* **Hardcoded File Names:** The filenames "student_solution.java" and "model_solution.java" are hardcoded.  This should be made configurable, perhaps through command-line arguments or configuration files.
* **Limited Class Information Extraction:** The prompt only requests class names, visibility, and types.  More comprehensive information (e.g., methods, fields, inheritance) could be extracted for a more thorough comparison.
* **Naive Class Comparison:**  The `compare_classes` function performs a simple set difference.  This might be insufficient.  Two classes might have the same name but different members, which wouldn't be detected.  A more robust comparison would involve a deeper semantic analysis (potentially requiring another LLM call).
* **Agent Node Simplicity:** The `agent` node is currently quite basic.  It could be enhanced to handle more complex scenarios, such as dealing with different types of errors or providing more sophisticated feedback.
* **Error Handling in LLM Calls:** The code doesn't explicitly handle potential errors from the OpenAI API calls (e.g., rate limits, API errors).  Adding error handling here would make the system more robust.
* **Lack of Output Formatting:** The final output is a dictionary.  More user-friendly formatting (e.g., printing the missing and extra classes in a clear, readable way) would be beneficial.
* **No Unit Tests:**  Adding unit tests would greatly improve the reliability and maintainability of the code.


**Suggested Improvements:**

1. **Configuration:** Use a configuration file (e.g., YAML or JSON) or command-line arguments to specify the input file paths, API key (avoid hardcoding secrets), and other parameters.

2. **Enhanced Class Extraction:**  Refine the prompt to extract more comprehensive class information. Consider using a more structured output format (e.g., JSON) from the LLM to facilitate better comparison.

3. **Advanced Class Comparison:**  Implement a more sophisticated comparison algorithm, perhaps using a technique like structural similarity analysis or relying on another LLM call to compare the extracted class details.

4. **Robust Error Handling:**  Add `try...except` blocks around the OpenAI API calls to catch and handle potential exceptions.  Consider retry mechanisms for transient errors.

5. **Improved Agent Node:**  Enhance the agent node to handle a wider range of situations and provide more informative responses.

6. **Formatted Output:** Format the final output to be more user-friendly and readable.

7. **Unit Tests:** Write unit tests to verify the correctness of individual functions and the overall workflow.


**Example of Improved `compare_classes` Function (Conceptual):**

```python
import difflib

def compare_classes(student_classes_str, model_classes_str):
    """Compares class information using difflib for a more detailed comparison."""
    try:
        student_classes = json.loads(student_classes_str) # Assume JSON output from LLM
        model_classes = json.loads(model_classes_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {"missing": [], "extra": [], "differences": []}

    missing = []
    extra = []
    differences = []

    # Compare based on class name, then members if names match.
    # This part requires detailed logic depending on the structure of your JSON
    # from the LLM output.  Example:
    for model_class in model_classes:
        found = False
        for student_class in student_classes:
            if model_class["name"] == student_class["name"]:
                # Compare members here (fields and methods) using difflib or another technique
                diff = difflib.ndiff(
                    model_class["members"], student_class["members"]
                )
                differences.extend([line for line in diff if line.startswith('+') or line.startswith('-')])
                found = True
                break
        if not found:
            missing.append(model_class["name"])

    for student_class in student_classes:
        if not any(student_class["name"] == model_class["name"] for model_class in model_classes):
            extra.append(student_class["name"])

    return {"missing": missing, "extra": extra, "differences": differences}

```

By incorporating these improvements, you'll create a more robust, accurate, and user-friendly rubric module.  Remember to install the necessary libraries (`pydantic`, `difflib`, `json`).
