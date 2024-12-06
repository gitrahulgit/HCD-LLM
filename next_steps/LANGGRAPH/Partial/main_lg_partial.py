import glob
import os
from tqdm import tqdm
import google.generativeai as genai
from json_from_reports import generate_json_for_reports

# Configure the AI model
genai.configure(api_key="AIzaSyDbh0mLOlOMwOb5ft9i63ol7KZIg4iBXGQ")
model = genai.GenerativeModel('gemini-1.5-flash-002')

# Define base paths
base_path = r"D:\llm_exam\next_steps\LANGGRAPH"
resources_folder = os.path.join(base_path, "Resources")
output_folder = os.path.join(base_path, "Partial", "evaluation_reports")
os.makedirs(output_folder, exist_ok=True)

# Load files into placeholders from the "Resources" folder
files_to_load = ["prompt.md", "model_solution.py", "problem_statement.md", "rubric.md", "report_format.md"]
file_contents = {}

for file_name in files_to_load:
    file_path = os.path.join(resources_folder, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        file_contents[file_name] = f.read()

# Extract relevant information from loaded files
evaluation_prompt_template = file_contents["prompt.md"]
model_solution = file_contents["model_solution.py"]
problem_statement = file_contents["problem_statement.md"]
rubric = file_contents["rubric.md"]
report_format = file_contents["report_format.md"]

# Split rubric into modules
rubric_sections = rubric.split("---")

# Get student solution paths from the "Resources" folder containing student submissions
submission_folder = os.path.join(resources_folder, "11601001325_CS F441_AUG_2024-Mid-sem exam submission-42941")
student_folders = glob.glob(os.path.join(submission_folder, "*_assignsubmission_file_"))

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

**RUBRIC (General Instructions):**
{rubric_general}

**MODEL SOLUTION:**
{model_solution}

**STUDENT SOLUTION:**
{student_solution}
"""

module_prompt_template = """
### RUBRIC MODULE: {rubric_module}

{rubric_section}

{student_solution}
"""

# Generate reports for each student
for student_folder in tqdm(student_folders):
    # Extract the student ID from the folder name
    student_folder_name = os.path.basename(student_folder)
    student_id = student_folder_name.split('_')[1]

    # Get the student solution files (searching for both .py and .ipynb files recursively)
    solution_files = glob.glob(os.path.join(student_folder, "**/*.py"), recursive=True) + \
                     glob.glob(os.path.join(student_folder, "**/*.ipynb"), recursive=True)

    if not solution_files:
        continue

    # Assuming there's only one solution file per student, otherwise consider iterating through all
    solution_path = solution_files[0]

    with open(solution_path, 'r', encoding='utf-8', errors='ignore') as f:
        student_solution = f.read()

    # Pass the general rubric and instructions first
    rubric_general = rubric_sections[0]
    final_prompt = combined_prompt_template.format(
        evaluation_prompt_template=evaluation_prompt_template,
        report_format=report_format,
        problem_statement=problem_statement,
        rubric_general=rubric_general,
        model_solution=model_solution,
        student_solution=student_solution
    )

    # Generate initial evaluation using Gemini model
    evaluation_result = model.generate_content([final_prompt])

    # Save the generated evaluation to a list
    module_evaluations = [evaluation_result.text]

    # Evaluate each module separately
    for idx, rubric_section in enumerate(rubric_sections[1:], start=1):
        module_prompt = module_prompt_template.format(
            rubric_module=f"Module {idx}",
            rubric_section=rubric_section.strip(),
            student_solution=student_solution
        )
        module_result = model.generate_content([module_prompt])
        module_evaluations.append(module_result.text)

    # Combine all module evaluations into a single report
    full_report = "\n\n".join(module_evaluations)

    # Save the report to the output folder
    output_name = f"{student_id}_evaluation_report.md"
    output_path = os.path.join(output_folder, output_name)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_report)

print("Generating JSON for reports...")
generate_json_for_reports(output_folder, "lg_students_scores_partial.json")
print("JSON generation completed successfully!")