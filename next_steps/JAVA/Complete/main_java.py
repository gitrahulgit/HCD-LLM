import glob
import os
from tqdm import tqdm
import google.generativeai as genai
from json_from_reports import generate_json_for_reports

# Configure the AI model
genai.configure(api_key="AIzaSyDbh0mLOlOMwOb5ft9i63ol7KZIg4iBXGQ")
model = genai.GenerativeModel('gemini-1.5-flash-002')

# Define base paths
base_path = r"D:\llm_exam\next_steps\JAVA"
resources_folder = os.path.join(base_path, "Resources")
output_folder = os.path.join(base_path, "Complete", "evaluation_reports")
os.makedirs(output_folder, exist_ok=True)

# Load files into placeholders from the "Resources" folder
files_to_load = ["prompt.md", "model_solution.java", "problem_statement.md", "rubric.md", "report_format.md"]
file_contents = {}

for file_name in files_to_load:
    file_path = os.path.join(resources_folder, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        file_contents[file_name] = f.read()

# Extract relevant information from loaded files
evaluation_prompt_template = file_contents["prompt.md"]
model_solution = file_contents["model_solution.java"]
problem_statement = file_contents["problem_statement.md"]
rubric = file_contents["rubric.md"]
report_format = file_contents["report_format.md"]

# Get student solution paths from the "Resources/java_student_solutions" folder
solution_paths = glob.glob(os.path.join(resources_folder, "java_student_solutions", r"*student_solution.java"))
solution_paths.sort(key=lambda x: int(os.path.basename(x).split('_')[0]))

# Template for the combined evaluation prompt
combined_prompt_template = """
{evaluation_prompt_template}

---

#### Follow the detailed report format strictly:
{report_format}

---

### CONTEXT

**PROBLEM STATEMENT:**
{problem_statement}

**RUBRIC:**
{rubric}

**MODEL SOLUTION:**
{model_solution}

**STUDENT SOLUTION:**
{student_solution}
"""

# Generate reports for each student
for solution_path in tqdm(solution_paths):
    with open(solution_path, 'r', encoding='utf-8', errors='ignore') as f:
        student_solution = f.read()

    student_number = os.path.basename(solution_path).split('_')[0]

    # Use the combined prompt template and fill placeholders
    final_prompt = combined_prompt_template.format(
        evaluation_prompt_template=evaluation_prompt_template,
        report_format=report_format,
        problem_statement=problem_statement,
        rubric=rubric,
        model_solution=model_solution,
        student_solution=student_solution
    )

    # Generate evaluation using Gemini model
    result = model.generate_content([final_prompt])

    # Save the generated report to output folder
    output_name = f"student_{student_number}_report.md"
    output_path = os.path.join(output_folder, output_name)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result.text)
print("Reports generated successfully!")

# Generate JSON for reports
print("Generating JSON for reports...")
generate_json_for_reports(output_folder, "java_students_scores.json")