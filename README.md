# LLM Exam Project

This repository contains resources for evaluating student solutions using a modular approach and a complete rubric approach. The structure is designed for both Java and LangGraph (lg) programming exercises, including solutions, student submissions, detailed rubric, evaluation reports, and scripts to process the reports/results.

### Key Components

- **Complete:** Contains script files for evaluating entire rubric items at once.
- **Partial:** Handles evaluation module by module.
- **evaluation\_reports:** Stores evaluation results.
- **json\_from\_reports.py:** Processes evaluation reports to generate JSON summaries.
- **main\_****.py:** Main script for complete rubric evaluation.
- **main\_****\_partial.py:** Main script for partial rubric evaluation.

---

## Steps to Execute

### 1. Clone the Repository

Download the repository using one of the following methods:

#### Option 1: Clone via Git

```bash
git clone <repository_url>
cd llm_exam
```

#### Option 2: Download ZIP

- Download the ZIP file of the repository.
- Extract the contents to a directory.

---

### 2. Create a Virtual Environment

Create a Python virtual environment to manage dependencies:

```bash
python -m venv env
env\Scripts\activate
```

---

### 3. Install Dependencies

Install all required Python libraries using `requirements.txt` (create one if not present):

```bash
pip install -r requirements.txt
```

---

### 4. Run Evaluation Scripts

Navigate to the appropriate folder based on the task (e.g., `JAVA` or `LANGGRAPH`) and whether you want to run a complete or partial evaluation.

#### Example: Run Complete Evaluation for Java

```bash
cd next_steps/JAVA/Complete
python main_java.py
```

#### Example: Run Partial Evaluation for LangGraph

```bash
cd Resources/LANGGRAPH/Partial
python main_lg_partial.py
```

---

### 5. Generate Reports

Use the `json_from_reports.py` script to process evaluation results:

```bash
python json_from_reports.py
```

This will create a JSON file summarizing the evaluation.

---

## Additional Files

### 1. `model_solution.py`

Contains the reference solution for the exercises.

### 2. `problem_statement.md`

Details the problem statement for the tasks.

### 3. `prompt.md`

Provides instructions or prompts for the tasks.

### 4. `report_format.md`

Describes the expected format for evaluation reports.

### 5. `rubric.md`

Defines the rubric used for evaluation.

---

## Notes

- Ensure all dependencies are installed before running any scripts.
- Adjust paths in scripts if running from a different directory.
- All evaluation reports are stored in their respective `evaluation_reports` folders.

---
