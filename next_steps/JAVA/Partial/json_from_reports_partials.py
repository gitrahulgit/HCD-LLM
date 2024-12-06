import os
import re
import json
from glob import glob
from tqdm import tqdm


def parse_report(report_path):

    student_id = os.path.basename(report_path).split('_')[1]

    with open(report_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Extract Student ID and Overall Marks
    #student_id = os.path.basename(report_path).split('_')[0]
    overall_marks_match = re.search(r"\*\*Overall Marks:\*\* (\d+)/50", content)
    overall_marks = int(overall_marks_match.group(1)) if overall_marks_match else 0

    # JSON Template for Student Report
    student_data = {
        "Student ID": student_id,
        "Overall Marks": overall_marks,
        "modules": {}
    }

    # Define patterns to extract marks for modules and submodules
    module_patterns = {
        "1. Implementation of Core Functionalities": r"\*\*1\. Implementation of Core Functionalities \((\d+)/25\)\*\*",
        "1.1 Book Management": r"\*\*1\.1 Book Management \((\d+)/10\)\*\*",
        "1.1.1 Add a Book": r"\*\*1\.1\.1 Add a Book \((\d+)/4\)\*\*",
        "1.1.2 Display Available Books": r"\*\*1\.1\.2 Display Available Books \((\d+)/3\)\*\*",
        "1.1.3 Update Book Details": r"\*\*1\.1\.3 Update Book Details \((\d+)/3\)\*\*",
        "1.2 Borrower Management": r"\*\*1\.2 Borrower Management \((\d+)/7\)\*\*",
        "1.2.1 Register Borrower": r"\*\*1\.2\.1 Register Borrower \((\d+)/4\)\*\*",
        "1.2.2 View Borrower History": r"\*\*1\.2\.2 View Borrower History \((\d+)/3\)\*\*",
        "1.3 Transaction Handling": r"\*\*1\.3 Transaction Handling \((\d+)/8\)\*\*",
        "1.3.1 Borrow Book": r"\*\*1\.3\.1 Borrow Book \((\d+)/5\)\*\*",
        "1.3.2 Return Book": r"\*\*1\.3\.2 Return Book \((\d+)/3\)\*\*",
        "2. Use of OOP Principles": r"\*\*2\. Use of OOP Principles \((\d+)/10\)\*\*",
        "2.1 Classes and Objects": r"\*\*2\.1 Classes and Objects \((\d+)/3\)\*\*",
        "2.2 Inheritance": r"\*\*2\.2 Inheritance \((\d+)/3\)\*\*",
        "2.3 Polymorphism": r"\*\*2\.3 Polymorphism \((\d+)/2\)\*\*",
        "2.4 Encapsulation": r"\*\*2\.4 Encapsulation \((\d+)/2\)\*\*",
        "3. Exception Handling": r"\*\*3\. Exception Handling \((\d+)/5\)\*\*",
        "3.1 Use of Try-Catch Blocks": r"\*\*3\.1 Use of Try-Catch Blocks \((\d+)/2\)\*\*",
        "3.2 Custom Exception Class": r"\*\*3\.2 Custom Exception Class \((\d+)/2\)\*\*",
        "3.3 Edge Case Handling": r"\*\*3\.3 Edge Case Handling \((\d+)/1\)\*\*",
        "4. File I/O Implementation": r"\*\*4\. File I/O Implementation \((\d+)/5\)\*\*",
        "4.1 Save Data": r"\*\*4\.1 Save Data \((\d+)/2\)\*\*",
        "4.2 Load Data": r"\*\*4\.2 Load Data \((\d+)/2\)\*\*",
        "4.3 File Handling Robustness": r"\*\*4\.3 File Handling Robustness \((\d+)/1\)\*\*",
        "5. Code Efficiency and Quality": r"\*\*5\. Code Efficiency and Quality \((\d+)/5\)\*\*",
        "5.1 Efficient Algorithms": r"\*\*5\.1 Efficient Algorithms \((\d+)/3\)\*\*",
        "5.2 Adherence to Java Naming Conventions": r"\*\*5\.2 Adherence to Java Naming Conventions \((\d+)/2\)\*\*",
        "6. Code Formatting": r"\*\*6\. Code Formatting \((\d+)/5\)\*\*",
        "6.1 Code Readability and Indentation": r"\*\*6\.1 Code Readability and Indentation \((\d+)/5\)\*\*"
    }

    # Parse module and submodule scores
    for module, pattern in module_patterns.items():
        match = re.search(pattern, content)
        if match:
            score = int(match.group(1))
            if "submodules" not in student_data["modules"].get(module.split()[0], {}):
                student_data["modules"][module] = {"total": score}
            else:
                student_data["modules"][module]["submodules"] = score

    return student_data


def generate_json_for_reports(report_folder, output_json):

    # Check if the JSON file exists
    if os.path.exists(output_json):
        with open(output_json, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
    else:
        data = []

    # Determine the next iteration number
    next_iteration_number = len(data) + 1

    # Collect all markdown reports
    report_files = glob(os.path.join(report_folder, "student_*_report.md"))
    report_files.sort(key=lambda x: int(os.path.basename(x).split('_')[1]))


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
    report_folder = r"D:\llm_exam\next_steps\JAVA\Partial\evaluation_reports"  # Replace with the actual folder containing markdown reports
    output_json = "java_students_scores_partial.json"  # Replace with desired JSON file name
    generate_json_for_reports(report_folder, output_json)
    