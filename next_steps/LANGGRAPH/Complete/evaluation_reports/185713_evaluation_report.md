## LangGraph - Student Submission Evaluation

**Overall Marks:** 14/50

**Detailed Report:**

#### 1. Extract Class Method [1/6]
**1.1. Prompt Design [0/3]:**  
The student's prompt is extremely basic and does not guide the LLM to effectively extract classes, only class names.  It lacks detail and specific instructions on how to handle multiple classes, resulting in an incomplete solution.

**1.2. Parsing/Output Extraction [1/2]:**  
The code attempts to parse the LLM output, extracting class names, however, this misses the code associated with each class, making it incomplete.

**1.3. State Saving [0/1]:**  
The extracted class information (only names, not code) is not correctly saved into the state variables for further use in subsequent parts of the workflow.

#### 2. Extract Rubric Method [0/6]
**2.1. Prompt Design [0/3]:**  
No rubric extraction method is implemented.

**2.2. Parsing/Output Extraction [0/2]:**  
No rubric extraction is attempted.

**2.3. State Saving [0/1]:**  
No state saving is implemented.

#### 3. Initial Evaluation Method [0/6]
**3.1. Prompt Design [0/3]:**  
No initial evaluation method is implemented.

**3.2. Parsing/Output Extraction [0/2]:**  
No parsing of initial evaluations is attempted.

**3.3. State Saving [0/1]:**  
No state management for initial evaluations is done.


#### 4. Review Evaluation Method [0/6]
**4.1. Prompt Design [0/3]:**  
No review evaluation method is implemented.

**4.2. Parsing/Output Extraction [0/2]:**  
No extraction of reviewed evaluations is attempted.

**4.3. State Saving [0/1]:**  
No state saving is implemented.

#### 5. Marks Extraction Method [0/6]
**5.1. Prompt Design [0/3]:**  
No marks extraction method is implemented.

**5.2. Parsing/Output Extraction [0/2]:**  
No marks extraction is implemented.

**5.3. State Saving [0/1]:**  
No state management for extracted marks is done.

#### 6. Total Marks Calculation Method [0/6]
**6.1. Prompt Design [0/3]:**  
No total marks calculation method is implemented.

**6.2. Parsing/Output Extraction [0/2]:**  
No extraction of the final sum is implemented.

**6.3. State Saving [0/1]:**  
No state saving for the final marks is implemented.

#### 7. Graph Construction [13/14]
**7.1. Correct Addition of Nodes to the Graph [5/5]:**  
All modules are added as nodes, although some are not implemented.

**7.2. Correct Addition of Edges to the Graph [5/5]:**  
The edges between the nodes are correctly structured, representing the intended workflow.

**7.3. Correct Compilation of Graph [3/4]:**  
The graph compilation is mostly correct, with the functionality working, however, the graph lacks most of its necessary function implementation.


---

**Feedback:**  
The student's submission demonstrates a basic understanding of LangGraph's structure by setting up a workflow graph.  However, the core functionality of the code for evaluating Java code is largely missing. Focus on implementing the LLM prompts and output parsing for each module to make the workflow complete and functional.  The `class_extraction` function is a good starting point, but it needs to be expanded to extract the class code itself, rather than only names.
