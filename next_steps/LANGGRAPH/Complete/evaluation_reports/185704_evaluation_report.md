## LangGraph - Student Submission Evaluation

**Overall Marks:** 14/50

**Detailed Report:**

#### 1. Extract Class Method [1/6]
**1.1. Prompt Design [0/3]:**  
The student does not use an LLM for class extraction.  The code uses regular expressions to extract classes, which is not in line with the requirements.  A proper LLM prompt was not designed.

**1.2. Parsing/Output Extraction [1/2]:**  
The regular expression-based class extraction partially works, extracting the classes present. However, this approach violates the requirement to use an LLM.

**1.3. State Saving [0/1]:**  
The extracted class information is not saved to state variables.


#### 2. Extract Rubric Method [0/6]
**2.1. Prompt Design [0/3]:**  
No LLM prompt is designed or used for rubric extraction.

**2.2. Parsing/Output Extraction [0/2]:**  
No rubric details are extracted.

**2.3. State Saving [0/1]:**  
No state saving of rubric details is implemented.


#### 3. Initial Evaluation Method [0/6]
**3.1. Prompt Design [0/3]:**  
No LLM prompt is used for the initial evaluation.

**3.2. Parsing/Output Extraction [0/2]:**  
No scores or comments are extracted.

**3.3. State Saving [0/1]:**  
No initial evaluation results are saved.


#### 4. Review Evaluation Method [0/6]
**4.1. Prompt Design [0/3]:**  
No LLM prompt for reviewing evaluations is present.

**4.2. Parsing/Output Extraction [0/2]:**  
No reviewed evaluations are extracted.

**4.3. State Saving [0/1]:**  
No state saving of reviewed evaluations is done.


#### 5. Marks Extraction Method [0/6]
**5.1. Prompt Design [0/3]:**  
No prompt design for marks extraction is visible.

**5.2. Parsing/Output Extraction [0/2]:**  
No marks are extracted.

**5.3. State Saving [0/1]:**  
No state management of extracted marks is done.


#### 6. Total Marks Calculation Method [0/6]
**6.1. Prompt Design [0/3]:**  
The `sum_marks` tool is not used within an LLM prompt.

**6.2. Parsing/Output Extraction [0/2]:**  
The final sum is not extracted.

**6.3. State Saving [0/1]:**  
The final marks are not saved.


#### 7. Graph Construction [13/14]
**7.1. Correct Addition of Nodes to the Graph [5/5]:**  
All modules are correctly added as nodes, although their implementations are incorrect.

**7.2. Correct Addition of Edges to the Graph [5/5]:**  
All the edges between the modules are correctly added.

**7.3. Correct Compilation of Graph [3/4]:**  
The graph compilation is attempted but is not functional due to the absence of LLM usage in the preceding modules.


---

**Feedback:**  
The student's submission demonstrates a basic understanding of LangGraph's structure and workflow.  The graph construction is mostly correct. However, the core requirement of utilizing LLMs within each module for the evaluation process was not implemented, resulting in a non-functional application.  The student should focus on integrating LLM calls within each function and appropriately handling the LLM responses.  The regular expression-based approach shows some basic programming skill, but this is not applicable to this assignment.
