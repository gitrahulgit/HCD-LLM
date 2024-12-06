# Import necessary libraries
from langgraph import LangGraph, Node, Edge
import json
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Function to call the GPT-4.0 Mini model
def get_gpt_feedback(prompt):
    """
    Call the GPT-4.0 Mini model with the given prompt and return the response.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

# Class Extraction Module
class ExtractionNode(Node):
    def run(self, model_solution, student_submission):
        model_structure = self.extract_structure(model_solution)
        student_structure = self.extract_structure(student_submission)
        return model_structure, student_structure

    def extract_structure(self, java_file):
        # Logic to extract class and method structure from the Java file
        structure = {"class_name": "ExampleClass", "methods": ["method1", "method2"]}
        return structure


# Rubric Extraction Module
class RubricExtractionNode(Node):
    def run(self, rubric_file):
        rubric = self.extract_rubric(rubric_file)
        return rubric

    def extract_rubric(self, rubric_file):
        with open(rubric_file, 'r') as file:
            rubric = json.load(file)
        return rubric


# Initial Evaluation Module
class InitialEvaluationNode(Node):
    def run(self, student_structure, model_structure, rubric):
        feedback, marks = self.initial_evaluate(student_structure, model_structure, rubric)
        return feedback, marks

    def initial_evaluate(self, student_structure, model_structure, rubric):
        feedback = []
        marks = 0
        # Compare student structure with model structure using the rubric
        if student_structure == model_structure:
            feedback.append("Class and methods match the model solution.")
            marks += rubric["correct_structure_points"]
        else:
            feedback.append("Class or methods do not match the model solution.")
        return feedback, marks


# Review Evaluation Module
class ReviewEvaluationNode(Node):
    def run(self, feedback, marks):
        final_feedback, adjusted_marks = self.review_evaluate(feedback, marks)
        return final_feedback, adjusted_marks

    def review_evaluate(self, feedback, marks):
        # Generate detailed feedback using GPT-4.0 Mini
        gpt_prompt = "Provide detailed feedback for the following evaluation: \n" + "\n".join(feedback)
        gpt_feedback = get_gpt_feedback(gpt_prompt)
        
        final_feedback = feedback + [gpt_feedback, "TA review completed."]
        adjusted_marks = marks + 2  # Example of adjustment
        return final_feedback, adjusted_marks


# Marks Extraction Module
class MarksExtractionNode(Node):
    def run(self, adjusted_marks):
        extracted_marks = self.extract_marks(adjusted_marks)
        return extracted_marks

    def extract_marks(self, adjusted_marks):
        # Logic to extract the marks after evaluation
        return adjusted_marks


# Total Marks Computation Module (with sum_marks)
class TotalMarksComputationNode(Node):
    def run(self, extracted_marks):
        total_marks = self.compute_total_marks(extracted_marks)
        return total_marks

    def sum_marks(self, marks_list):
        """
        Takes a comma-separated list of marks and returns their sum.
        """
        try:
            marks = [int(mark.strip()) for mark in marks_list.split(",")]
            return sum(marks)
        except ValueError:
            raise ValueError("Invalid marks provided. Ensure all marks are integers.")
    
    def compute_total_marks(self, adjusted_marks):
        """
        Compute the total marks by using sum_marks on the adjusted marks.
        """
        # Convert the list of marks into a comma-separated string and sum them
        marks_string = ",".join(map(str, adjusted_marks))
        total_marks = self.sum_marks(marks_string)
        return total_marks


# Workflow Definition
def build_workflow():
    graph = LangGraph()

    # Define the nodes
    extraction_node = ExtractionNode("Class Extraction")
    rubric_extraction_node = RubricExtractionNode("Rubric Extraction")
    initial_eval_node = InitialEvaluationNode("Initial Evaluation")
    review_eval_node = ReviewEvaluationNode("Review Evaluation")
    marks_extraction_node = MarksExtractionNode("Marks Extraction")
    total_marks_computation_node = TotalMarksComputationNode("Total Marks Computation")

    # Add nodes to the graph
    graph.add_node(extraction_node)
    graph.add_node(rubric_extraction_node)
    graph.add_node(initial_eval_node)
    graph.add_node(review_eval_node)
    graph.add_node(marks_extraction_node)
    graph.add_node(total_marks_computation_node)

    # Define the edges (transitions between nodes)
    graph.add_edge(Edge(extraction_node, rubric_extraction_node, label="Class Structure Extracted"))
    graph.add_edge(Edge(rubric_extraction_node, initial_eval_node, label="Rubric Extracted"))
    graph.add_edge(Edge(initial_eval_node, review_eval_node, label="Initial Evaluation Done"))
    graph.add_edge(Edge(review_eval_node, marks_extraction_node, label="Review Evaluation Done"))
    graph.add_edge(Edge(marks_extraction_node, total_marks_computation_node, label="Marks Extracted"))

    return graph




# Main function to run the workflow
def main():
    # Input files (replace with actual file paths in real implementation)
    problem_description = "input/problem_description.txt"
    model_solution = "input/model_solution.java"
    rubric_file = "input/rubric.json"
    student_submission = "input/student_submission.java"
    output_file = "final_evaluations.txt"

    # Load the rubric
    with open(rubric_file, 'r') as file:
        rubric = json.load(file)

    # Read the student's code for feedback generation
    with open(student_submission, 'r') as student_file:
        student_code = student_file.read()

    # Build the graph workflow
    graph = build_workflow()

    # Step-by-step execution
    initial_node = graph.get_node("Class Extraction")
    model_structure, student_structure = initial_node.run(model_solution, student_submission)

    rubric_node = graph.get_node("Rubric Extraction")
    rubric = rubric_node.run(rubric_file)

    initial_eval_node = graph.get_node("Initial Evaluation")
    feedback, marks = initial_eval_node.run(student_structure, model_structure, rubric)

    review_eval_node = graph.get_node("Review Evaluation")
    final_feedback, adjusted_marks = review_eval_node.run(feedback, marks)

    marks_extraction_node = graph.get_node("Marks Extraction")
    extracted_marks = marks_extraction_node.run(adjusted_marks)

    total_marks_node = graph.get_node("Total Marks Computation")
    total_marks = total_marks_node.run(extracted_marks)

    # Save the detailed feedback and total marks to a file
    with open(output_file, 'w') as output:
        output.write("Detailed Evaluation Feedback:\n")
        output.write("\n".join(final_feedback))
        output.write(f"\n\nTotal Marks Obtained: {total_marks}")

    print(f"Total marks for the student: {total_marks}")
    print(f"Evaluation saved to {output_file}")

# Run the main function
main()