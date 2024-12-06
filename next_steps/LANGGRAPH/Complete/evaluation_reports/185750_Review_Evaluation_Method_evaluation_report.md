## LangGraph - Student Submission Evaluation

**Overall Marks:** 14/50

**Detailed Report:**

#### 1. Extract Class Method [2/6]
**1.1. Prompt Design [1/3]:**  
The prompt attempts to extract classes, but it lacks specific instructions on the desired output format.  A more structured prompt specifying the desired JSON format for class names and code would improve accuracy.

**1.2. Parsing/Output Extraction [1/2]:**  
The student's code attempts to parse the LLM output, but the parsing is incomplete and does not consistently extract classes accurately. The `parse_extracted_classes` function needs refinement to handle variations in LLM output.

**1.3. State Saving [0/1]:**  
The extracted classes are not saved into the state variable.  The code lacks the necessary state updates for the `extracted_classes` within the class_extraction method.


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

#### 7. Graph Construction [12/14]
**7.1. Correct Addition of Nodes to the Graph [5/5]:**  
The student correctly added nodes to the LangGraph, representing each stage of the process.

**7.2. Correct Addition of Edges to the Graph [5/5]:**  
The student correctly defined the edges connecting the nodes, showing a proper sequential workflow.

**7.3. Correct Compilation of Graph [2/4]:**  
The graph compiles, but the conditional edge routing logic within the router function and the tool invocation are not fully functional. The application does not complete the entire workflow.


---

**Feedback:**  
The student demonstrates a basic understanding of LangGraph by creating a graph structure and connecting nodes.  However, the core evaluation logic, including prompt design, parsing, and state management, is largely incomplete.  Focus on refining prompts for clearer instructions, developing robust parsing techniques, and implementing all required modules to complete the evaluation workflow.
