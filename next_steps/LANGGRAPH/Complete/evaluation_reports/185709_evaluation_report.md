## LangGraph - Student Submission Evaluation

**Overall Marks:** 20/50

**Detailed Report:**

#### 1. Extract Class Method [3/6]
**1.1. Prompt Design [1/3]:** The prompt attempts to extract classes but lacks specificity regarding the desired output format (e.g., JSON).  It doesn't explicitly instruct the LLM to only extract the class code.

**1.2. Parsing/Output Extraction [1/2]:** The code attempts to parse the LLM response, but it is rudimentary and not robust enough to handle variations in LLM output.  It relies on the LLM producing JSON which may not always happen.

**1.3. State Saving [1/1]:** Extracted class information is saved to the `student_classes` state variable, though the method of extraction is unreliable, as mentioned before.


#### 2. Extract Rubric Method [0/6]
**2.1. Prompt Design [0/3]:**  The prompt design is missing.  There's no mechanism implemented to extract rubric details for individual classes.

**2.2. Parsing/Output Extraction [0/2]:** No rubric details are extracted due to the lack of implementation.

**2.3. State Saving [0/1]:**  No state saving is implemented for rubric details.


#### 3. Initial Evaluation Method [0/6]
**3.1. Prompt Design [0/3]:** The prompt for this section is not present in the code.

**3.2. Parsing/Output Extraction [0/2]:** No parsing is done.

**3.3. State Saving [0/1]:** No state saving is implemented.


#### 4. Review Evaluation Method [0/6]
**4.1. Prompt Design [0/3]:** Missing prompt design for reviewing evaluations.

**4.2. Parsing/Output Extraction [0/2]:**  No parsing of reviewed evaluations.

**4.3. State Saving [0/1]:**  Missing state saving for reviewed evaluations.


#### 5. Marks Extraction Method [0/6]
**5.1. Prompt Design [0/3]:** Missing prompt design for marks extraction.

**5.2. Parsing/Output Extraction [0/2]:** No extraction of marks is implemented.

**5.3. State Saving [0/1]:** No state saving for extracted marks.


#### 6. Total Marks Calculation Method [0/6]
**6.1. Prompt Design [0/3]:** The `sum_marks` tool is defined, but it's not properly integrated into the workflow for total marks calculation.  The prompt for using this tool is not in the code.

**6.2. Parsing/Output Extraction [0/2]:** No final sum extraction is performed.

**6.3. State Saving [0/1]:**  No state saving of the total marks.


#### 7. Graph Construction [14/14]
**7.1. Correct Addition of Nodes to the Graph [5/5]:** All modules are added as nodes in the graph.

**7.2. Correct Addition of Edges to the Graph [5/5]:** All edges correctly connect modules in the workflow.

**7.3. Correct Compilation of Graph [4/4]:** The graph is compiled using `graph.compile()`.


---

**Feedback:**  The student demonstrates a basic understanding of LangGraph's structure by successfully constructing the graph and adding nodes and edges. However, the core functionality of using the LLM for code evaluation is largely incomplete and lacks well-defined prompts, output parsing, and state management in several crucial modules.  Focus on developing robust prompts that specify desired output formats (e.g., JSON) and improve the parsing logic to reliably extract information from the LLM responses.  Remember to handle potential errors from the LLM more gracefully.
