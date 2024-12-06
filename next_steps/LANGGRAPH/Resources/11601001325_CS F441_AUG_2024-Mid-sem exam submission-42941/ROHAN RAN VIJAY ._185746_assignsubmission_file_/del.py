import openai

# Function to calculate sum of marks from a comma-separated list
# Function to calculate sum of marks from a comma-separated list
def sum_marks(mark_list):
    """
    This function takes a string of comma-separated marks,
    splits them into a list of integers, and returns the sum.
    Handles cases where the input contains invalid entries.
    """
    try:
        # Split the mark list by commas and convert to integers, ignoring invalid entries
        marks = [int(mark.strip()) for mark in mark_list.split(',') if mark.strip().isdigit()]
        return sum(marks)
    except ValueError:
        # Return 0 if there is an error in conversion
        return 0


# Ask the user to provide the OpenAI API key
openai.api_key = input("Enter your OpenAI API key: ")

# Base Node class (LangGraph emulation)
class Node:
    def run(self, state):
        raise NotImplementedError("Each node must implement the run method.")

# ClassExtractionNode: Extracts classes from student code and model solution
class ClassExtractionNode(Node):
    def run(self, state):
        student_code = state['student_code']
        model_solution = state['model_solution']
        
        # Extract classes from student and model code
        student_classes = self.extract_classes(student_code, "student")
        model_classes = self.extract_classes(model_solution, "model")
        
        # Store the extracted classes in state
        state['student_classes'] = student_classes
        state['model_classes'] = model_classes
        return state

    def extract_classes(self, code, source_type):
        prompt = f"Extract all class definitions from the following {source_type} Java code:\n{code}"
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an expert Java developer."},
                  {"role": "user", "content": prompt}]
    )
    
        # Parse the response to create a dictionary of classes
        classes = response['choices'][0]['message']['content'].strip().splitlines()
        class_dict = {}
    
        for class_code in classes:
            class_code = class_code.strip()  # Strip whitespace
            if class_code:  # Check if the line is not empty
                parts = class_code.split()
                if len(parts) > 1 and parts[0] == "class":  # Check for valid class declaration
                    class_name = parts[1]  # Assuming the class declaration is in the format "class ClassName {"
                    class_dict[class_name] = class_code
    
        return class_dict


# RubricExtractionNode: Extracts rubric details for each class
class RubricExtractionNode(Node):
    def run(self, state):
        rubric = state['rubric']
        student_classes = state['student_classes']
        
        class_rubrics = {}
        
        for class_name in student_classes.keys():
            class_rubrics[class_name] = self.extract_rubric(rubric, class_name)
        
        state['class_rubrics'] = class_rubrics
        return state

    def extract_rubric(self, rubric, class_name):
        prompt = f"Extract the relevant rubric for the class '{class_name}' from the following rubric:\n{rubric}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a grading assistant."},
                      {"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()

# InitialEvaluationNode: Evaluates each class based on rubric and model solution
class InitialEvaluationNode(Node):
    def run(self, state):
        student_classes = state['student_classes']
        model_classes = state['model_classes']
        class_rubrics = state['class_rubrics']
        problem_description = state['problem_description']
        
        evaluations = {}
        
        for class_name in student_classes.keys():
            model_code = model_classes.get(class_name, "")
            rubric = class_rubrics.get(class_name, "")
            evaluations[class_name] = self.evaluate_class(class_name, model_code, rubric, problem_description)
        
        state['initial_evaluations'] = evaluations
        return state

    def evaluate_class(self, class_name, model_code, rubric, problem_description):
        prompt = (f"Evaluate the class '{class_name}' in detail. Compare it against the model class:\n{model_code}\n"
                  f"using the following rubric:\n{rubric}\n"
                  f"and the problem description:\n{problem_description}\n"
                  "Provide detailed comments including:\n"
                  "- Correctness of the implementation\n"
                  "- Any errors or mistakes in the code\n"
                  "- Suggestions for improvement\n"
                  "- Marks breakdown for each criterion in the rubric.")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a Java code evaluator."},
                      {"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()


# ReviewEvaluationNode: Reviews and refines the initial evaluations
class ReviewEvaluationNode(Node):
    def run(self, state):
        initial_evaluations = state['initial_evaluations']
        final_evaluations = {}
        
        for class_name, eval_text in initial_evaluations.items():
            final_evaluations[class_name] = self.review_evaluation(eval_text)
        
        state['final_evaluations'] = final_evaluations
        return state

    def review_evaluation(self, eval_text):
        prompt = (f"Review the following evaluation and ensure it contains detailed feedback:\n{eval_text}\n"
                  "Make sure the evaluation includes:\n"
                  "- Detailed correctness analysis\n"
                  "- Identification of errors\n"
                  "- Suggestions for improvement\n"
                  "- Proper marks breakdown for each criterion.")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a Java evaluation reviewer."},
                      {"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()


# MarksExtractionNode: Extracts marks from the final evaluations
class MarksExtractionNode(Node):
    def run(self, state):
        final_evaluations = state['final_evaluations']
        marks_data = {}
        
        for class_name, eval_text in final_evaluations.items():
            marks_data[class_name] = self.extract_marks(eval_text)
            print(f"Extracted marks for {class_name}: {marks_data[class_name]}")  # Debugging statement
        
        state['marks_data'] = marks_data
        return state


    def extract_marks(self, eval_text):
        """
       Extract the step-by-step marks awarded for each criterion from the evaluation text.
        Handles cases where marks are presented in different formats.
       """
        prompt = f"Extract the step-by-step marks awarded for each criterion in this evaluation:\n{eval_text}"
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an expert at extracting grades."},
                  {"role": "user", "content": prompt}]
        )
    
       # Assuming the response provides a comma-separated string of marks
        marks_str = response['choices'][0]['message']['content'].strip()
    
        # Debugging statement to see the extracted marks
        print(f"Extracted marks: {marks_str}")
    
        return marks_str


# TotalMarksCalculationNode: Calculates total marks from extracted marks
class TotalMarksCalculationNode(Node):
    def run(self, state):
        marks_data = state['marks_data']
        total_marks = 0
        
        for class_name, marks_str in marks_data.items():
            total_marks += sum_marks(marks_str)
        
        state['total_marks'] = total_marks
        return state

# FinalOutputNode: Produces the final output including evaluations and total marks
class FinalOutputNode(Node):
    def run(self, state):
        final_evaluations = state['final_evaluations']
        total_marks = state['total_marks']
        evaluation_template = state['evaluation_template']
        
        # Initialize output with the evaluation template structure
        output = evaluation_template
        
        # Fill in the evaluations for each class
        for class_name, eval_text in final_evaluations.items():
            evaluation_section = f"\nClass {class_name} Evaluation:\n{eval_text}\n\n"
            output += evaluation_section
        
        # Append the total marks to the output
        output += f"Total Marks: {total_marks}\n"
        
        # Write the output to a file
        with open("final_evaluations.txt", "w") as f:
            f.write(output)
        
        return state


# Define the Workflow class to manage nodes
class Workflow:
    def __init__(self, nodes, initial_state):
        self.nodes = nodes
        self.state = initial_state

    def run(self):
        for node in self.nodes:
            self.state = node.run(self.state)

# Main workflow definition
def main():
    # Load all input files
    with open("student_code.java", "r") as f:
        student_code = f.read()
    
    with open("model_solution.java", "r") as f:
        model_solution = f.read()
    
    with open("rubric.txt", "r") as f:
        rubric = f.read()
    
    with open("problem_description.txt", "r") as f:
        problem_description = f.read()
    
    with open("evaluation.txt", "r") as f:
        evaluation_template = f.read()

    # Define the LangGraph workflow
    workflow = Workflow(
        nodes=[
            ClassExtractionNode(),
            RubricExtractionNode(),
            InitialEvaluationNode(),
            ReviewEvaluationNode(),
            MarksExtractionNode(),
            TotalMarksCalculationNode(),
            FinalOutputNode()
        ],
        initial_state={
            'student_code': student_code,
            'model_solution': model_solution,
            'rubric': rubric,
            'problem_description': problem_description,
            'evaluation_template': evaluation_template
        }
    )

    # Run the workflow
    workflow.run()

# Execute the main function
if __name__ == "__main__":
    main()
