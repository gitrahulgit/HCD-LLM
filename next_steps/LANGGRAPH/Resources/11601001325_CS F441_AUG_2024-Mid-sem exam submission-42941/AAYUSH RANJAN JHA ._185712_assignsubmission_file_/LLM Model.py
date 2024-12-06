# agent_system.py

from openai import OpenAI
import os

# Set up OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define the LangGraph-like framework (simplified for this implementation)
class State:
    def __init__(self):
        self.data = {}

class Node:
    def __init__(self, func):
        self.func = func

    def run(self, state):
        self.func(state)

# Define each module as a function
def class_extraction_module(state):
    # Read instructor's and student's code
    with open('model_solution.md', 'r') as f:
        instructor_code = f.read()
    with open('student_solution.md', 'r') as f:
        student_code = f.read()

    # Extract classes using GPT-3.5-turbo
    prompt = f"Extract all Java classes from the following code:\n\n{student_code}\n\nReturn each class separately."
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt}]
    )
    student_classes = response.choices[0].message.content

    prompt = f"Extract all Java classes from the following code:\n\n{instructor_code}\n\nReturn each class separately."
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt}]
    )
    instructor_classes = response.choices[0].message.content

    # Store in state
    state.data['student_classes'] = student_classes
    state.data['instructor_classes'] = instructor_classes

def rubric_extraction_module(state):
    # Read rubric
    with open('rubric.md', 'r') as f:
        rubric = f.read()

    # Extract rubric details for each class
    prompt = f"Extract rubric details for each Java class from the following rubric:\n\n{rubric}\n\nReturn in a structured format."
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt}]
    )
    rubric_details = response.choices[0].message.content

    # Store in state
    state.data['rubric_details'] = rubric_details

def initial_evaluation_module(state):
    student_classes = state.data['student_classes']
    instructor_classes = state.data['instructor_classes']
    rubric_details = state.data['rubric_details']

    # Evaluate each class
    prompt = f"""
Evaluate the following student classes against the rubric and model solution.

For each criterion in the rubric, provide:
- The numeric score awarded.
- Detailed comments about correctness, errors, and suggestions for improvement in the student's code.

Student Classes:
{student_classes}

Instructor Classes:
{instructor_classes}

Rubric Details:
{rubric_details}
"""
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt.strip()}]
    )
    initial_evaluation = response.choices[0].message.content

    # Store in state
    state.data['initial_evaluation'] = initial_evaluation

def review_evaluation_module(state):
    initial_evaluation = state.data['initial_evaluation']

    # Review and correct initial evaluation
    prompt = f"Review the following initial evaluation and make corrections as needed. Provide the final assessment for each Java class, including numeric scores and detailed comments.\n\n{initial_evaluation}"
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt}]
    )
    final_evaluation = response.choices[0].message.content

    # Store in state
    state.data['final_evaluation'] = final_evaluation

def marks_extract_module(state):
    final_evaluation = state.data['final_evaluation']

    # Extract marks
    prompt = f"From the following evaluation, extract the numeric scores awarded for each criterion as a comma-separated list per class.\n\n{final_evaluation}"
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt}]
    )
    marks_list = response.choices[0].message.content

    # Store in state
    state.data['marks_list'] = marks_list

def sum_marks(marks_list):
    # Sum up the marks
    total = 0
    for marks in marks_list.split(','):
        try:
            total += float(marks.strip())
        except ValueError:
            continue
    return total

def total_marks_calculation_module(state):
    marks_list = state.data['marks_list']

    # Calculate total marks
    total_marks = sum_marks(marks_list)

    # Store in state
    state.data['total_marks'] = total_marks

def output_module(state):
    final_evaluation = state.data['final_evaluation']
    total_marks = state.data['total_marks']

    # Write to final_evaluation.txt
    with open('final_evaluation.txt', 'w') as f:
        f.write(f"{final_evaluation}\n\nTotal Grade: {total_marks}")

# Create nodes
nodes = [
    Node(class_extraction_module),
    Node(rubric_extraction_module),
    Node(initial_evaluation_module),
    Node(review_evaluation_module),
    Node(marks_extract_module),
    Node(total_marks_calculation_module),
    Node(output_module)
]

# Run the workflow
def main():
    state = State()
    for node in nodes:
        node.run(state)

if __name__ == '__main__':
    main()
