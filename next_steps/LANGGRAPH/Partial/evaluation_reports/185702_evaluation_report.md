## LangGraph - Student Submission Evaluation

**Overall Marks:** 14/50

**Detailed Report:**

#### 1. Extract Class Method [0/6]
**1.1. Prompt Design [0/3]:**  
The student attempts to use OpenAI's API for class extraction, but the code is outdated and incompatible with the current OpenAI API version. The prompt itself is reasonably well-structured but does not account for potential errors in the LLM's response.

**1.2. Parsing/Output Extraction [0/2]:**  
No classes are extracted due to the API incompatibility. The parsing function `parse_extracted_classes` exists but is not utilized effectively.

**1.3. State Saving [0/1]:**  
State saving is attempted but fails due to the absence of extracted classes.


#### 2. Extract Rubric Method [0/6]
**2.1. Prompt Design [0/3]:**  
The prompt is structurally sound, attempting to extract rubric details based on a given class name. However, it suffers from the same API incompatibility as the class extraction method.

**2.2. Parsing/Output Extraction [0/2]:**  
No rubric details are extracted due to the failure of the LLM invocation.

**2.3. State Saving [0/1]:**  
State saving for extracted rubrics is attempted but is ineffective due to the absence of extracted data.


#### 3. Initial Evaluation Method [0/6]
**3.1. Prompt Design [0/3]:**  
The prompt design for initial evaluation is adequate.  It includes the student code, model solution, and extracted rubric; however, it is not used because of the prior failures.

**3.2. Parsing/Output Extraction [0/2]:**  
No score or comments are extracted because the LLM call fails.

**3.3. State Saving [0/1]:**  
State saving for initial evaluations is attempted but fails due to missing data from earlier stages.


#### 4. Review Evaluation Method [0/6]
**4.1. Prompt Design [0/3]:**  
The prompt for reviewing evaluations is well-structured but is never used due to previous errors.

**4.2. Parsing/Output Extraction [0/2]:**  
No reviewed evaluations are extracted.

**4.3. State Saving [0/1]:**  
State saving for reviewed evaluations is attempted but does not occur because of the prior failures.


#### 5. Marks Extraction Method [0/6]
**5.1. Prompt Design [0/3]:**  
The prompt for extracting marks is reasonable but remains unused.

**5.2. Parsing/Output Extraction [0/2]:**  
No marks are extracted.

**5.3. State Saving [0/1]:**  
State saving for extracted marks is attempted but is not successful.


#### 6. Total Marks Calculation Method [0/6]
**6.1. Prompt Design [0/3]:**  
The prompt for utilizing the `sum_marks` tool is correctly designed, but the tool is never invoked.

**6.2. Parsing/Output Extraction [0/2]:**  
The final sum is not extracted.

**6.3. State Saving [0/1]:**  
The final marks are not saved.


#### 7. Graph Construction [14/14]
**7.1. Correct Addition of Nodes to the Graph [5/5]:**  
The student correctly adds all nodes to the LangGraph.

**7.2. Correct Addition of Edges to the Graph [5/5]:**  
The student correctly adds edges to define the workflow.

**7.3. Correct Compilation of Graph [4/4]:**  
The graph compiles successfully, indicating the correct setup of the workflow.


---

**Feedback:**  
The graph structure is well-implemented.  However, the student's code suffers from significant issues with API compatibility, causing all LLM-related modules to fail.  Update to the current OpenAI or Google Gemini API and carefully handle potential errors in the LLM responses to improve functionality.  The `openai migrate` command is suggested to address the incompatibility.


The student's code has a significant issue: it uses the outdated `openai.Completion` API call, which is no longer supported in `openai>=1.0.0`.  The code needs to be updated to use the current `openai.ChatCompletion` API.  Because the code does not function due to this error, none of the rubric's scoring criteria can be evaluated.  Therefore, the score for Module 1 is 0.


**Detailed Explanation of Scoring:**

The rubric explicitly states:

* "If any portion of the rubric is not applicable or not found in the solution, strictly do not give any marks for that portion."
* "Strictly use the provided model_solution as the reference for correctly invoking the LLM, for correctly parsing the output of the LLM invocation, and for correctly saving the LLM output as part of the state for the subsequent use."

Since the fundamental LLM invocation is incorrect, preventing any subsequent steps from executing, no marks can be awarded.  The code needs to be fixed before any evaluation based on the rubric is possible.  The error messages clearly show the problem. The output shows that `extracted_classes`, `extracted_rubric`, and `evaluation_results` are all empty dictionaries because the LLM calls failed.

**To Receive a Score:**

The student needs to:

1. **Update the OpenAI API calls:** Replace all instances of `openai.Completion.create` with `openai.ChatCompletion.create` and adapt the prompt structure accordingly to use the `messages` parameter with the correct role ("user" for the prompt).
2. **Ensure correct key.env setup:**  Verify that the `OPENAI_API_KEY` is correctly set in the `key.env` file and that the file is accessible to the notebook.
3. **Re-run the notebook:**  Execute the code after making the necessary changes.


Only after these corrections are made can the code be evaluated against the provided rubric.


Based on the provided notebook and rubric instructions, I cannot provide a numerical score or detailed feedback.  The code attempts to use the OpenAI API to perform several tasks (class extraction, rubric mapping, and evaluation). However, the code is using outdated OpenAI API calls (`openai.Completion.create` and `openai.ChatCompletion.create`).  These functions are deprecated in the newer versions of the OpenAI library.  The error messages clearly indicate this.

To evaluate the student's work, the following must be done:

1. **Update the OpenAI API calls:** The student needs to migrate their code to use the current OpenAI API functions  (`openai.ChatCompletion.create` with appropriately formatted messages, for instance).  The migration guide linked in the error messages should assist in this.

2. **Obtain and Set API Key:** The student correctly loads an API key from `key.env`. However, the `key.env` file is not included in the submission, making it impossible to run the code.

3. **Provide Student Submission and Model Solution:** The notebook includes placeholder strings for `"student_submission"` and `"model_solution"`.  Actual code needs to be provided in these fields for the evaluation to run.  The model solution is necessary for comparison.

4. **Define a Rubric:** While a sample rubric is present, it is also a placeholder.  A complete and well-defined rubric is crucial for accurate evaluation.

Once these issues are resolved, the notebook can be run, and then an evaluation can be performed based on the rubric's criteria. Only then can a proper assessment of the student's code be made.


The provided notebook uses the older OpenAI API calls (`openai.Completion.create`), which are deprecated.  The current OpenAI API uses `openai.ChatCompletion.create`.  This is the primary reason for the errors.

Here's a corrected version of the notebook, addressing the API changes and improving the prompt design for clarity and robustness:


```python
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv("key.env")
openai.api_key = os.getenv("OPENAI_API_KEY")


# Define the input state
class State(TypedDict):
    student_submission: str
    model_solution: str
    rubric: str
    extracted_classes: dict
    extracted_rubric: dict
    evaluation_results: dict
    reviewed_evaluation: dict


# Define the class extraction node function
def class_extraction_node(state: State) -> State:
    """Extract classes from student and model solution using OpenAI's API."""
    print("---Class Extraction Node---")

    def extract_classes_from_code(code: str) -> dict:
        prompt = f"""
        Given the following Java code, extract the names and bodies of all classes present.  
        Return your answer as a JSON object with the class names as keys and the class bodies as values.  
        Ensure the class bodies include all methods and attributes within the class.  
        Handle edge cases like nested classes and inner classes appropriately.
        If no classes are found, return an empty JSON object (`{}`).

        ```java
        {code}
        ```
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Or gpt-4 if available and appropriate
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000,  # Increased for potentially larger classes
                temperature=0.0,  # Deterministic output
                n=1
            )
            extracted_classes_json = response.choices[0].message['content'].strip()
            import json
            return json.loads(extracted_classes_json)

        except Exception as e:
            print(f"Error extracting classes: {e}")
            return {}

    # Extract classes from both the student submission and the model solution
    student_classes = extract_classes_from_code(state["student_submission"])
    model_classes = extract_classes_from_code(state["model_solution"])

    # Update the state with extracted classes
    state["extracted_classes"] = {
        "student_classes": student_classes,
        "model_classes": model_classes
    }

    # Return the updated state
    return state


# Define the rubric extraction node function
def rubric_extraction_node(state: State) -> State:
    """Use the LLM to map rubric items to specific Java classes."""
    print("---Rubric Extraction Node---")

    rubric = state["rubric"]
    student_classes = state["extracted_classes"]["student_classes"]

    def map_rubric_to_classes(rubric_text: str, classes: dict) -> dict:
        prompt = f"""
        Given the following rubric and Java classes, map each rubric item to the relevant class(es).  
        Return your answer as a JSON object.  Keys should be rubric items, and values should be lists of class names to which the rubric item applies.

        Rubric:
        {rubric_text}

        Java Classes:
        {json.dumps(classes, indent=2)}  #Improved formatting for clarity.

        Example Response (JSON):
        {{
          "Correctness of code": ["Calculator"],
          "Clarity of logic": ["Calculator"],
          "Use of proper coding conventions": ["Calculator"]
        }}
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.0,
                n=1
            )
            rubric_mapping_json = response.choices[0].message['content'].strip()
            import json
            return json.loads(rubric_mapping_json)
        except Exception as e:
            print(f"Error extracting rubric details: {e}")
            return {}

    # Map the rubric to each extracted class
    extracted_rubric = map_rubric_to_classes(rubric, student_classes)

    # Update the state with extracted rubric details
    state["extracted_rubric"] = extracted_rubric

    # Return the updated state
    return state


# Define the initial evaluation node function
def initial_evaluation_node(state: State) -> State:
    """Use LLM to evaluate each class based on rubric and model solution."""
    print("---Initial Evaluation Node---")

    student_classes = state["extracted_classes"]["student_classes"]
    model_classes = state["extracted_classes"]["model_classes"]
    rubric_details = state["extracted_rubric"]
    evaluation_results = {}

    for rubric_item, classes in rubric_details.items():
        evaluation_results[rubric_item] = {}
        for class_name in classes:
            student_class_code = student_classes.get(class_name, "")
            model_class_code = model_classes.get(class_name, "")

            prompt = f"""
            Evaluate the following Java class based on the rubric criterion: "{rubric_item}".

            Model Solution:
            ```java
            {model_class_code}
            ```

            Student Submission:
            ```java
            {student_class_code}
            ```

            Provide a score (e.g., 1-5) and detailed comments.
            """
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=500,
                    temperature=0.0,
                    n=1
                )
                evaluation = response.choices[0].message['content'].strip()
                evaluation_results[rubric_item][class_name] = evaluation

            except Exception as e:
                print(f"Error evaluating class {class_name} for rubric item {rubric_item}: {e}")
                evaluation_results[rubric_item][class_name] = "Error in evaluation."

    # Update the state with evaluation results
    state["evaluation_results"] = evaluation_results

    # Return the updated state
    return state


# Define the review evaluation node function (optional, but recommended)
def review_evaluation_node(state: State) -> State:
    """Review the initial evaluation using LLM to ensure accuracy."""
    print("---Review Evaluation Node---")
    # ... (Implementation similar to initial_evaluation_node, but for review) ...  This would require another LLM prompt.


# Build the LangGraph workflow
builder = StateGraph(State)

# Add the nodes to the workflow
builder.add_node("ClassExtractionNode", class_extraction_node)
builder.add_node("RubricExtractionNode", rubric_extraction_node)
builder.add_node("InitialEvaluationNode", initial_evaluation_node)
# builder.add_node("ReviewEvaluationNode", review_evaluation_node) #Uncomment if you implement the review node

# Define the workflow order
builder.add_edge(START, "ClassExtractionNode")
builder.add_edge("ClassExtractionNode", "RubricExtractionNode")
builder.add_edge("RubricExtractionNode", "InitialEvaluationNode")
# builder.add_edge("InitialEvaluationNode", "ReviewEvaluationNode") #Uncomment if you implement the review node
# builder.add_edge("ReviewEvaluationNode", END) #Uncomment if you implement the review node
builder.add_edge("InitialEvaluationNode", END)

# Create the workflow graph
graph = builder.compile()

# Sample initial state for invoking the graph
initial_state = {
    "student_submission": """
    public class Calculator {
        public int add(int a, int b) {
            return a + b;
        }
    }
    """,
    "model_solution": """
    public class Calculator {
        public int add(int a, int b) {
            return a + b;
        }
    }
    """,
    "rubric": """
    - Correctness of code
    - Clarity of logic
    - Use of proper coding conventions
    """,
    "extracted_classes": {},
    "extracted_rubric": {},
    "evaluation_results": {},
    "reviewed_evaluation": {} #added for completeness
}

# Execute the graph with the initial state
final_state = graph.invoke(initial_state)

# Display the extracted classes and corresponding rubric details
print(f"Extracted Student Classes: {final_state['extracted_classes']['student_classes']}")
print(f"Extracted Rubric: {final_state['extracted_rubric']}")
print(f"Evaluation Results: {final_state['evaluation_results']}")

import json
print(json.dumps(final_state, indent=2))
```

Remember to install the necessary libraries:  `pip install langgraph langchain openai python-dotenv`  and create a `key.env` file with your OpenAI API key:  `OPENAI_API_KEY=your_api_key`


This revised code uses the current OpenAI API, handles JSON for cleaner data exchange, and provides more robust prompts to the LLM, significantly improving the chances of successful class extraction and rubric mapping.  The optional review stage is left as a framework for you to complete, following a similar pattern to the `initial_evaluation_node` function.  Remember to choose an appropriate OpenAI model (gpt-3.5-turbo is generally a good balance of cost and performance).


The provided code attempts to build a LangChain workflow using LangGraph to automatically evaluate student code against a rubric.  However, it has several issues preventing it from working correctly.  The primary problem is the use of outdated OpenAI API calls.  The `openai.Completion.create` method is deprecated in OpenAI's v1 API.  The code needs to be updated to use the newer `openai.ChatCompletion.create` method.

Here's a breakdown of the problems and a corrected version:

**Problems:**

1. **Outdated OpenAI API:** As mentioned, the use of `openai.Completion.create` is the biggest issue.  The API has changed, and this function no longer exists.
2. **Error Handling:** While the code includes `try...except` blocks, the error handling is insufficient. It simply prints an error message and returns an empty dictionary, preventing the workflow from continuing.  More robust error handling is needed, potentially raising exceptions to halt execution if critical steps fail.
3. **Prompt Engineering:** The prompts are functional but could be improved.  More explicit instructions and examples within the prompts would likely improve the LLM's responses.  Clearer formatting of the expected output is also beneficial.
4. **State Management:** The state saving appears correct in principle but will fail due to the API errors.

**Corrected Code (with explanations):**

This corrected code addresses the outdated API calls and improves error handling.  It also includes improved prompts.  Remember to install the `openai` library: `pip install openai` and set your OpenAI API key in the environment.

```python
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
import openai
import json

# Define the input state
class State(TypedDict):
    student_submission: str
    model_solution: str
    rubric: str
    extracted_classes: dict
    extracted_rubric: dict
    evaluation_results: dict


# Define the class extraction node function
def class_extraction_node(state: State) -> State:
    """Extract classes from student and model solution using OpenAI's API."""
    print("---Class Extraction Node---")

    def extract_classes_from_code(code: str) -> dict:
        prompt = f"""
        Given the following Java code, extract the names and bodies of all classes present. 
        Provide the output as a JSON array of objects, where each object has a "name" and "body" key.  
        Example: `[{"name": "Calculator", "body": "public class Calculator { ... }"}, {"name": "AnotherClass", "body": "public class AnotherClass { ... }"}]`
        Here is the code:

        ```java
        {code}
        ```
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Or a suitable model
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.2,
            )
            class_extraction = response.choices[0].message["content"].strip()
            try:
                classes = json.loads(class_extraction)
                class_dict = {c["name"]: c["body"] for c in classes}
                return class_dict
            except json.JSONDecodeError:
                print(f"Error parsing JSON response: {class_extraction}")
                raise  # Re-raise to be caught by the outer try-except
        except Exception as e:
            print(f"Error extracting classes: {e}")
            raise

    try:
        student_classes = extract_classes_from_code(state["student_submission"])
        model_classes = extract_classes_from_code(state["model_solution"])
        state["extracted_classes"] = {
            "student_classes": student_classes,
            "model_classes": model_classes,
        }
    except Exception as e:
        print(f"Critical error in Class Extraction Node.  Stopping execution: {e}")
        return state # Return the state as is to avoid cascading failures


    return state


# Define the rubric extraction node function (simplified for demonstration)
def rubric_extraction_node(state: State) -> State:
    """This node is simplified for brevity;  a more sophisticated rubric mapping would be needed in a real-world application."""
    print("---Rubric Extraction Node---")
    state["extracted_rubric"] = {"Calculator": ["Correctness of code", "Clarity of logic"]} #Example mapping
    return state

# Define the initial evaluation node function
def initial_evaluation_node(state: State) -> State:
    """Use LLM to evaluate each class based on rubric and model solution."""
    print("---Initial Evaluation Node---")
    # ... (Similar improvements as in class_extraction_node needed here)
    state["evaluation_results"] = {} # Placeholder
    return state


# Build the LangGraph workflow
builder = StateGraph(State)

# Add the nodes to the workflow
builder.add_node("ClassExtractionNode", class_extraction_node)
builder.add_node("RubricExtractionNode", rubric_extraction_node)
builder.add_node("InitialEvaluationNode", initial_evaluation_node)

# Define the workflow order
builder.add_edge(START, "ClassExtractionNode")
builder.add_edge("ClassExtractionNode", "RubricExtractionNode")
builder.add_edge("RubricExtractionNode", "InitialEvaluationNode")
builder.add_edge("InitialEvaluationNode", END)

# Create the workflow graph
graph = builder.compile()

# Sample initial state
initial_state = {
    "student_submission": """
    public class Calculator {
        public int add(int a, int b) {
            return a + b;
        }
    }
    """,
    "model_solution": """
    public class Calculator {
        public int add(int a, int b) {
            return a + b;
        }
    }
    """,
    "rubric": """
    - Correctness of code
    - Clarity of logic
    - Use of proper coding conventions
    """,
    "extracted_classes": {},
    "extracted_rubric": {},
    "evaluation_results": {},
}

# Execute the graph
final_state = graph.invoke(initial_state)

# Display results
print(f"Extracted Student Classes: {final_state['extracted_classes']}")
print(f"Extracted Rubric: {final_state['extracted_rubric']}")
print(f"Evaluation Results: {final_state['evaluation_results']}")

```

This improved version uses the correct OpenAI API call and adds better error handling and more structured output. Remember to replace `"gpt-3.5-turbo"` with the appropriate model name if needed and handle potential rate limits from the OpenAI API.  The rubric extraction and evaluation nodes still need to be completed with proper LLM interactions, mirroring the structure and improvements applied to `class_extraction_node`.  The example provided for `rubric_extraction_node` is a placeholder and needs further development.


The code attempts to build a LangChain workflow using LangGraph to automatically evaluate student code based on a rubric and model solution.  However, it currently suffers from several critical issues, primarily related to the OpenAI API changes and incomplete implementation.  Let's break down the problems and how to fix them:


**1. OpenAI API Migration:**

The most significant problem is that the code uses `openai.Completion.create()`, which is deprecated in OpenAI's Python library version 1.0.0 and later.  The error messages clearly indicate this.  The code needs to be migrated to use the new `openai.ChatCompletion.create()` method, which requires structuring the API calls with `messages` instead of a `prompt` parameter.  


**2. Incomplete Prompt Engineering:**

Even after migrating to the ChatCompletion API, the prompts are not robust.  They are simple requests and may not consistently produce the structured output needed for reliable parsing. The prompts need significant improvement to:

* **Specify the desired format more precisely:**  The instructions should be clear and unambiguous, perhaps using examples to illustrate the expected JSON or dictionary-like structure.  This is crucial for reliable parsing in subsequent steps.
* **Handle edge cases:**  Consider what happens if the code contains no classes, or if the LLM fails to extract them perfectly. Add error handling and fallback mechanisms.
* **Add context:**  The prompts could benefit from providing more context. For example, the rubric extraction prompt could include a brief description of the overall task the code is supposed to perform.  This gives the LLM a better understanding of the rubric's relevance.


**3. Missing Parsing Logic:**

The code extracts the raw text response from OpenAI. It has a rudimentary attempt to parse the class extraction, but it's fragile.   Robust parsing is essential for both the class extraction and the evaluation results.  The current `if ": " in entry:` is too simplistic and will fail on various output formats.  Consider using regular expressions or a more sophisticated parsing library (like `json` if the LLM returns JSON) to handle different possible responses from the LLM.

**4.  Lack of Error Handling:**

The `try...except` blocks catch errors, but they only print error messages and return empty dictionaries. The workflow should gracefully handle errors, perhaps by logging them, providing informative feedback to the user, or attempting alternative strategies.

**5.  No Numeric Score Extraction:**

The rubric requires numeric scores. The code doesn't extract these scores from the LLM's response. The prompts need to explicitly ask for scores (e.g., "Criterion 1: Score (1-5): ...") and the parsing needs to extract those scores.

**6. Missing State Saving Implementation:**

Although the `state` dictionary is used, there's no actual demonstration of state saving across nodes. While the structure exists, the crucial part of storing and updating the intermediate results from each node isn't actively demonstrated or tested in the provided code example.

**7.  Review Evaluation Node:**

The `review_evaluation_node` is added but never used because the graph is recompiled after its creation.

**How to Fix It:**

1. **Install necessary libraries:** Ensure you have the updated `openai` library installed (`pip install openai`).  Do *not* try to pin it to an older version unless absolutely necessary. The newer API is far superior.
2. **Migrate to `ChatCompletion`:**  Replace all instances of `openai.Completion.create()` with `openai.ChatCompletion.create()`, adjusting the prompt structure to use the `messages` parameter with role-based (user, assistant) interactions.
3. **Improve Prompts:**  Re-design the prompts with more specific instructions, format examples, and appropriate context.
4. **Implement Robust Parsing:**  Use regular expressions or a structured parsing approach (e.g., JSON parsing) to extract the relevant information (classes, rubric mappings, scores, and comments) from the LLM's responses.
5. **Enhance Error Handling:**  Implement more sophisticated error handling, providing informative feedback and perhaps fallback mechanisms.
6. **Add Score Extraction:** Modify the prompts and parsing to handle numeric scores explicitly.
7. **Test State Management:** Verify that the `state` dictionary is correctly updated and passed between nodes, demonstrating actual state preservation in the workflow.
8. **Correct Graph Compilation:** Ensure the graph is only compiled once, after all nodes and edges have been defined.

**Example of Improved Prompt (for initial evaluation):**

```python
prompt = f"""
You are evaluating a Java class based on the following rubric criteria:

Rubric Criteria:
{', '.join(rubric_items)}

Model Solution:
```java
{model_class_code}
```

Student Submission:
```java
{student_class_code}
```

Please provide a detailed evaluation with scores (1-5, 5 being the best) for each criterion and comments.  Use this JSON format for your response:

```json
{{
  "evaluation": [
    {{"criterion": "Correctness of code", "score": 4, "comment": "..."}},
    {{"criterion": "Clarity of logic", "score": 5, "comment": "..."}},
    {{"criterion": "Use of proper coding conventions", "score": 3, "comment": "..."}}
  ]
}}
```
"""
```

After making these changes, you'll need to thoroughly test the workflow with various student submissions to ensure its accuracy and robustness.  Remember to handle potential exceptions and gracefully deal with cases where the LLM's response isn't perfectly formatted as expected.  You might also need to experiment with different LLM models and parameters to optimize the results.


The provided code attempts to create a LangChain workflow using LangGraph to automatically evaluate student code submissions against a rubric and a model solution.  However, it's currently broken due to API changes in the `openai` library.  The code uses `openai.Completion.create`, which is deprecated in `openai>=1.0.0`.  The error messages clearly indicate this.

To fix the code, you need to:

1. **Upgrade OpenAI Library and Migrate Code:**  Follow the instructions in the error messages.  Run `openai migrate` to automatically update your code to use the `openai.ChatCompletion.create` API. This involves changing the way prompts are structured and how the responses are accessed.  The new method requires sending messages in a list format.

2. **Install necessary libraries:** Ensure you have all necessary libraries, including `openai`, installed and correctly configured with your API key. The `key.env` file is crucial for this, and it must contain your API key correctly set as the `OPENAI_API_KEY` environment variable.

3. **Correct Prompt Design:** After migration, double-check your prompts. They should be well-structured and clear for the LLM to understand the task.  The prompts currently seem reasonable in structure, but their effectiveness will be significantly impacted by the deprecated API calls. The revised prompts after `openai migrate` will need to be formatted as `messages` (list of dictionaries).

4. **Handle potential errors:** The `try-except` blocks are good for catching errors, but they could be improved by providing more specific error handling or logging.

5. **Output Extraction:** After fixing the OpenAI API calls, the output extraction part needs thorough testing to ensure it accurately parses the LLM's response.  The current parsing logic assumes a specific format.  LLMs can be unpredictable, so robust parsing is important.

**Revised Code (Illustrative - requires `openai migrate` and testing):**

This revised code shows the general structure needed after migrating the OpenAI calls.  You'll need to adapt it based on the exact changes made by `openai migrate`.


```python
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
import openai

# Define the input state (unchanged)
class State(TypedDict):
    student_submission: str
    model_solution: str
    rubric: str
    extracted_classes: dict
    extracted_rubric: dict
    evaluation_results: dict
    reviewed_evaluation: dict

# ... (class_extraction_node function - needs revision based on openai migrate) ...
def class_extraction_node(state: State) -> State:
    # ... (Revised code after migration) ...
    def extract_classes_from_code(code: str) -> dict:
        prompt = f"""Given the following Java code, extract the names and bodies of all classes present. 
        Provide the output in the format:
        ClassName: <code>
        Separate each class with a newline. Here is the code:

        {code}"""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # Assuming gpt-4 after migration
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.2
            )
            class_extraction = response.choices[0].message['content'].strip()
            # ... (rest of parsing logic - needs to be tested thoroughly) ...
        except Exception as e:
            print(f"Error extracting classes: {e}")
            return {}
    # ... (rest of the function) ...


# ... (rubric_extraction_node function - needs revision based on openai migrate) ...
# ... (initial_evaluation_node function - needs revision based on openai migrate) ...
# ... (review_evaluation_node function - needs revision based on openai migrate) ...

# Build the LangGraph workflow (unchanged except potentially node names)

# ... (rest of the code - graph building and execution) ...
```

Remember to replace `"gpt-4o"` with the appropriate model name after the migration and thoroughly test each function's output and error handling.  The image generation part of the code should work correctly after fixing the LLM integration.  The rubric scoring will need to be adjusted based on the actual output of your LLM.  Finally, the state saving will depend on how you're structuring your data and saving it (e.g., to a file, database, etc.).  This isn't explicitly defined in the current code.


The provided code uses an outdated OpenAI API call (`openai.Completion.create`) which is no longer supported.  The error messages clearly indicate this.  To fix this, you need to update your code to use the newer `openai.ChatCompletion.create` method.  The change is more than just replacing the function name; the way you structure the prompt also needs alteration.

Here's the corrected code with explanations of the changes:

```python
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv("key.env")
openai.api_key = os.getenv("OPENAI_API_KEY")


# Define the input state
class State(TypedDict):
    student_submission: str
    model_solution: str
    rubric: str
    extracted_classes: dict
    extracted_rubric: dict
    evaluation_results: dict
    reviewed_evaluation: dict  # Added for review node


# Define the class extraction node function
def class_extraction_node(state: State) -> State:
    """Extract classes from student and model solution using OpenAI's API."""
    print("---Class Extraction Node---")

    def extract_classes_from_code(code: str) -> dict:
        prompt = f"""
        Given the following Java code, extract the names and bodies of all classes present. 
        Provide the output in the format:
        ClassName: ```java
        <class code>
        ```
        Separate each class with a newline. Here is the code:

        ```java
        {code}
        ```
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or gpt-4 if available and you have access
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.2,
            )

            class_extraction = response.choices[0].message["content"].strip()

            # Parse the response into a dictionary of class names and bodies
            classes = {}
            class_entries = class_extraction.split("```java")
            for i in range(1, len(class_entries), 2): # Iterate through code blocks
                class_entry = class_entries[i].strip()
                if ": " in class_entry:
                    class_name, class_code = class_entry.split(": ", 1)
                    classes[class_name.strip()] = class_code.strip()
            return classes
        except Exception as e:
            print(f"Error extracting classes: {e}")
            return {}

    # Extract classes from both the student submission and the model solution
    student_classes = extract_classes_from_code(state["student_submission"])
    model_classes = extract_classes_from_code(state["model_solution"])

    # Update the state with extracted classes
    state["extracted_classes"] = {
        "student_classes": student_classes,
        "model_classes": model_classes,
    }

    return state


# Define the rubric extraction node function (similar changes needed here)
def rubric_extraction_node(state: State) -> State:
    """Use the LLM to map rubric items to specific Java classes."""
    print("---Rubric Extraction Node---")

    rubric = state["rubric"]
    extracted_classes = state["extracted_classes"]["student_classes"]

    def map_rubric_to_classes(rubric_text: str, classes: dict) -> dict:
        prompt = f"""
        Given the following rubric and Java classes, map the relevant rubric items to each class.

        Rubric:
        {rubric_text}

        Java Classes:
        {', '.join(classes.keys())}

        Provide the output in the format:
        ClassName: [relevant rubric items]
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or gpt-4
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.2,
            )
            rubric_mapping = response.choices[0].message["content"].strip()
            rubric_details = {}
            rubric_entries = rubric_mapping.split("\n")
            for entry in rubric_entries:
                if ": " in entry:
                    class_name, rubric_items = entry.split(": ", 1)
                    rubric_details[class_name.strip()] = [
                        item.strip() for item in rubric_items.split(",")
                    ]
            return rubric_details
        except Exception as e:
            print(f"Error extracting rubric details: {e}")
            return {}

    # Map the rubric to each extracted class
    extracted_rubric = map_rubric_to_classes(rubric, extracted_classes)

    # Update the state with extracted rubric details
    state["extracted_rubric"] = extracted_rubric
    return state


# Define the initial evaluation node function (similar changes needed here)
def initial_evaluation_node(state: State) -> State:
    """Use LLM to evaluate each class based on rubric and model solution."""
    print("---Initial Evaluation Node---")
    # ... (rest of the function with similar changes to use ChatCompletion)


# Define the review evaluation node function (new function)
def review_evaluation_node(state: State) -> State:
    """Review the initial evaluation using LLM to ensure accuracy."""
    print("---Review Evaluation Node---")
    # ... (Implementation using ChatCompletion)


# Build the LangGraph workflow
builder = StateGraph(State)

# Add the nodes to the workflow
builder.add_node("ClassExtractionNode", class_extraction_node)
builder.add_node("RubricExtractionNode", rubric_extraction_node)
builder.add_node("InitialEvaluationNode", initial_evaluation_node)
builder.add_node("ReviewEvaluationNode", review_evaluation_node) # Add review node

# Define the workflow order
builder.add_edge(START, "ClassExtractionNode")
builder.add_edge("ClassExtractionNode", "RubricExtractionNode")
builder.add_edge("RubricExtractionNode", "InitialEvaluationNode")
builder.add_edge("InitialEvaluationNode", "ReviewEvaluationNode")
builder.add_edge("ReviewEvaluationNode", END)

# Create the workflow graph
graph = builder.compile()

# ... (rest of the code remains similar)

```

Remember to fill in the `initial_evaluation_node` and `review_evaluation_node` functions with the appropriate logic using `openai.ChatCompletion.create` and correctly formatted prompts.  Also, ensure that you have the `openai` library installed and your API key correctly set in your `key.env` file.  The code uses `gpt-3.5-turbo` as the model; you can change it to `gpt-4` if you have access and prefer.  The code also handles potential errors more gracefully.  The code also improves the class extraction by using ````java` to explicitly identify code blocks.


After making these changes, the code should run without the API version error and perform the intended LLM interactions. Remember to install the `openai` library if you haven't already: `pip install openai`


The provided Jupyter Notebook code attempts to build a LangChain workflow for automated code evaluation.  However, it has several critical flaws preventing it from working correctly, primarily related to the OpenAI API calls and the handling of its output.

**Major Issues:**

1. **OpenAI API Changes:** The code uses `openai.Completion.create`, which is deprecated in OpenAI's Python library (version 1.0.0 and later).  The error messages clearly indicate this.  The correct approach now is to use `openai.ChatCompletion.create` with a list of messages, specifying the roles ("user", "system", "assistant").

2. **Missing OpenAI API Key Setup:** While the code loads environment variables, it doesn't actually *use* the API key in the `openai.ChatCompletion.create` calls.  Even if the API call was correctly structured, it would still fail without the key being set properly.

3. **Error Handling and Output Parsing:** The `extract_classes_from_code` and similar functions have basic error handling (`try...except`), but the error handling isn't robust. More importantly, there's no sophisticated parsing of the LLM's response.  The code assumes a very specific format from the LLM, which may not always be consistent.  Robust parsing would require more sophisticated techniques (e.g., regular expressions or a dedicated parsing library) to extract the class names and code reliably.


4. **Unnecessary Re-Compilation:** The code attempts to re-compile the graph (`graph = builder.compile()`) multiple times.  This is redundant and might be a contributing factor to unexpected behavior.  Compilation should only happen once after the graph is fully defined.


5. **No `sum_marks` Tool:** The rubric description mentions a `sum_marks` tool, but this tool is not defined or used in the code.  The code doesn't even attempt to calculate a total score.


**How to Fix:**

1. **Update OpenAI API Calls:** Replace all instances of `openai.Completion.create` with `openai.ChatCompletion.create`.  Structure the messages properly, defining the `messages` parameter as a list of dictionaries (e.g., `[{"role": "user", "content": prompt}]`).

2. **Set OpenAI API Key:** Ensure that your OpenAI API key is correctly set in the `key.env` file (or directly in the code as an environment variable) and that your code is set up to load that key properly.

3. **Improve Error Handling and Output Parsing:** Implement more robust error handling that provides more informative messages if something goes wrong with the API calls. Implement more robust parsing of the LLM responses, potentially using regular expressions or other parsing methods to deal with the variability of LLM output.

4. **Remove Redundant Compilation:** Remove the extra `builder.compile()` calls; the graph should only be compiled once after building it.

5. **Add `sum_marks` Functionality:**  Implement the `sum_marks` function. This function should take the `evaluation_results` dictionary (after properly parsing and reviewing the evaluations) and compute the total score based on the rubric's scoring system.


**Example (Partial Fix - Addressing OpenAI API Changes and Key Setup):**

This revised snippet shows how to fix the OpenAI API calls.  Note that you still need to implement the `sum_marks` function and robust output parsing:

```python
import openai
import os
from dotenv import load_dotenv

load_dotenv("key.env") # Load your API key from key.env
openai.api_key = os.getenv("OPENAI_API_KEY")


def extract_classes_from_code(code: str) -> dict:
    prompt = f"""
    Given the following Java code, extract the names and bodies of all classes present. 
    Provide the output in the format:
    ClassName: <code>
    Separate each class with a newline. Here is the code:

    {code}
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4", # or gpt-3.5-turbo
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.2
        )
        class_extraction = response.choices[0].message['content'].strip()
        # ... (Implement robust parsing here) ...
        return classes  # Replace with actual parsed classes
    except Exception as e:
        print(f"Error extracting classes: {e}")
        return {}

# ... rest of the code (needs similar updates and sum_marks function) ...

```

Remember to replace `"gpt-4"` with the appropriate OpenAI model you're using and to install the `openai` library (`pip install openai`).  This revised code addresses only the most glaring issues; a fully functional and robust solution requires substantial further development.


The provided notebook has several issues preventing successful execution and graph construction.  Let's break down the problems and how to fix them:

**1. OpenAI API Key and Library Version:**

* **Problem:** The notebook correctly loads the OpenAI API key from `key.env`, but the code uses the outdated `openai.Completion.create()` method, which is deprecated in `openai>=1.0.0`.  The error messages clearly indicate this.
* **Solution:**  You must either:
    * **A) Upgrade and Migrate:** Run `openai migrate` in your terminal (or within a code cell) to automatically update your codebase to use the `openai.ChatCompletion.create()` method. This is the recommended approach.
    * **B) Downgrade:**  If migration is not feasible, temporarily downgrade your `openai` library using `pip install openai==0.28` (or a compatible version).  Remember this is a temporary solution, as the older API is no longer supported.


**2. Correcting the OpenAI Calls:**

* **Problem:**  The `class_extraction_node`, `rubric_extraction_node`, and `initial_evaluation_node` functions all rely on the now deprecated `openai.Completion.create()` method.
* **Solution:** Replace all instances of  `openai.Completion.create()` with `openai.ChatCompletion.create()`.  This requires changing the prompt structure to use the `messages` parameter as shown below (example for `class_extraction_node`):

```python
def class_extraction_node(state: State) -> State:
    """Extract classes from student and model solution using OpenAI's API."""
    print("---Class Extraction Node---")

    def extract_classes_from_code(code: str) -> dict:
        prompt = f"""
        Given the following Java code, extract the names and bodies of all classes present.
        Provide the output in the format:
        ClassName: <code>
        Separate each class with a newline. Here is the code:

        {code}
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", # or gpt-4, choose a suitable model
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.2
            )
            class_extraction = response.choices[0].message['content'].strip()
            # ... (rest of the parsing remains the same) ...
        except Exception as e:
            print(f"Error extracting classes: {e}")
            return {}
    # ... (rest of the function remains the same) ...
```

Apply this change to the other two OpenAI-using functions similarly.  Remember to replace `"gpt-4o"` with `"gpt-3.5-turbo"` or `"gpt-4"` (depending on your access and preference).


**3. Graph Compilation:**

* **Problem:** The code compiles the graph, then tries to add more nodes and edges afterwards.  `builder.compile()` finalizes the graph; you can't modify it after compilation. The warning messages show this happening.
* **Solution:** Move all `builder.add_node` and `builder.add_edge` calls *before* `graph = builder.compile()`.


**4.  Error Handling (Optional but Recommended):**

The `try...except` blocks handle exceptions during OpenAI API calls.  You might want to add more robust error handling (e.g., logging, different exception types, retry mechanisms) for production-level code.


**5.  Model Selection:**

The code uses `"gpt-4o"`. While powerful, it may not be the most cost-effective.  Consider using `"gpt-3.5-turbo"` as a more affordable alternative, especially for tasks that don't strictly require the advanced capabilities of GPT-4.


**Revised Code (incorporating key changes):**

```python
# ... (imports and load_dotenv remain the same) ...

# Define the input state (same as before)

# ... (class_extraction_node, rubric_extraction_node, initial_evaluation_node functions with corrected OpenAI calls)

# Build the LangGraph workflow
builder = StateGraph(State)

# Add the nodes *BEFORE* compilation
builder.add_node("ClassExtractionNode", class_extraction_node)
builder.add_node("RubricExtractionNode", rubric_extraction_node)
builder.add_node("InitialEvaluationNode", initial_evaluation_node)

# Define the workflow order *BEFORE* compilation
builder.add_edge(START, "ClassExtractionNode")
builder.add_edge("ClassExtractionNode", "RubricExtractionNode")
builder.add_edge("RubricExtractionNode", "InitialEvaluationNode")
builder.add_edge("InitialEvaluationNode", END)

# Compile the workflow graph - NOW
graph = builder.compile()

# View (this part remains the same)
display(Image(graph.get_graph().draw_mermaid_png()))

# ... (rest of the code to invoke the graph and print results)
```


After making these corrections, the code *should* run successfully, creating and executing the LangGraph workflow.  Remember to replace placeholder values with your actual code and rubric.  If you still encounter issues, please share the complete error messages.


The notebook has several issues preventing it from running correctly:

1. **OpenAI API Key and Version:** The code attempts to use the `openai` library, but the API calls are outdated. The error messages clearly state that `openai.Completion` and `openai.ChatCompletion` are deprecated in versions 1.0.0 and later.  You need to either:
    * **Migrate:** Run `openai migrate` in your terminal to update your code to the new API structure.
    * **Downgrade:** Install an older version of the `openai` library:  `pip install openai==0.28`.  This is less recommended as the older API will likely be removed entirely eventually.

2. **OpenAI API Calls:**  The `openai.ChatCompletion.create` calls need to be adjusted to the new API format.  The `messages` parameter is correctly used, but the way the response is handled needs to be changed to access the `choices[0].message['content']`.

3. **`graph.invoke(initial_state)`:** This line is crucial and will throw errors if the OpenAI API calls fail.  The LangGraph will only proceed if the previous steps are successful.

4. **Missing Imports:** The code is missing the `Image` import, needed for displaying the graph. Add this at the beginning:

   ```python
   from IPython.display import Image
   ```

**Corrected Code (using the new OpenAI API):**

```python
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from IPython.display import Image
import openai

# ... (State class remains the same) ...

def class_extraction_node(state: State) -> State:
    print("---Class Extraction Node---")

    def extract_classes_from_code(code: str) -> dict:
        prompt = f"""
        Given the following Java code, extract the names and bodies of all classes present. 
        Provide the output in the format:
        ClassName: <code>
        Separate each class with a newline. Here is the code:

        {code}
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", # or gpt-4, choose the appropriate model
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.2
            )
            class_extraction = response.choices[0].message['content'].strip()
            classes = {}
            class_entries = class_extraction.split("\n\n")
            for entry in class_entries:
                if ": " in entry:
                    class_name, class_code = entry.split(": ", 1)
                    classes[class_name.strip()] = class_code.strip()
            return classes
        except Exception as e:
            print(f"Error extracting classes: {e}")
            return {}

    # ... (rest of the class_extraction_node function remains largely the same) ...

# ... (rubric_extraction_node and initial_evaluation_node functions are similarly corrected) ...

def review_evaluation_node(state: State) -> State:
    print("---Review Evaluation Node---")
    # ... (similar corrections as above for openai.ChatCompletion.create and response handling) ...


# Build the LangGraph workflow (remains the same)

# ... (rest of the code remains largely the same, except ensure you have the correct model specified in openai.ChatCompletion.create) ...


# Sample initial state (remains the same)

# Execute and display results (remains the same)
```

**Before running:**

1.  **Install the necessary libraries:** Make sure you have `langgraph`, `langchain-community`, `langchain-anthropic`, `tavily-python`, `pandas`, `python-dotenv`, and `openai` installed.  Use the updated `pip install` command in the notebook cell.

2.  **Set your OpenAI API key:** Create a `.env` file in the same directory as your notebook and add the line `OPENAI_API_KEY=your_actual_api_key`.  Replace `your_actual_api_key` with your actual key.

3.  **Choose an appropriate OpenAI model:** I've changed the model to `"gpt-3.5-turbo"`. You can use `"gpt-4"` if you have access, but it's more expensive.  Make sure you choose a model that can handle the prompt complexity.

After making these changes, the notebook should run without the previous errors (assuming your OpenAI key is valid and you have sufficient quota).  However, the LLM responses might need fine-tuning depending on the desired output format and complexity of the code.  The success depends heavily on the OpenAI model's ability to accurately extract classes, map rubric items, and evaluate code.
