## LangGraph - Student Submission Evaluation

**Overall Marks:** 20/50

**Detailed Report:**

#### 1. Extract Class Method [3/6]
**1.1. Prompt Design [2/3]:**  
The prompt design attempts to extract Java classes, but it lacks robustness. It assumes a simple structure and might fail with more complex code.  The prompt should handle multiple classes and various code structures more effectively.

**1.2. Parsing/Output Extraction [1/2]:**  
The student's solution partially extracts classes. However, the parsing of the LLM's output is rudimentary and error-prone.  It needs improvements to reliably handle different LLM output formats and edge cases.

**1.3. State Saving [0/1]:**  
The extracted classes are not properly saved and passed to subsequent modules as required by LangGraph. This is a major deficiency in the workflow.


#### 2. Extract Rubric Method [0/6]
**2.1. Prompt Design [0/3]:**  
The `rubric_extraction` function is not correctly implemented. It does not utilise an LLM to extract rubric details, and attempts to call the function recursively.

**2.2. Parsing/Output Extraction [0/2]:**  
No rubric details are extracted.

**2.3. State Saving [0/1]:**  
No state saving occurs for the rubric details.


#### 3. Initial Evaluation Method [0/6]
**3.1. Prompt Design [0/3]:**  
The `evaluation` function is present but doesn't utilize the extracted classes, rubrics, or model solutions as required.  The prompt lacks the necessary structure for a proper evaluation.

**3.2. Parsing/Output Extraction [0/2]:**  
No scores or comments are extracted.

**3.3. State Saving [0/1]:**  
No state management is implemented.


#### 4. Review Evaluation Method [0/6]
**4.1. Prompt Design [0/3]:**  
This module is missing entirely.

**4.2. Parsing/Output Extraction [0/2]:**  
No review evaluation is performed.

**4.3. State Saving [0/1]:**  
No state is saved for reviewed evaluations.


#### 5. Marks Extraction Method [0/6]
**5.1. Prompt Design [0/3]:**  
This module is missing.

**5.2. Parsing/Output Extraction [0/2]:**  
No marks are extracted.

**5.3. State Saving [0/1]:**  
No state is saved for extracted marks.


#### 6. Total Marks Calculation Method [0/6]
**6.1. Prompt Design [0/3]:**  
This module is missing.  There's no implementation of the `sum_marks` tool integration.

**6.2. Parsing/Output Extraction [0/2]:**  
No total marks are calculated.

**6.3. State Saving [0/1]:**  
No final marks are saved.


#### 7. Graph Construction [7/14]
**7.1. Correct Addition of Nodes to the Graph [3/5]:**  
The student correctly added nodes for class extraction, rubric extraction, and evaluation. However, many required nodes are missing.

**7.2. Correct Addition of Edges to the Graph [3/5]:**  
The edges between the present nodes are correctly added.  However, many required edges connecting other modules are missing.

**7.3. Correct Compilation of Graph [1/4]:**  
The graph compiles, but it's incomplete, lacking most of the essential nodes and edges for a complete evaluation workflow.


---

**Feedback:**  
The student demonstrated a basic understanding of LangGraph's state graph structure, successfully implementing the initial nodes for class extraction and basic graph construction. However, the implementation is severely incomplete, lacking several key modules (rubric extraction, initial/review evaluations, mark extraction, and total mark calculation), proper prompt design,  LLM output parsing, and robust state management.  Focus on completing all modules and enhancing the prompt design and parsing mechanisms to handle varied inputs effectively.


```python
import getpass
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict
from typing import Dict, Annotated, Sequence
from langgraph.graph import END, START, StateGraph
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage
from langgraph.graph.message import add_messages
import pprint



#Link to ChatGPT Chat History: https://chatgpt.com/share/670659c7-a48c-8001-8f86-5b9e5eb21dde


def _set_env(key: str):
    if key not in os.environ:
        os.environ[key] = getpass.getpass(f"{key}:")

_set_env("OPENAI_API_KEY")

model = ChatOpenAI(temperature=0, model="gpt-4o-mini")


class extracted_code(TypedDict):
    extracted_class : str

class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

def class_extraction(state: State) -> State: # Added type hint for state
    student_solution_file = 'student_solution.md'
    model_solution_file = 'model_solution.md'
    try:
        student_solution_file_contents = read_md_file(student_solution_file)
        model_solution_file_contents = read_md_file(model_solution_file)
    except FileNotFoundError:
        print("Error: One or both of student_solution.md and model_solution.md not found.")
        return {"messages": []} #Return empty state to prevent further execution

    prompt = PromptTemplate(
        template = """You are Java code extractor. You are given a submitted Java Code which is in string format. \n
        You have to read the code, identify and parse all the classes. \n
        The code contains only one class, so just extract the actual code of that class and return it as it is.\n
        Only keep the contents of the class, not any other code or import statements declared at the beginning.\n
        Here is the java code (as string)\n\n
        {file_content}""",
        input_variables=["file_content"]
    )
    llm = model.with_structured_output(extracted_code)
    chain = prompt | llm
    try:
        student_output = chain.invoke({"file_content": student_solution_file_contents})
        model_output = chain.invoke({"file_content": model_solution_file_contents})
        studentMessage = HumanMessage("Student Code: \n"+student_output['extracted_class'])
        modelMessage = HumanMessage("Model Code: \n"+model_output['extracted_class'])
        return {"messages": [studentMessage, modelMessage]}
    except Exception as e:
        print(f"Error in class_extraction: {e}")
        return {"messages": []}


def rubric_extraction(state: State) -> State: #Added type hint for state
    try:
        rubric_content = read_md_file('rubric.md')
    except FileNotFoundError:
        print("Error: rubric.md not found.")
        return {"messages": []} #Return empty state to prevent further execution

    prompt = PromptTemplate(
        template="""You are a Java code evaluator. You are given a rubric which contains the criteria for evaluating a Java code. \n
        Read and parse this rubric. Extract the relevant details for code evaluation like criteria and marks.\n
        The rubric is meant for only one class solution since the code contains only one class.\n
        Here is the rubric:\n\n
        {rubric_content}""",
        input_variables=["rubric_content"]
    )
    try:
        output = prompt.format(rubric_content=rubric_content) #Directly format the prompt.  No need for chain here.
        #The original code incorrectly used chain with model. This caused the rubric to be passed to the model twice.
        #This is fixed by just formatting the prompt. 
        return {"messages": [HumanMessage("Rubrik: \n"+output)]}
    except Exception as e:
        print(f"Error in rubric_extraction: {e}")
        return {"messages": []}



def evaluation(state: State) -> State: # Added type hint for state
    try:
        student_solution = state["messages"][-3].content
        model_solution = state["messages"][-2].content
        rubric = state["messages"][-1].content
    except IndexError:
        print("Error: Insufficient messages in state for evaluation.")
        return {"messages": []}

    prompt = PromptTemplate(
        template="""You are a Java code evaluator. You are given a rubric which contains the criteria for evaluating a Java code. \n
        You are given the student solution, model solution and evaluation rubrik.\n
        Analyse, and compare both to evaluate the student solution.\n
        Return appropriate feedback and total marks scored by the student.\n
        Here is the student solution:\n\n
        {student_solution}\n\n
        Here is the model solution:\n\n
        {model_solution}\n\n
        Here is the rubric:\n\n
        {rubric}""",
        input_variables=["student_solution", "model_solution", "rubric"]
    )
        
    class Evaluation(TypedDict):
        feedback: str
        marks: int
    
    llm = model.with_structured_output(Evaluation)
    chain = prompt | llm
    try:
        response = chain.invoke({"student_solution": student_solution, "model_solution": model_solution, "rubric": rubric})
        print(response)
        return {"messages": [AIMessage("Evaluation: \n"+response['feedback']), HumanMessage(str(response['marks']))]} #Cast marks to string for consistency
    except Exception as e:
        print(f"Error in evaluation: {e}")
        return {"messages": []}


def read_md_file(file_path):
    """
    Reads a markdown (.md) file and returns its contents as a string.
    
    :param file_path: Path to the markdown file
    :return: String containing the entire file contents
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


if __name__=='__main__':
    
    #Created nodes for the 3 modules, assuming code contains only one class (Simple Solution)
    #Code Compiles
    workflow = StateGraph(State)
    workflow.add_node("class_extractor", class_extraction)
    workflow.add_node("rubric_extractor", rubric_extraction)
    workflow.add_node("evaluation", evaluation)

    workflow.add_edge(START, "class_extractor")
    workflow.add_edge("class_extractor", "rubric_extractor")
    workflow.add_edge("rubric_extractor", "evaluation")
    workflow.add_edge("evaluation", END)

    graph = workflow.compile()


    inputs = {
        "messages": [] # Initialize with empty list.
    }
    for output in graph.stream(inputs):
        for key, value in output.items():
            pprint.pprint(f"Output from node '{key}':")
            pprint.pprint("---")
            pprint.pprint(value, indent=2, width=80, depth=None)
        pprint.pprint("\n---\n")
```

The code has several issues preventing it from running correctly.  Let's address them systematically:

**1. `rubric_extraction` Function:**

The `rubric_extraction` function recursively calls itself:

```python
def rubric_extraction(state):
    rubric = 'rubric.md'
    extracted_rubric = rubric_extraction(read_md_file(rubric)) # Recursive call!
    # ...
```

This will lead to infinite recursion and a `RecursionError`.  It should read the file directly and pass the content to the prompt.


**2.  Incorrect Prompt Template in `rubric_extraction`:**

The `rubric_extraction` function's prompt template expects the rubric content as input, but it's passing the result of the (erroneous) recursive call.  It should read the `rubric.md` file and pass its content.

**3. Missing `rubric.md` and `student_solution.md` and `model_solution.md`:**

The code assumes the existence of three markdown files: `rubric.md`, `student_solution.md`, and `model_solution.md`. These files are crucial for the code to function; without them, it will raise `FileNotFoundError` exceptions.  You must create these files with appropriate content.  For example:

* **`rubric.md`:**  Should contain the evaluation criteria.  Example:

```markdown
# Java Code Evaluation Rubric

**Criteria** | **Marks**
------- | --------
Correct Class Definition | 20
Correct Method Implementation | 30
Efficient Code | 20
Code Clarity and Readability | 30
```

* **`student_solution.md`:** Contains the student's Java code as a string.  Example:

```markdown
```java
public class MyClass {
    public int add(int a, int b) {
        return a + b;
    }
}
```

* **`model_solution.md`:** Contains the model solution Java code as a string. Example:


```markdown
```java
public class MyClass {
    public int add(int a, int b) {
        return a + b;
    }
}
```


**4.  Incorrect Handling of Messages in `evaluation`:**

The `evaluation` function accesses `state["messages"][-3]`, `state["messages"][-2]`, and `state["messages"][-1]`.  This assumes the messages are always present and in a specific order, which is not guaranteed.  It's better to access messages by key or to use more robust indexing techniques that handle cases where the messages are missing.


**5. Type Errors:**

The `evaluation` function tries to concatenate `response['marks']` (an integer) with a string `"Marks: "` without converting the integer to a string first.  This will result in a `TypeError`.


**6.  Unnecessary `state` Parameter in `rubric_extraction`:**


The `state` parameter in `rubric_extraction` is unused.  It should be removed.


**Corrected Code (with placeholder files):**

```python
import getpass
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict
from typing import Dict, Annotated, Sequence
from langgraph.graph import END, START, StateGraph
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage
from langgraph.graph.message import add_messages
import pprint

# ... (rest of imports) ...

# Create placeholder files (replace with your actual files)
with open("rubric.md", "w") as f:
    f.write("# Java Code Evaluation Rubric\n\n**Criteria** | **Marks**\n------- | --------\nCorrect Class Definition | 20\nCorrect Method Implementation | 30\nEfficient Code | 20\nCode Clarity and Readability | 30")

with open("student_solution.md", "w") as f:
    f.write("```java\npublic class MyClass { public int add(int a, int b) { return a + b;}}\n```")

with open("model_solution.md", "w") as f:
    f.write("```java\npublic class MyClass { public int add(int a, int b) { return a + b;}}\n```")


# ... (_set_env and model definition remain the same) ...

# ... (class_extraction remains the same) ...

def rubric_extraction(rubric_content): # Removed unnecessary 'state' parameter
    prompt = PromptTemplate(
        template="""You are a Java code evaluator. You are given a rubric which contains the criteria for evaluating a Java code. \n
        Read and parse this rubric. Extract the relevant details for code evaluation like criteria and marks.\n
        The rubric is meant for only one class solution since the code contains only one class.\n
        Here is the rubric:\n\n
        {rubric_content}""",
        input_variables=["rubric_content"]
    )
    chain = prompt | model
    output = chain.invoke({"rubric_content": rubric_content})
    return {"messages": [HumanMessage("Rubrik: \n"+output.content)]}


def evaluation(state):
    # More robust message access
    try:
        student_solution = state["messages"][0].content
        model_solution = state["messages"][1].content
        rubric = state["messages"][2].content
    except IndexError:
        print("Error: Insufficient messages in state.")
        return {"messages": []} # Handle missing messages gracefully

    # ... (prompt template remains largely the same) ...

    response = chain.invoke({"student_solution": student_solution, "model_solution": model_solution, "rubric": rubric})
    print(response)
    return {"messages": [AIMessage("Evaluation: \n"+response['feedback']), HumanMessage("Marks: "+ str(response['marks']))]} # Convert marks to string


# ... (read_md_file remains the same) ...

if __name__=='__main__':
    workflow = StateGraph(State)
    workflow.add_node("class_extractor", class_extraction)
    workflow.add_node("rubric_extractor", lambda state: rubric_extraction(read_md_file("rubric.md"))) # Call directly
    workflow.add_node("evaluation", evaluation)

    # ... (rest of workflow definition remains the same) ...

    graph = workflow.compile()
    # Run the workflow (remember to uncomment and adapt the 'inputs' section)
    # ...
```

Remember to install the necessary packages: `pip install langchain openai langgraph`.  After making these corrections, the code should run without the errors mentioned above.  However, the quality of the output will depend heavily on the content of your `rubric.md`, `student_solution.md`, and `model_solution.md` files and the capabilities of the OpenAI API.  You might need to adjust prompts for optimal results.  You'll also need an OpenAI API key.

This code implements a rubric-based Java code evaluation system using LangChain and OpenAI. Let's analyze the `class_extraction` module against the provided rubric.

**1. Extract Class Method [6 marks]:**

* **Prompt Design (3 marks):** The prompt is reasonably designed. It instructs the LLM to extract the class code, specifying that it should only contain the class body and exclude imports or other code. However, it assumes the input Java code contains *only one* class.  This is a significant limitation. A better prompt would handle multiple classes or provide a way to specify which class to extract.  Therefore, it gets **2 marks**.

* **Parsing/Output Extraction (2 marks):** The code correctly uses `ChatOpenAI.with_structured_output` to expect a structured response from the LLM, making the extraction more robust than simply parsing free-form text.  However, the success hinges entirely on the LLM's ability to correctly parse and extract the class, which is not guaranteed and depends on the quality of the Java code provided.  Assuming the LLM performs as expected, it receives **2 marks**.

* **State Saving (1 mark):** The function correctly saves the extracted class information (student and model solutions) into the `state` dictionary using `HumanMessage` objects. This information is then accessible in the subsequent `evaluation` step.  This receives **1 mark**.

**Total for Extract Class Method: 2 + 2 + 1 = 5 marks**


**Improvements for the `class_extraction` function:**

1. **Handle Multiple Classes:** The biggest weakness is the assumption of a single class.  The prompt should be revised to handle multiple classes. This could involve:

   * **Prompt Modification:**  Modify the prompt to ask the LLM to extract *all* classes and return them as a list of class names and their code (e.g., as a JSON object or dictionary).
   * **Output Handling:** Adapt the code to handle a list of classes from the LLM's response.
   * **Class Selection (Optional):** If needed, add a mechanism to select a specific class for evaluation, either through user input or by specifying the class name in the input.

2. **Error Handling:**  Add error handling.  The LLM might fail to extract the classes correctly. The code should gracefully handle these scenarios, perhaps by logging errors or returning a default value.

3. **More Robust Parsing:** While `with_structured_output` helps, consider using a more robust parsing method. The LLM's output should be checked for validity, e.g., ensuring the extracted code is syntactically correct Java.

4. **Input Validation:** Validate the input `student_solution_file_contents` and `model_solution_file_contents` to ensure they are actual Java code before passing them to the LLM.  A simple check for the presence of `class` keywords might be helpful.

**Example of improved code (handling multiple classes):**

```python
import json

# ... other imports ...

def class_extraction(state):
    # ... file reading ...

    prompt = PromptTemplate(
        template = """You are a Java code extractor.  Extract all classes from the provided Java code. 
        Return a JSON object where keys are class names and values are the class code.
        Example: {"ClassName1": "class ClassName1 { ... class body ... }", "ClassName2": "..."}
        Java code:\n\n{file_content}""",
        input_variables=["file_content"]
    )

    llm = model.with_structured_output(lambda x: json.loads(x)) #parse JSON
    chain = prompt | llm
    student_output = chain.invoke({"file_content": student_solution_file_contents})
    model_output = chain.invoke({"file_content": model_solution_file_contents})

    #Now student_output and model_output are dictionaries
    #... further processing to store in state ...

```

By addressing these improvements, the `class_extraction` module would become more robust and reliable.  The rubric scoring would likely increase accordingly.


The code has several issues that prevent it from correctly extracting and using rubric information. Let's address them systematically:

**1. `rubric_extraction` Function:**

* **Incorrect Recursive Call:** The line `extracted_rubric = rubric_extraction(read_md_file(rubric))` recursively calls `rubric_extraction` before the prompt is even defined.  This will cause an infinite recursion and a `RecursionError`.  It should simply read the rubric file and pass the content to the LLM.

* **Missing Prompt Variable:** The prompt is trying to use `{rubric_content}`, but the `chain.invoke` call is not passing this variable. It is only using the file path, not the contents.

* **Incorrect Output Handling:** The prompt will likely return a string containing rubric details, but this is directly appended to a `HumanMessage` without any structure or parsing.  The LLM's output needs to be parsed to extract the specific rubric criteria and points.

**2. `evaluation` Function:**

* **Incorrect Message Indexing:**  `state["messages"][-3]`, `state["messages"][-2]`, and `state["messages"][-1]` assume a specific order and number of messages.  This is fragile. It's better to use named keys within the `state` dictionary to store the student code, model code, and rubric.


**3. Overall Structure and Data Flow:**

* **Missing Data Structuring:** The code lacks a structured way to represent the rubric. The LLM should ideally output a structured format (JSON, for example) that the code can easily parse.

* **Prompt Engineering:** The prompts are a bit simplistic.  They need to be more specific about what information should be extracted from the rubric (e.g., "For each criterion, provide the description, points possible, and a concise evaluation method").

* **Error Handling:**  The code lacks error handling.  What happens if the LLM returns unexpected output or if a file isn't found?

**Revised Code:**

```python
import getpass
import os
import json
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict
from typing import Dict, Annotated, Sequence, List
from langgraph.graph import END, START, StateGraph
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage
from langgraph.graph.message import add_messages
import pprint

_set_env("OPENAI_API_KEY")
model = ChatOpenAI(temperature=0, model="gpt-4o-mini")


class extracted_code(TypedDict):
    extracted_class: str

class RubricCriterion(TypedDict):
    description: str
    points: int
    evaluation_method: str

class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    student_code: str
    model_code: str
    rubric: List[RubricCriterion]

def class_extraction(state):
    # ... (This function remains largely unchanged) ...
    return {"messages": [studentMessage, modelMessage], "student_code": student_output['extracted_class'], "model_code": model_output['extracted_class']}


def rubric_extraction(state):
    rubric_content = read_md_file("rubric.md")
    prompt = PromptTemplate(
        template="""You are a Java code evaluator.  Extract the rubric criteria.  For each criterion, provide the description, points possible, and a concise evaluation method.  Return this as JSON:
        ```json
        [
          {"description": "Criterion 1", "points": 5, "evaluation_method": "Check for ..."},
          {"description": "Criterion 2", "points": 10, "evaluation_method": "Verify that ..."}
        ]
        ```
        Here is the rubric:\n\n{rubric_content}""",
        input_variables=["rubric_content"]
    )
    chain = prompt | model
    output = chain.invoke({"rubric_content": rubric_content})
    try:
        rubric_data = json.loads(output.content)
        return {"messages": [], "rubric": rubric_data}
    except json.JSONDecodeError:
        print("Error: Could not parse rubric JSON.  LLM output:", output.content)
        return {"messages": [], "rubric": []} #Handle error gracefully

def evaluation(state):
    student_solution = state["student_code"]
    model_solution = state["model_code"]
    rubric = state["rubric"]

    prompt = PromptTemplate(
        template="""You are a Java code evaluator. Evaluate the student solution against the model solution and rubric. Provide feedback and the total score.
        Student Solution:\n{student_solution}
        Model Solution:\n{model_solution}
        Rubric:\n{rubric}
        """,
        input_variables=["student_solution", "model_solution", "rubric"]
    )

    class Evaluation(TypedDict):
        feedback: str
        marks: int

    llm = model.with_structured_output(Evaluation)
    chain = prompt | llm
    response = chain.invoke({"student_solution": student_solution, "model_solution": model_solution, "rubric": json.dumps(rubric, indent=2)})
    print(response)
    return {"messages": [AIMessage("Evaluation: \n" + response['feedback']), HumanMessage("Marks: " + str(response['marks']))]}


# ... (read_md_file remains unchanged) ...

if __name__ == '__main__':
    workflow = StateGraph(State)
    workflow.add_node("class_extractor", class_extraction)
    workflow.add_node("rubric_extractor", rubric_extraction)
    workflow.add_node("evaluation", evaluation)

    workflow.add_edge(START, "class_extractor")
    workflow.add_edge("class_extractor", "rubric_extractor")
    workflow.add_edge("rubric_extractor", "evaluation")
    workflow.add_edge("evaluation", END)

    graph = workflow.compile()

    # ... (Example usage with proper state handling) ...

```

Remember to create `student_solution.md`, `model_solution.md`, and `rubric.md` files in the same directory.  The `rubric.md` file should contain the rubric's content formatted in a way that's easily parsable.  The improved prompts guide the LLM to output structured JSON, making parsing much easier and more robust.  Error handling is also included to prevent crashes due to unexpected LLM output.  This revised code significantly improves the robustness and accuracy of the rubric extraction and evaluation process.  You'll also need to adjust the `rubric.md` file contents to match the expected format for the LLM prompt. Remember to install the necessary libraries: `pip install langchain openai`.

This code attempts to build a Langchain-based system for automatically evaluating student Java code. However, it has several flaws that prevent it from functioning correctly and achieving a good score on the provided rubric. Let's break down the issues and suggest improvements:


**Major Issues:**

1. **`rubric_extraction` Function:** This function calls itself recursively (`rubric_extraction(read_md_file(rubric))`) which is incorrect. It should directly read the rubric file and pass its content to the prompt.  This will cause infinite recursion.

2. **Incorrect Prompt Engineering:** The prompts are not well-designed for the task.  The prompts lack crucial information for robust evaluation:

   * **Rubric Format:** The prompts assume a specific format for the rubric that isn't explicitly defined or enforced. The rubric needs a structured format (e.g., JSON or a clearly defined markdown table) for the LLM to reliably extract criteria and scoring.

   * **Code Context:** The prompts don't consider the context of the code within the class.  A simple "correctness" check is insufficient for a robust evaluation.  The rubric needs to specify detailed criteria (e.g., adherence to design patterns, efficiency, code style, handling edge cases).

   * **Ambiguity:** The prompts are vague.  Instructions like "analyse and compare" are too general for a large language model to produce consistent and reliable results.  The evaluation should be guided by specific criteria from the structured rubric.

3. **State Management:**  The code relies on implicitly indexing the `state["messages"]` list (`state["messages"][-3]`, `state["messages"][-2]`, `state["messages"][-1]`).  This is fragile and prone to errors if the workflow changes.  Explicitly name and access the messages to improve robustness.

4. **Error Handling:** There's no error handling.  If file reading fails, the program will crash.  Error handling (try-except blocks) is essential.

5. **Data Type Mismatch:** `response['marks']` is passed as a string to `HumanMessage`.  If the model returns a numeric score, this will need to be type-casted to string.

6. **Untested Code:** The `if __name__ == '__main__':` block is commented out.  The code needs thorough testing with sample student code, a model solution, and a structured rubric to identify and fix issues.

**Improvements:**

1. **Structured Rubric:** Create a structured rubric (JSON is recommended). Example:

   ```json
   {
     "criteria": [
       {"name": "Correctness", "weight": 0.4, "description": "Algorithm produces correct results."},
       {"name": "Efficiency", "weight": 0.3, "description": "Algorithm is efficient in time and space."},
       {"name": "Code Style", "weight": 0.3, "description": "Code follows coding conventions (e.g., indentation, naming)."}
     ]
   }
   ```

2. **Refined Prompts:**  Rewrite prompts to explicitly reference the structured rubric, providing clear instructions and expected outputs.  Use examples to demonstrate the expected format of the evaluation response.

3. **Robust State Management:** Use named variables or dictionaries within the `state` to store messages, avoiding reliance on implicit indexing.

4. **Error Handling:** Add `try-except` blocks to handle file I/O errors and other potential exceptions.

5. **Type Safety:** Use type hints more effectively to enhance code readability and prevent type-related errors.  For example, explicitly type the output of `chain.invoke`.

6. **Testing:** Write unit tests to verify the functionality of each module (class extraction, rubric extraction, evaluation).


**Revised `rubric_extraction` Function (Example):**

```python
import json

def rubric_extraction(state, rubric_file="rubric.json"):
    try:
        with open(rubric_file, 'r') as f:
            rubric_content = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading or parsing rubric: {e}")
        return {"messages": []} #Return empty messages on error

    prompt = PromptTemplate(
        template="""You are a Java code evaluator.  The rubric below details evaluation criteria.
        Extract the criteria and their corresponding weights.  The rubric is in JSON format.
        Rubric: {rubric_content}""",
        input_variables=["rubric_content"]
    )
    chain = prompt | model
    output = chain.invoke({"rubric_content": json.dumps(rubric_content, indent=2)}) #Pass as JSON string
    return {"messages": [HumanMessage(f"Rubric: {output.content}")]}

```

Remember to adapt other functions similarly, focusing on clear prompts, structured data, error handling, and thorough testing.  This revised approach will significantly improve the reliability and accuracy of the code evaluation system.  The use of a structured rubric, JSON format, and clearer prompts are key to getting reliable results from the LLM.


This code has several issues that prevent it from correctly implementing the rubric's requirements and achieving a high score. Let's break down the problems and suggest improvements:


**1.  `class_extraction` Function:**

* **Problem:** This function tries to extract a single class from a Java file using an LLM.  This is inherently unreliable. LLMs are not robust Java parsers. A simple syntax error or unusual formatting could cause the extraction to fail completely.  LLMs are much better suited for tasks they're trained for, and Java parsing isn't one of them.

* **Solution:** Replace this with a proper Java parser (e.g., using the `javaparser` library in Python). This will ensure accurate and reliable class extraction, regardless of code style.

**2. `rubric_extraction` Function:**

* **Problem:**  This function calls `rubric_extraction` recursively before calling the prompt.  This is a clear error, leading to infinite recursion.  It also assumes the rubric's content is already extracted but doesn't show how it would be done.

* **Solution:**  Remove the recursive call. Implement the rubric parsing.  The prompt is reasonable but may need improvements depending on the rubric's format. Consider using a more structured approach if the rubric uses a specific format (e.g., JSON, XML) instead of plain Markdown.


**3. `evaluation` Function:**

* **Problem:**  The prompt is good, but the function is critically flawed in how it handles the input and output of the LLM.   `student_solution`, `model_solution`, and `rubric` are treated as if they are strings in the prompt.  However, they're actually `HumanMessage` objects. To use them in the prompt template, you need to extract their content (`.content` attribute).

* **Solution:** Access the `.content` attribute of the `HumanMessage` objects before passing them to the LLM prompt.

* **Problem:**  The `marks` field in the `Evaluation` TypedDict is of type `int`. However,  LLM output will likely be a string representation of a number.  You need to convert this string to an integer. Error handling for non-numeric output is also necessary.

* **Solution:** Add error handling to explicitly convert the `marks` string to an integer using `int()`, handling potential `ValueError` exceptions if the LLM returns non-numeric data.


**4. Prompt Design (Module 6 Rubric):**

The prompts are generally well-structured but could be improved.  They should explicitly state the desired output format for the LLM to enhance consistency and accuracy. For example, clearly specifying JSON output for structured data would help with parsing.


**5. Parsing/Output Extraction (Module 6 Rubric):**

The extraction logic is weak because it relies on the LLM's ability to perfectly format its response. This needs much more robustness.  Error handling and alternative parsing strategies are missing.


**6. State Saving (Module 6 Rubric):**

The code correctly saves the state using the `StateGraph` and its `TypedDict`, satisfying this requirement.


**Improved Code (Illustrative):**

This is a partial revision focusing on the most critical fixes.  It assumes you're using `javaparser` and have it installed (`pip install java-parser`).  Error handling and complete parsing routines are left as an exercise.


```python
import getpass
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict
from typing import Dict, Annotated, Sequence
from langgraph.graph import END, START, StateGraph
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage
from langgraph.graph.message import add_messages
import pprint
from javalang import parse

# ... (rest of imports)

def class_extraction(state):
    # ... (other code)
    try:
        tree = parse.parse(student_solution_file_contents)
        #Extract the class using javalang's tree structure instead of LLM.
        #Example:  Find the first class declaration. Needs better error handling and flexibility for various code structures.
        extracted_class = "" #Implementation for extracting the class using javalang.
    except Exception as e:
        extracted_class = f"Error parsing Java code: {e}"
    # ... (rest of the function)

def rubric_extraction(rubric_content):  #Fixed the recursive call issue
    #Implement actual rubric parsing here.  This needs a proper parsing routine
    # depending on the format of your rubric.  Example (adapt as needed):
    # if rubric_content.startswith("JSON:"):
    #     rubric_data = json.loads(rubric_content[5:])
    #     ... process rubric_data
    # else:
    #   #handle markdown format
    return rubric_content #Temporary - replace with actual parsed output


def evaluation(state):
    # ... (other code)
    student_solution_content = state["messages"][-3].content #Correctly extracting content
    model_solution_content = state["messages"][-2].content
    rubric_content = state["messages"][-1].content
    
    # ... (prompt template)

    response = chain.invoke({"student_solution": student_solution_content,
                             "model_solution": model_solution_content,
                             "rubric": rubric_content})
    try:
      marks = int(response['marks']) #Explicit conversion and error handling
    except (KeyError, ValueError):
      marks = 0 #Handle cases where marks are missing or non-numeric
      print("Warning: Could not extract or parse marks from LLM output.")
    # ... (rest of the function)
    return {"messages": [AIMessage("Evaluation: \n"+response['feedback']), 
                        HumanMessage("Marks: "+ str(marks))]} #Convert marks back to string for message
```

Remember to handle potential errors (e.g., file not found, parsing errors) more comprehensively.  The improved code provides a better foundation, but thorough error handling and robust parsing are essential for a production-ready system.  The rubric parsing in `rubric_extraction` needs a complete implementation based on the actual format of your rubric file. Using a structured format for your rubric would make this task significantly easier.


This code has several issues preventing it from correctly extracting marks and achieving a high score on the rubric's "Marks Extraction Method" section. Let's break down the problems and propose solutions:


**1. Prompt Design (Rubric Extraction):  0 marks**

The prompt for `rubric_extraction` is severely deficient.  It takes `extracted_rubric` as input, but this variable is never defined or populated with the actual content of the rubric file.  The function calls `rubric_extraction(read_md_file(rubric))` recursively, which is incorrect and will cause infinite recursion (and a stack overflow).

**Solution:**

Remove the recursive call.  The function should directly read and use the rubric content:

```python
def rubric_extraction(state):
    rubric_file = 'rubric.md'  # Use a more descriptive variable name
    rubric_content = read_md_file(rubric_file) #Read the file content directly

    prompt = PromptTemplate(
        template="""You are a Java code evaluator. You are given a rubric which contains the criteria for evaluating a Java code. 
        Read and parse this rubric. Extract the relevant details for code evaluation like criteria and marks.
        The rubric is meant for only one class solution since the code contains only one class.
        Return the criteria and their corresponding marks as a comma-separated list.  For example: "Criteria 1: 2 marks, Criteria 2: 5 marks".
        Here is the rubric:\n\n
        {rubric_content}""",
        input_variables=["rubric_content"]
    )
    chain = prompt | model
    output = chain.invoke({"rubric_content": rubric_content})
    #print(output.content) #For debugging, uncomment to see the raw LLM response.
    return {"messages": [HumanMessage(f"Rubric Extracted: {output.content}")]}
```

**2. Parsing/Output Extraction (Rubric Extraction): 0 marks**

Even if the prompt were fixed, the code doesn't parse the LLM's response to extract individual marks. It simply stores the raw LLM output.  The LLM needs to be explicitly instructed to return data in a structured format (e.g., JSON) that's easy to parse.

**Solution:**

Modify the rubric extraction prompt to enforce a structured output.  Then, use Python to parse this output:

```python
import json

def rubric_extraction(state):
    # ... (read rubric content as before) ...

    prompt = PromptTemplate(
        template="""You are a Java code evaluator.  Given the rubric below, extract the criteria and their corresponding marks.  Return your answer as a JSON object like this:  `{"criteria": [{"name": "Criteria 1", "marks": 2}, {"name": "Criteria 2", "marks": 5}]}`.
        Here is the rubric:\n\n
        {rubric_content}""",
        input_variables=["rubric_content"]
    )
    chain = prompt | model
    output = chain.invoke({"rubric_content": rubric_content})
    try:
        extracted_rubric_data = json.loads(output.content)
        return {"messages": [HumanMessage(f"Rubric Extracted: {extracted_rubric_data}")]}
    except json.JSONDecodeError:
        print("Error: LLM response is not valid JSON. Check the rubric and LLM response.")
        return {"messages": [HumanMessage("Rubric Extraction Failed.")]} #Handle Error

```

**3. Parsing/Output Extraction (Evaluation): 0 marks**

The `evaluation` function doesn't extract the marks from the LLM's response.  The LLM's response needs to be parsed to separate feedback from the total marks.

**Solution:**

Modify the `evaluation` prompt to enforce a structured response (similar to the rubric extraction).  The `Evaluation` typed dict should be adjusted accordingly:

```python
class Evaluation(TypedDict):
    feedback: str
    marks: int  #This should not be a string.
```

Modify the evaluation prompt:

```python
prompt = PromptTemplate(
    template="""You are a Java code evaluator. ... (rest of the prompt) ... Return your answer as a JSON object: `{"feedback": "your feedback here", "marks": 10}`.
    """,
    input_variables=["student_solution", "model_solution", "rubric"]
)
```

And the parsing in the evaluation function:

```python
response = chain.invoke({"student_solution": student_solution_content, "model_solution": model_solution_content, "rubric": rubric_content})
    try:
        evaluation_data = json.loads(response.content)
        print(evaluation_data)
        return {"messages": [AIMessage("Evaluation: \n"+evaluation_data['feedback']), HumanMessage("Marks: "+str(evaluation_data['marks']))]}
    except json.JSONDecodeError:
        print("Error: LLM response is not valid JSON. Check the LLM response.")
        return {"messages": [AIMessage("Evaluation Failed."), HumanMessage("Marks: 0")]} # Handle error gracefully.
```

**4. State Saving: 0 marks**

The state isn't used effectively.  The marks are printed to the console but aren't saved for aggregation.

**Solution:**

Modify the `evaluation` function to save the extracted marks in the state:

```python
def evaluation(state):
    # ... (rest of the function) ...
    try:
        evaluation_data = json.loads(response.content)
        state["marks"] = evaluation_data['marks'] #Save marks to state
        return {"messages": [AIMessage("Evaluation: \n"+evaluation_data['feedback']), HumanMessage("Marks: "+str(evaluation_data['marks']))], "marks": evaluation_data["marks"]}
    # ... (error handling) ...
```

And finally, access and print the total marks after the workflow completes (you would need to modify the workflow execution to handle the updated return).


By implementing these changes, you'll significantly improve the robustness and accuracy of your mark extraction process, leading to a much higher score on the rubric.  Remember to carefully craft your LLM prompts to ensure they return structured data that is easily parsed by your Python code.  Always handle potential errors (e.g., invalid JSON from the LLM) gracefully.


The provided code is a good starting point for an automated code evaluation system, but it has several flaws that prevent it from achieving a high score on the described rubric.  The biggest issue is the lack of a `sum_marks` tool and the improper use of Langchain for achieving the desired functionality.  Let's break down the problems and propose solutions.

**Problems:**

1. **No `sum_marks` Tool:** The rubric explicitly requires a `sum_marks` tool, which is completely absent from the code.  The code extracts marks, but there's no mechanism to sum them across different evaluation criteria.

2. **Improper Prompt Design for Mark Summation:** The prompts don't instruct the LLM to explicitly provide marks in a structured format easily summable. The current `evaluation` function relies on the LLM to output a single `marks` integer.  This is unreliable and doesn't allow for partial credit or multiple criteria.

3. **Error Handling:** There's no error handling. If the LLM fails to extract information correctly, the program might crash or produce incorrect results.

4. **State Management:** While the code uses `StateGraph`, it doesn't effectively manage the state for summing marks.  The final total isn't reliably stored and retrieved.

5. **Unnecessary Complexity:** The code uses `PromptTemplate` excessively. Many of the steps could be simplified and made more robust.

6. **Hardcoded File Paths:**  The file paths (`student_solution.md`, `model_solution.md`, `rubric.md`) are hardcoded.  This makes the code inflexible.


**Proposed Solution:**

We'll restructure the code to incorporate a `sum_marks` function and improve the prompt design for reliable mark extraction.

```python
import getpass
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict
from typing import Dict, Annotated, Sequence, List
from langgraph.graph import END, START, StateGraph
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage
from langgraph.graph.message import add_messages
import pprint

_set_env("OPENAI_API_KEY")  # Assuming this function is defined elsewhere

model = ChatOpenAI(temperature=0, model="gpt-4o-mini")

class extracted_code(TypedDict):
    extracted_class: str

class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    total_marks: int  # Added to track total marks

def class_extraction(state: State) -> State:
    # ... (class_extraction function remains largely unchanged) ...
    return {"messages": [studentMessage, modelMessage], "total_marks": state.get("total_marks", 0)} # Preserve total_marks

def rubric_extraction(state: State) -> State:
    # ... (rubric_extraction function remains largely unchanged) ...
    return {"messages": [HumanMessage("Rubrik: \n"+output.content)], "total_marks": state.get("total_marks", 0)}

def evaluation(state: State) -> State:
    # ... (Get student_solution, model_solution, rubric from state) ...

    prompt = PromptTemplate(
        template="""You are a Java code evaluator.  ... (rest of the prompt) ...
        Return feedback and a list of marks for each criterion, one per line in the format: "Criterion: Mark".  Example:
        "Correctness: 5"
        "Efficiency: 3"
        "Readability: 2"
        """,
        input_variables=["student_solution", "model_solution", "rubric"]
    )

    class Evaluation(TypedDict):
        feedback: str
        marks_list: List[str]

    llm = model.with_structured_output(Evaluation)
    response = chain.invoke({"student_solution": student_solution, "model_solution": model_solution, "rubric": rubrik})
    marks = [int(x.split(":")[1].strip()) for x in response["marks_list"] if ":" in x]
    total_marks = sum(marks)

    return {
        "messages": [AIMessage("Evaluation: \n"+response['feedback']), HumanMessage("Marks Breakdown: " + str(marks)), HumanMessage(f"Total Marks: {total_marks}")],
        "total_marks": total_marks
    }

def sum_marks(state: State) -> State:
    return {"messages": state["messages"], "total_marks": state["total_marks"]}

# ... (rest of the code, including read_md_file and workflow definition) ...

workflow.add_node("sum_marks", sum_marks)
workflow.add_edge("evaluation", "sum_marks")
workflow.add_edge("sum_marks", END)

# ... (rest of the code) ...


graph = workflow.compile()

# Example usage (replace with actual file loading)

initial_state = {"messages": [], "total_marks": 0}
for output in graph.stream(initial_state):
    pprint.pprint(output)

```

This revised code introduces a `sum_marks` function, modifies the prompts to elicit structured mark output, and handles the state more effectively.  Remember to replace placeholder comments with your actual file reading and handling logic.  Thorough testing is crucial to ensure the LLM consistently provides the marks in the expected format.  Consider adding more robust error handling and input validation for production use.  The  `gpt-4o-mini` model may struggle with complex evaluations; consider using a more powerful model for better accuracy.


The code correctly creates a LangGraph with nodes and edges representing the workflow.  The rubric criteria are mostly met. Here's a breakdown:

**7. Graph Construction [14 marks]:**

* **Correct addition of nodes to the graph (5 marks):**  5 marks. All three modules (`class_extraction`, `rubric_extraction`, `evaluation`) are correctly added as nodes.

* **Correct addition of edges to the graph (5 marks):** 5 marks. The edges correctly represent the flow: `START` -> `class_extraction` -> `rubric_extraction` -> `evaluation` -> `END`.

* **Correct compilation of the graph (4 marks):** 4 marks. `workflow.compile()` is called correctly, creating the executable graph.


**Areas for Improvement and potential deductions (hypothetical):**

While the code fulfills the basic requirements,  a few points could lead to minor deductions if strictly assessed:

* **Error Handling:**  The code lacks error handling.  What happens if `read_md_file` fails to open a file?  Robust code should include `try-except` blocks to gracefully handle such situations.  This is crucial for production-ready systems.  A missing error handling could justify a small deduction (maybe 1 mark across the three sections).

* **`rubric_extraction` function:** The `rubric_extraction` function recursively calls itself. This is likely a mistake. It should probably read the rubric file, process it, and return the result, instead of calling `rubric_extraction(read_md_file(rubric))`. This recursion will result in a stack overflow because the base case is not defined.  This is a significant error that could lead to a larger deduction (possibly 2-3 marks depending on the severity of the rubric section's assessment).


* **`evaluation` function's output:** The `evaluation` function prints the `response` before returning it.  While this doesn't break functionality, it's generally better to keep printing separate from the core logic.  This is a minor stylistic issue and might not affect the score significantly.

* **Input Handling:** The commented-out section suggests the intention to handle inputs.  While not required by the prompt,  a more complete system might benefit from explicit input handling. This is not required for the rubric and wouldn't impact the score.

**Overall:**

Based on the provided code and rubric, the score would be **14/14**. However, addressing the `rubric_extraction` function error and adding robust error handling would make the code significantly more robust and production-ready.


This code implements a LangChain-based workflow for automatically evaluating Java code.  Let's break down the code, identify potential issues, and suggest improvements.

**Code Breakdown:**

1. **Environment Setup:** The code starts by setting the `OPENAI_API_KEY` environment variable, prompting the user for the key if it's not already set.

2. **OpenAI Model Initialization:** It initializes a `ChatOpenAI` model using `gpt-4o-mini` with temperature set to 0 (deterministic outputs).

3. **TypedDicts:**  `extracted_code` and `State` are defined using `TypedDict` for type hinting and better code readability.

4. **`class_extraction` Function:** This function reads student and model solutions from `.md` files, uses a prompt to extract the class code from each, and returns a `State` containing the extracted code as `HumanMessage` objects.  **Crucial Issue:** It assumes the `.md` files contain Java code *directly within the markdown*.  This is a very fragile assumption. Realistically, the Java code would be embedded using code blocks (```java ... ```).  The prompt needs to be significantly improved to handle this correctly.

5. **`rubric_extraction` Function:**  This function reads a rubric from a `.md` file.  **Major Issue:** The function calls itself recursively, leading to infinite recursion. This line `extracted_rubric = rubric_extraction(read_md_file(rubric))` is the problem. It should use a prompt to extract the rubric criteria, not recursively call itself.

6. **`evaluation` Function:** This function takes the student's solution, model solution, and rubric (as messages) and uses a prompt to evaluate the student's code, returning feedback and a mark.

7. **`read_md_file` Function:** A helper function to read the contents of a markdown file.

8. **Workflow Definition:** A `StateGraph` is used to define the workflow:  `class_extraction` -> `rubric_extraction` -> `evaluation`.

9. **Main Execution Block:** The commented-out section shows how the workflow would be executed, iterating through the graph and printing the outputs.


**Issues and Improvements:**

* **Markdown Handling:** The biggest issue is the assumption that Java code is directly in the `.md` files.  Use a regex or a more robust parser to extract code blocks from markdown files.  For example, using `re.findall(r'```java(.*?)```', file_content, re.DOTALL)` to extract Java code blocks.

* **Infinite Recursion in `rubric_extraction`:**  Fix the recursive call in `rubric_extraction`. The function should read the rubric from the file and then use the prompt to extract the relevant information.

* **Prompt Engineering:** The prompts need refinement.  They are currently quite basic.  More context and specific instructions are needed to ensure accurate and reliable results from the LLM.  For example, provide examples of what constitutes a good vs. bad answer according to the rubric.

* **Error Handling:** Add error handling (e.g., `try...except` blocks) to gracefully handle file I/O errors and potential LLM errors.

* **Input Validation:** Validate the inputs to the functions.  Check that the files exist, that the code is valid Java (optionally), and that the rubric is well-formed.

* **More Robust Parsing:** Consider using a dedicated Markdown parser instead of relying solely on string manipulation. Libraries like `markdown` can help with this.

* **Output Formatting:**  The output currently isn't very well-formatted. Consider using a templating engine or formatting library to produce cleaner and more readable feedback.

* **Unclear Rubric Structure:**  The code doesn't specify the format of the rubric. A structured format (e.g., JSON or YAML) would make processing much easier and less error-prone than relying on natural language parsing alone.


**Revised `class_extraction` Function (example):**

```python
import re

def class_extraction(state):
    # ... (rest of the function)

    # Extract Java code blocks using regex
    student_code = re.findall(r'```java(.*?)```', student_solution_file_contents, re.DOTALL)
    model_code = re.findall(r'```java(.*?)```', model_solution_file_contents, re.DOTALL)

    # Handle cases where no code is found
    if not student_code or not model_code:
        return {"messages": [HumanMessage("Error: Could not extract Java code from file.")]}

    student_output = {"extracted_class": student_code[0].strip()}  #Take the first code block
    model_output = {"extracted_class": model_code[0].strip()}

    # ... (rest of the function)
```

Remember to fix the `rubric_extraction` function and improve the prompts significantly for a more robust and reliable code evaluation system.  Consider using a structured format for the rubric (e.g., JSON) for better parsing and error handling.
