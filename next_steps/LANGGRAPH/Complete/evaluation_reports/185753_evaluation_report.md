## LangGraph - Student Submission Evaluation

**Overall Marks:** 14/50

**Detailed Report:**

#### 1. Extract Class Method [1/6]
**1.1. Prompt Design [0/3]:**  
The student's code attempts to use a prompt for class extraction, but it is not a proper LLM prompt. It lacks a clear instruction on how the LLM should format its output to easily parse extracted classes.  The prompt design doesn't specify the expected format and structure of the output, making parsing difficult.

**1.2. Parsing/Output Extraction [1/2]:**  
The `parse_extracted_classes` function attempts to parse the LLM output but is not robust and relies on the LLM providing an output which is easily parsable, making it unreliable. While a partial implementation is visible, it lacks the correctness to effectively extract all classes from the LLM output.

**1.3. State Saving [0/1]:**  
The extracted class information is not properly saved into state variables. The function returns a dictionary, but this dictionary is not integrated with a LangGraph state mechanism, resulting in a lack of state saving.


#### 2. Extract Rubric Method [0/6]
**2.1. Prompt Design [0/3]:**  
No prompt is designed or implemented for rubric extraction.

**2.2. Parsing/Output Extraction [0/2]:**  
No parsing or extraction of rubric details is implemented.

**2.3. State Saving [0/1]:**  
No state saving for rubric details is implemented.


#### 3. Initial Evaluation Method [0/6]
**3.1. Prompt Design [0/3]:**  
No prompt is designed for initial evaluation.

**3.2. Parsing/Output Extraction [0/2]:**  
No parsing or extraction of initial evaluations is implemented.

**3.3. State Saving [0/1]:**  
No state saving for initial evaluations is implemented.


#### 4. Review Evaluation Method [0/6]
**4.1. Prompt Design [0/3]:**  
No prompt is designed for reviewing evaluations.

**4.2. Parsing/Output Extraction [0/2]:**  
No parsing or extraction of reviewed evaluations is implemented.

**4.3. State Saving [0/1]:**  
No state saving for reviewed evaluations is implemented.


#### 5. Marks Extraction Method [0/6]
**5.1. Prompt Design [0/3]:**  
No prompt is implemented for marks extraction.

**5.2. Parsing/Output Extraction [0/2]:**  
No parsing or extraction of marks is implemented.

**5.3. State Saving [0/1]:**  
No state saving for extracted marks is implemented.


#### 6. Total Marks Calculation Method [0/6]
**6.1. Prompt Design [0/3]:**  
The `sum_marks` function is implemented, but it is not used within the LangGraph framework and is not bound to the LLM for total marks calculation.  There is no prompt design to integrate this tool with the LLM workflow.

**6.2. Parsing/Output Extraction [0/2]:**  
No extraction of the final sum of marks is implemented within the LangGraph context.

**6.3. State Saving [0/1]:**  
No state saving of total marks is implemented.


#### 7. Graph Construction [13/14]
**7.1. Correct Addition of Nodes to the Graph [5/5]:**  
The student correctly added nodes for each module to the LangGraph.

**7.2. Correct Addition of Edges to the Graph [5/5]:**  
The student mostly correctly added edges representing the workflow between nodes.  There is a slight deviation, showing a potential misunderstanding of the expected flow.

**7.3. Correct Compilation of Graph [3/4]:**  
The graph compilation is mostly correct, however, there is an error in running the graph due to missing elements in the code.

---

**Feedback:**  
The student demonstrates some understanding of LangGraph by correctly setting up the nodes of the graph.  However,  the implementation of the individual modules is incomplete and lacks crucial aspects of LLM prompt engineering, output parsing, and state management within the LangGraph framework.  Focus on improving prompt design, output parsing robustness, and proper state variable usage.  The model solution provides a comprehensive structure for guidance.
