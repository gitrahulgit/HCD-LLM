## LangGraph - Student Submission Evaluation

**Overall Marks:** 14/50

**Detailed Report:**

#### 1. Extract Class Method [2/6]
**1.1. Prompt Design [1/3]:**  
The prompt is partially complete. It attempts to extract classes but lacks specificity in handling potential variations in code structure.  It doesn't explicitly instruct the LLM on how to format the output for easy parsing, which is crucial.

**1.2. Parsing/Output Extraction [1/2]:**  
The student's code attempts to parse the LLM output, but the parsing logic is rudimentary and fails to reliably extract classes from varied code structures.  The parsing is not robust enough to handle unexpected formatting.

**1.3. State Saving [0/1]:**  
Extracted class information is not properly saved into the state variable. The code lacks the necessary mechanisms to store the extracted classes for subsequent use within the LangGraph workflow.

#### 2. Extract Rubric Method [0/6]
**2.1. Prompt Design [0/3]:**  
The prompt design is missing. The student's code doesn't include a defined prompt for extracting rubric details.  This module is completely absent.

**2.2. Parsing/Output Extraction [0/2]:**  
No parsing or extraction is attempted as the prompt is missing.

**2.3. State Saving [0/1]:**  
No state saving is implemented for this module.


#### 3. Initial Evaluation Method [0/6]
**3.1. Prompt Design [0/3]:**  
The prompt design for initial evaluation is missing. The module is not implemented.

**3.2. Parsing/Output Extraction [0/2]:**  
No parsing or extraction is attempted.

**3.3. State Saving [0/1]:**  
No state saving occurs.


#### 4. Review Evaluation Method [0/6]
**4.1. Prompt Design [0/3]:**  
The prompt is missing. This module is not implemented.

**4.2. Parsing/Output Extraction [0/2]:**  
No parsing or extraction.

**4.3. State Saving [0/1]:**  
No state saving.


#### 5. Marks Extraction Method [0/6]
**5.1. Prompt Design [0/3]:**  
The prompt is missing.  The module is absent.

**5.2. Parsing/Output Extraction [0/2]:**  
No parsing or extraction is done.

**5.3. State Saving [0/1]:**  
No state saving.


#### 6. Total Marks Calculation Method [0/6]
**6.1. Prompt Design [0/3]:**  
The prompt design is missing. This module is not implemented.

**6.2. Parsing/Output Extraction [0/2]:**  
No parsing or extraction of the final sum is attempted.

**6.3. State Saving [0/1]:**  
No state saving is done.


#### 7. Graph Construction [12/14]
**7.1. Correct Addition of Nodes to the Graph [5/5]:**  
All modules are correctly added as nodes, although many are not functional.

**7.2. Correct Addition of Edges to the Graph [5/5]:**  
All edges between the nodes are correctly added, representing the intended workflow, though a significant portion of the workflow is incomplete.

**7.3. Correct Compilation of Graph [2/4]:**  
The graph compiles, but several nodes are non-functional, leading to a broken workflow.  The compilation itself is correct but the result is incomplete.


---

**Feedback:**  
The student demonstrates a basic understanding of LangGraph's graph structure and node connection, successfully building the graph skeleton. However, the crucial logic within each node is largely absent or incomplete, preventing the program from functioning as intended. Focus on completing the LLM prompts and implementing robust parsing and state management within each node.  Prioritize completing one module fully before moving to the next.
