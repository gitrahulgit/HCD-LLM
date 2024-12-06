## LangGraph - Student Submission Evaluation

**Overall Marks:** 14/50

**Detailed Report:**

#### 1. Extract Class Method [1/6]
**1.1. Prompt Design [1/3]:**  
The prompt attempts to extract classes but lacks sophistication. It doesn't explicitly define the expected output format, leading to unpredictable results.  More precise instructions on how to structure the extracted classes would improve the prompt.

**1.2. Parsing/Output Extraction [0/2]:**  
The code does not correctly parse the LLM's output.  The `parse_extracted_classes` function is poorly implemented and doesn't reliably extract class definitions.  It relies on heuristics that are prone to failure with variations in code formatting.

**1.3. State Saving [0/1]:**  
The extracted class information is not properly saved into the state variable.  The state management within the `class_extraction` function needs to be implemented.

#### 2. Extract Rubric Method [0/6]
**2.1. Prompt Design [0/3]:**  
This module is not implemented.

**2.2. Parsing/Output Extraction [0/2]:**  
This module is not implemented.

**2.3. State Saving [0/1]:**  
This module is not implemented.

#### 3. Initial Evaluation Method [0/6]
**3.1. Prompt Design [0/3]:**  
This module is not implemented.

**3.2. Parsing/Output Extraction [0/2]:**  
This module is not implemented.

**3.3. State Saving [0/1]:**  
This module is not implemented.

#### 4. Review Evaluation Method [0/6]
**4.1. Prompt Design [0/3]:**  
This module is not implemented.

**4.2. Parsing/Output Extraction [0/2]:**  
This module is not implemented.

**4.3. State Saving [0/1]:**  
This module is not implemented.

#### 5. Marks Extraction Method [0/6]
**5.1. Prompt Design [0/3]:**  
This module is not implemented.

**5.2. Parsing/Output Extraction [0/2]:**  
This module is not implemented.

**5.3. State Saving [0/1]:**  
This module is not implemented.

#### 6. Total Marks Calculation Method [0/6]
**6.1. Prompt Design [0/3]:**  
This module is not implemented.

**6.2. Parsing/Output Extraction [0/2]:**  
This module is not implemented.

**6.3. State Saving [0/1]:**  
This module is not implemented.

#### 7. Graph Construction [13/14]
**7.1. Correct Addition of Nodes to the Graph [5/5]:**  
The student correctly added nodes for each step in the workflow.

**7.2. Correct Addition of Edges to the Graph [5/5]:**  
The student added edges between nodes to represent the flow of data and operations.

**7.3. Correct Compilation of Graph [3/4]:**  
The graph compiles, but the conditional logic in the router function is not completely effective due to missing implementation of other modules which would feed into the router function.


---

**Feedback:**  
The student demonstrated a basic understanding of LangGraph by creating a workflow graph. However, the core functionality of extracting classes, processing rubrics, and performing evaluations is missing.  Focus on improving prompt design, output parsing, and state management to make the individual modules functional. Implement the missing parts of the application step by step.
