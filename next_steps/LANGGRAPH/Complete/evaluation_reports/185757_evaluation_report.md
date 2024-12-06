## LangGraph - Student Submission Evaluation

**Overall Marks:** 28/50

**Detailed Report:**

#### 1. Extract Class Method [4/6]
**1.1. Prompt Design [2/3]:** The prompt attempts to extract Java classes but lacks specifics regarding desired output format (e.g., JSON, key-value pairs).  The prompt should also explicitly state to only extract code and class names.

**1.2. Parsing/Output Extraction [2/2]:** The code correctly parses the LLM output and extracts classes from both student and model solutions.

**1.3. State Saving [0/1]:**  The extracted class information is not saved to state variables; it's stored in a dictionary within the `messages` state variable which is not consistent with the model solution or expectations.

#### 2. Extract Rubric Method [3/6]
**2.1. Prompt Design [2/3]:** The prompt design is reasonable but doesn't specify the desired format for the extracted rubric details.  It should request a structured output for each class.

**2.2. Parsing/Output Extraction [1/2]:** The rubric extraction partially works; however, the parsing only takes the entire rubric as a single string rather than structured rubric details for each class.

**2.3. State Saving [0/1]:**  Similar to class extraction, rubric details are stored in the `messages` variable, not proper state variables.


#### 3. Initial Evaluation Method [3/6]
**3.1. Prompt Design [2/3]:** The prompt structure is acceptable, but it could be improved by clearly defining the expected format for the evaluation (scores and comments).

**3.2. Parsing/Output Extraction [1/2]:** Partial extraction is achieved, but the extraction of scores is not robust. It relies on the LLM to perfectly format the output which isn't reliable.

**3.3. State Saving [0/1]:** Initial evaluations are stored within the `messages` state variable, not in dedicated state variables.

#### 4. Review Evaluation Method [3/6]
**4.1. Prompt Design [2/3]:** The prompt is reasonably structured for reviewing evaluations but could benefit from clearer instructions on the format of corrections.

**4.2. Parsing/Output Extraction [1/2]:** Similar to the initial evaluation, the extraction lacks robustness in reliably retrieving the review and adjustments.


**4.3. State Saving [0/1]:** The reviewed evaluations are not saved to proper state variables.  They remain in the `messages` list.

#### 5. Marks Extraction Method [2/6]
**5.1. Prompt Design [1/3]:** The prompt attempts to extract marks but does not explicitly specify that the desired output should be a comma separated string of numeric marks.

**5.2. Parsing/Output Extraction [1/2]:**  Partial extraction of marks happens, but the implementation isn't robust enough to handle various output formats from the LLM.

**5.3. State Saving [0/1]:** The extracted marks are not saved correctly into the state. They're within the `messages` state.

#### 6. Total Marks Calculation Method [3/6]
**6.1. Prompt Design [2/3]:** The prompt correctly uses the `sum_marks` tool.

**6.2. Parsing/Output Extraction [1/2]:** The final sum is extracted, however the implementation is dependent on a specific format from the LLM, which is not reliable.

**6.3. State Saving [0/1]:** The total marks are not correctly saved to the designated state variable.

#### 7. Graph Construction [14/14]
**7.1. Correct Addition of Nodes to the Graph [5/5]:** All modules are added as nodes.

**7.2. Correct Addition of Edges to the Graph [5/5]:**  All edges between the modules are correctly added.

**7.3. Correct Compilation of Graph [4/4]:** The graph compiles correctly.


---

**Feedback:**  The student demonstrates understanding of LangChain and the concept of creating a LangGraph workflow.  However, there are significant flaws in prompt engineering, output parsing, and state management.  Focus on structuring LLM prompts to elicit specific, consistently formatted outputs and implementing robust parsing mechanisms to extract the necessary information.  Correct state management is critical for the workflow's functionality.
