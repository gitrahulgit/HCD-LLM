import os
import re
import json
from glob import glob
from tqdm import tqdm

def parse_report(report_path):
    """
    Parse a single report file and extract marks and details for each module and submodule.

    Parameters:
        report_path (str): Path to the report file.

    Returns:
        dict: A dictionary with parsed data.
    """
    # Extract student ID from the filename
    student_id = os.path.basename(report_path).split('_')[0]

    with open(report_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Extract overall marks
    overall_marks_match = re.search(r"\*\*Overall Marks:\*\* (\d+)/50", content)
    overall_marks = int(overall_marks_match.group(1)) if overall_marks_match else 0

    # Initialize student data structure
    student_data = {
        "Student ID": student_id,
        "Overall Marks": overall_marks,
        "modules": {}
    }

    # Define patterns for modules and submodules
    module_patterns = {
        "1. Extract Class Method": r"#### 1\. Extract Class Method \[(\d+)/6\]",
        "1.1. Prompt Design": r"\*\*1\.1\. Prompt Design \[(\d+)/3\]:",
        "1.2. Parsing/Output Extraction": r"\*\*1\.2\. Parsing/Output Extraction \[(\d+)/2\]:",
        "1.3. State Saving": r"\*\*1\.3\. State Saving \[(\d+)/1\]:",

        "2. Extract Rubric Method": r"#### 2\. Extract Rubric Method \[(\d+)/6\]",
        "2.1. Prompt Design": r"\*\*2\.1\. Prompt Design \[(\d+)/3\]:",
        "2.2. Parsing/Output Extraction": r"\*\*2\.2\. Parsing/Output Extraction \[(\d+)/2\]:",
        "2.3. State Saving": r"\*\*2\.3\. State Saving \[(\d+)/1\]:",

        "3. Initial Evaluation Method": r"#### 3\. Initial Evaluation Method \[(\d+)/6\]",
        "3.1. Prompt Design": r"\*\*3\.1\. Prompt Design \[(\d+)/3\]:",
        "3.2. Parsing/Output Extraction": r"\*\*3\.2\. Parsing/Output Extraction \[(\d+)/2\]:",
        "3.3. State Saving": r"\*\*3\.3\. State Saving \[(\d+)/1\]:",

        "4. Review Evaluation Method": r"#### 4\. Review Evaluation Method \[(\d+)/6\]",
        "4.1. Prompt Design": r"\*\*4\.1\. Prompt Design \[(\d+)/3\]:",
        "4.2. Parsing/Output Extraction": r"\*\*4\.2\. Parsing/Output Extraction \[(\d+)/2\]:",
        "4.3. State Saving": r"\*\*4\.3\. State Saving \[(\d+)/1\]:",

        "5. Marks Extraction Method": r"#### 5\. Marks Extraction Method \[(\d+)/6\]",
        "5.1. Prompt Design": r"\*\*5\.1\. Prompt Design \[(\d+)/3\]:",
        "5.2. Parsing/Output Extraction": r"\*\*5\.2\. Parsing/Output Extraction \[(\d+)/2\]:",
        "5.3. State Saving": r"\*\*5\.3\. State Saving \[(\d+)/1\]:",

        "6. Total Marks Calculation Method": r"#### 6\. Total Marks Calculation Method \[(\d+)/6\]",
        "6.1. Prompt Design": r"\*\*6\.1\. Prompt Design \[(\d+)/3\]:",
        "6.2. Parsing/Output Extraction": r"\*\*6\.2\. Parsing/Output Extraction \[(\d+)/2\]:",
        "6.3. State Saving": r"\*\*6\.3\. State Saving \[(\d+)/1\]:",

        "7. Graph Construction": r"#### 7\. Graph Construction \[(\d+)/14\]",
        "7.1. Correct Addition of Nodes to the Graph": r"\*\*7\.1\. Correct Addition of Nodes to the Graph \[(\d+)/5\]:",
        "7.2. Correct Addition of Edges to the Graph": r"\*\*7\.2\. Correct Addition of Edges to the Graph \[(\d+)/5\]:",
        "7.3. Correct Compilation of Graph": r"\*\*7\.3\. Correct Compilation of Graph \[(\d+)/4\]:"
    }

    # Extract module and submodule scores
    for module, pattern in module_patterns.items():
        match = re.search(pattern, content)
        if match:
            score = int(match.group(1))
            student_data["modules"][module] = {"total": score}

    return student_data


def generate_json_for_reports(report_folder, output_json):
    """
    Process all reports in a folder and generate a consolidated JSON.

    Parameters:
        report_folder (str): Folder containing the report files.
        output_json (str): Path to the output JSON file.
    """
    # Check if the JSON file exists
    if os.path.exists(output_json):
        with open(output_json, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
    else:
        data = []

    # Determine the next iteration number
    next_iteration_number = len(data) + 1

    # Collect all markdown reports
    report_files = glob(os.path.join(report_folder, "*.md"))
    report_files.sort(key=lambda x: int(os.path.basename(x).split('_')[0]))  # Sort by student ID

    # Parse reports and collect data
    iteration_data = {
        "iterationNumber": next_iteration_number,
        "students": []
    }

    for report_path in tqdm(report_files, desc="Processing Reports"):
        student_data = parse_report(report_path)
        iteration_data["students"].append(student_data)

    # Append the new iteration data
    data.append(iteration_data)

    # Write back to the JSON file
    with open(output_json, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"JSON data updated successfully at {output_json}")


# Example Usage
if __name__ == "__main__":
    report_folder = r"D:\llm_exam\next_steps\LANGGRAPH\Complete\evaluation_reports"  # Replace with the actual folder path
    output_json = "lg_students_scores.json"  # Desired output JSON file name
    generate_json_for_reports(report_folder, output_json)
