## LangGraph - Student Submission Evaluation

**Overall Marks:** 14/50

**Detailed Report:**

#### 1. Extract Class Method [1/6]
**1.1. Prompt Design [0/3]:**  
The student did not implement a method for extracting Java classes.  The code attempts to use web scraping instead of processing the input files provided.

**1.2. Parsing/Output Extraction [0/2]:**  
No class extraction was implemented.

**1.3. State Saving [0/1]:**  
No state saving related to class extraction was performed.

#### 2. Extract Rubric Method [0/6]
**2.1. Prompt Design [0/3]:**  
No rubric extraction method was implemented. The code attempts to use web scraping instead of processing the input files provided.

**2.2. Parsing/Output Extraction [0/2]:**  
No rubric details were extracted.

**2.3. State Saving [0/1]:**  
No state was saved for rubric details.

#### 3. Initial Evaluation Method [0/6]
**3.1. Prompt Design [0/3]:**  
No initial evaluation method was implemented.

**3.2. Parsing/Output Extraction [0/2]:**  
No scores or comments were extracted.

**3.3. State Saving [0/1]:**  
No state saving was done for initial evaluations.

#### 4. Review Evaluation Method [0/6]
**4.1. Prompt Design [0/3]:**  
No review evaluation method was implemented.

**4.2. Parsing/Output Extraction [0/2]:**  
No reviewed evaluations were extracted.

**4.3. State Saving [0/1]:**  
No state saving was done for reviewed evaluations.

#### 5. Marks Extraction Method [0/6]
**5.1. Prompt Design [0/3]:**  
No marks extraction method was implemented.

**5.2. Parsing/Output Extraction [0/2]:**  
No marks were extracted.

**5.3. State Saving [0/1]:**  
No state management for marks was performed.

#### 6. Total Marks Calculation Method [0/6]
**6.1. Prompt Design [0/3]:**  
The `sum_marks` tool was not utilized in the student's submission.

**6.2. Parsing/Output Extraction [0/2]:**  
No final sum was extracted.

**6.3. State Saving [0/1]:**  
No final marks were saved.

#### 7. Graph Construction [14/14]
**7.1. Correct Addition of Nodes to the Graph [5/5]:**  
The student added nodes for class extraction, rubric extraction, initial evaluation, review evaluation, marks extraction, and total marks calculation.

**7.2. Correct Addition of Edges to the Graph [5/5]:**  
The student correctly added edges to connect the nodes in a sequential workflow.

**7.3. Correct Compilation of Graph [4/4]:**  
The graph was correctly compiled using `workflow.compile()`.


---

**Feedback:**  
The student's submission demonstrates a partial understanding of LangGraph's structure by creating a basic graph. However, the core functionality of evaluating Java code using LLMs was not implemented.  The code focuses on web scraping instead of the provided input files.  The student needs to focus on implementing the LLM-based modules for class extraction, evaluation, and marks processing.  Understanding the prompt engineering aspect is crucial for success.
