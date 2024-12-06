import langgraph
from langgraph.graph import StateGraph  # Keep StateGraph from langgraph
import openai
import json

# GradingResult class remains unchanged
class GradingResult:
    def __init__(self, scores, comments):
        self.scores = scores
        self.comments = comments

# Custom Node class for the workflow
class Node:
    def __init__(self, name):
        self.name = name
        self.next_node = None

    def set_next_node(self, next_node):
        self.next_node = next_node

    def execute_next(self):
        if self.next_node:
            self.next_node.execute()

class JavaCodeEvaluator:
    def __init__(self, api_key):
        from typing import Dict, Any
from langgraph.graph import StateGraph

class JavaCodeEvaluator:
    def __init__(self, api_key):
        self.language_model_api = openai
        self.language_model_api.api_key = api_key
        
        # Define a proper state schema
        state_schema = {
            "input": str,
            "output": str,
            "intermediate": Dict[str, Any]
        }
        
        self.state_graph = StateGraph(state_schema)

        self.initialize_workflow()
        def class_extraction_node(state):
            # Implement your class extraction logic here
            return {"output": "Extracted classes"}

        def method_extraction_node(state):
            # Implement your method extraction logic here
            return {"output": "Extracted methods"}

        # Add nodes to the graph
        self.state_graph.add_node("class_extraction", class_extraction_node)
        self.state_graph.add_node("method_extraction", method_extraction_node)

        # Add edges if needed
        self.state_graph.add_edge("class_extraction", "method_extraction")

        # Set the entry point
        self.state_graph.set_entry_point("class_extraction")

        # Compile the graph
        self.chain = self.state_graph.compile()
       

    def initialize_workflow(self):
        class_extraction_node = Node("ClassExtraction")
        rubric_extraction_node = Node("RubricExtraction")
        initial_evaluation_node = Node("InitialEvaluation")
        review_evaluation_node = Node("ReviewEvaluation")
        marks_extraction_node = Node("MarksExtraction")
        total_marks_calculation_node = Node("TotalMarksCalculation")

        # Define transitions between nodes
        class_extraction_node.set_next_node(rubric_extraction_node)
        rubric_extraction_node.set_next_node(initial_evaluation_node)
        initial_evaluation_node.set_next_node(review_evaluation_node)
        review_evaluation_node.set_next_node(marks_extraction_node)
        marks_extraction_node.set_next_node(total_marks_calculation_node)

        self.state_graph.add_node(class_extraction_node)
        self.state_graph.add_node(rubric_extraction_node)
        self.state_graph.add_node(initial_evaluation_node)
        self.state_graph.add_node(review_evaluation_node)
        self.state_graph.add_node(marks_extraction_node)
        self.state_graph.add_node(total_marks_calculation_node)

    def evaluate_submission(self, student_code, model_solution, rubric, question):
        self.state_graph.set_state("student_code", student_code)
        self.state_graph.set_state("model_solution", model_solution)
        self.state_graph.set_state("rubric", rubric)
        self.state_graph.set_state("question", question)
        self.state_graph.execute()

    class ClassExtractionNode(Node):
        def execute(self):
            student_code = self.state_graph.get_state("student_code")
            model_solution = self.state_graph.get_state("model_solution")
            student_classes = self.extract_classes(student_code)
            model_classes = self.extract_classes(model_solution)
            self.state_graph.set_state("student_classes", student_classes)
            self.state_graph.set_state("model_classes", model_classes)
            super().execute_next()

        def extract_classes(self, code):
            prompt = f"Extract individual Java classes from the following code: \n{code}"
            response = self.language_model_api.Completion.create(
                engine="text-davinci-003", prompt=prompt, max_tokens=150
            )
            return response.choices[0].text.split("\n")

    class RubricExtractionNode(Node):
        def execute(self):
            rubric = self.state_graph.get_state("rubric")
            prompt = f"Extract key rubric details from the following rubric markdown file: \n{rubric}"
            rubric_details = self.language_model_api.Completion.create(
                engine="text-davinci-003", prompt=prompt, max_tokens=200
            ).choices[0].text.strip().split("\n")
            self.state_graph.set_state("rubric_details", rubric_details)
            super().execute_next()

    class InitialEvaluationNode(Node):
        def execute(self):
            student_classes = self.state_graph.get_state("student_classes")
            rubric_details = self.state_graph.get_state("rubric_details")
            grading_results = []

            for student_class, rubric_detail in zip(student_classes, rubric_details):
                result = self.initial_evaluation(student_class, rubric_detail)
                grading_results.append(result)

            self.state_graph.set_state("grading_results", grading_results)
            super().execute_next()

        def initial_evaluation(self, student_class, rubric_detail):
            model_class = self.find_matching_model_class(student_class)
            prompt = (
                f"Evaluate the following Java class against the rubric and model solution: \n"
                f"Class Code: {student_class}\n"
                f"Rubric: {rubric_detail}\n"
                f"Model Class: {model_class}\n"
                f"Please provide a detailed evaluation, including a numeric score for each criterion, "
                f"comments on correctness, errors found, and suggestions for improvement."
            )
            evaluation_response = self.language_model_api.Completion.create(
                engine="text-davinci-003", prompt=prompt, max_tokens=300
            )
            return self.process_evaluation_response(evaluation_response.choices[0].text)

        def find_matching_model_class(self, student_class):
            # Logic to find the corresponding model class for evaluation
            return ""  # Placeholder for actual matching logic

        def process_evaluation_response(self, response):
            parts = response.split("Comments:")
            score_part = parts[0].strip()
            comments_part = parts[1].strip() if len(parts) > 1 else ""

            # Extract numeric scores
            scores = []
            for part in score_part.split(","):
                part = part.strip()
                if part.isdigit():
                    scores.append(int(part))

            return GradingResult(scores, comments_part.strip())

    class ReviewEvaluationNode(Node):
        def execute(self):
            # Review logic can be implemented here
            super().execute_next()

    class MarksExtractionNode(Node):
        def execute(self):
            grading_results = self.state_graph.get_state("grading_results")
            marks = []

            for result in grading_results:
                marks.extend(result.scores)

            self.state_graph.set_state("marks", marks)
            super().execute_next()

    class TotalMarksCalculationNode(Node):
        def execute(self):
            marks = self.state_graph.get_state("marks")
            total_marks = self.sum_marks(marks)
            self.state_graph.set_state("total_marks", total_marks)
            self.save_final_evaluation(marks, total_marks)

        def sum_marks(self, marks):
            return sum(marks)

        def save_final_evaluation(self, marks, total_marks):
            final_output = {
                "Scores": marks,
                "Total Marks": total_marks
            }
            with open("final_evaluation.txt", "w") as f:
                f.write(json.dumps(final_output, indent=4))

def main():
    api_key = input("Kindly enter here your LLM API Key: ")
    evaluator = JavaCodeEvaluator(api_key)

    # Read from the specified input files
    try:
        with open("student_solution.md", "r") as student_file:
            student_code = student_file.read()

        with open("model_solution.md", "r") as model_file:
            model_solution = model_file.read()

        with open("rubric.md", "r") as rubric_file:
            rubric = rubric_file.read()

        with open("question.md", "r") as question_file:
            question = question_file.read()

        # Pass file contents to the evaluator
        evaluator.evaluate_submission(student_code, model_solution, rubric, question)

    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the input files exist in the current directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
