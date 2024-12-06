from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langgraph.graph import StateGraph
from typing import Dict, TypedDict, List, Annotated
from langchain.schema import runnable
import os
import json

load_dotenv()

llm = OpenAI(temperature=0,api_key="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")

class EvaluationInput(TypedDict):
    problem_description: str
    model_solution: str
    rubric: str
    student_submission: str

class EvaluationOutput(TypedDict):
    extracted_classes: Dict[str, str]
    class_evaluations: Dict[str, Dict[str, float]]
    detailed_feedback: Dict[str, str]
    total_score: float

def extract_classes(state:Dict)->Dict:
    student_submission = state['student_submission']
    class_extraction_prompt = PromptTemplate(
        input_variables=["code"],
        template="""
You are to extract Java class definitions from the following code and output them in a specific JSON format.

Input Code:
{code}

Instructions:
- For each Java class in the input code, extract its class name and the complete class code.
- **Do not include any extra text, explanations, numbering, or formatting.**
- Output a single JSON object where:
  - Each key is the class name (as a string).
  - Each value is a string containing the complete code of the class, exactly as it appears in the input.

**Example Output:**
{{
  "ClassName1": "class code...",
  "ClassName2": "class code..."
}}
"""
    )
    class_extraction_chain = class_extraction_prompt | llm
    extracted_classes = class_extraction_chain.invoke({"code": student_submission})
    print("LLM Output for extracted_classes:")
    print(extracted_classes)
    extracted_classes_dict = json.loads(extracted_classes)
    state['extracted_classes'] = extracted_classes_dict
    return state

def extract_rubric_details(state):
    extracted_classes = state['extracted_classes']
    rubric = state['rubric']
    rubric_extraction_prompt = PromptTemplate(
        input_variables=["rubric", "class_name"],
        template="""
Given the following rubric:

{rubric}

Extract the relevant rubric details for the Java class named '{class_name}'. Output the result as a JSON object where each key is a criterion and the value is the maximum score for that criterion.
"""
    )
    rubric_extraction_chain = LLMChain(llm=llm, prompt=rubric_extraction_prompt)
    
    class_rubrics = {}
    for class_name in extracted_classes:
        class_rubric = rubric_extraction_chain.run(rubric=rubric, class_name=class_name)
        class_rubrics[class_name] = json.loads(class_rubric)
    
    state['class_rubrics'] = class_rubrics
    return state

def evaluate_class(state):
    extracted_classes = state['extracted_classes']
    class_rubrics = state['class_rubrics']
    model_solution = state['model_solution']
    evaluation_prompt = PromptTemplate(
        input_variables=["class_code", "rubric_details", "model_solution"],
        template="""
Evaluate the following Java class based on the given rubric and model solution:

Class Code:
{class_code}

Rubric:
{rubric_details}

Model Solution:
{model_solution}

Provide a detailed evaluation including:
1. Numeric scores for each criterion
2. Detailed comments about correctness, errors, and suggestions for improvement

Output the result as a JSON object with two keys: 'scores' (a dictionary of criterion: score pairs) and 'feedback' (a string with detailed comments).
"""
    )
    evaluation_chain = LLMChain(llm=llm, prompt=evaluation_prompt)
    
    class_evaluations = {}
    detailed_feedback = {}
    
    for class_name, class_code in extracted_classes.items():
        rubric_details = json.dumps(class_rubrics[class_name])
        evaluation_result = evaluation_chain.run(
            class_code=class_code,
            rubric_details=rubric_details,
            model_solution=model_solution
        )
        evaluation_dict = json.loads(evaluation_result)
        class_evaluations[class_name] = evaluation_dict["scores"]
        detailed_feedback[class_name] = evaluation_dict["feedback"]
    
    state['class_evaluations'] = class_evaluations
    state['detailed_feedback'] = detailed_feedback
    return state

def review_evaluation(state):
    class_evaluations = state['class_evaluations']
    detailed_feedback = state['detailed_feedback']
    review_prompt = PromptTemplate(
        input_variables=["class_evaluations", "detailed_feedback"],
        template="""
Review the following class evaluations and detailed feedback:

Evaluations: {class_evaluations}

Feedback: {detailed_feedback}

Provide a summary of the evaluation, highlighting any inconsistencies or areas that may need further review. Output the result as a string.
"""
    )
    review_chain = LLMChain(llm=llm, prompt=review_prompt)
    
    review_result = review_chain.run(
        class_evaluations=json.dumps(class_evaluations),
        detailed_feedback=json.dumps(detailed_feedback)
    )
    
    state['review_summary'] = review_result
    return state

def extract_marks(state):
    class_evaluations = state['class_evaluations']
    extracted_marks = {}
    
    for class_name, evaluation in class_evaluations.items():
        extracted_marks[class_name] = sum(evaluation.values())
    
    state['extracted_marks'] = extracted_marks
    return state

def calculate_total_marks(state):
    extracted_marks = state['extracted_marks']
    total_score = sum(extracted_marks.values())
    state['total_score'] = total_score
    return state

def evaluate_submission(inputs: EvaluationInput) -> EvaluationOutput:
    state = {
        'student_submission': inputs['student_submission'],
        'rubric': inputs['rubric'],
        'model_solution': inputs['model_solution']
    }
    
    result_state = app.invoke(state)
    
    return EvaluationOutput(
        extracted_classes=result_state["extracted_classes"],
        class_evaluations=result_state["class_evaluations"],
        detailed_feedback=result_state["detailed_feedback"],
        total_score=result_state["total_score"]
    )

class State(TypedDict):
    student_submission: str
    rubric: str
    model_solution: str
    extracted_classes: Dict[str, str] = None
    class_rubrics: Dict[str, Dict[str, float]] = None
    class_evaluations: Dict[str, Dict[str, float]] = None
    detailed_feedback: Dict[str, str] = None
    extracted_marks: Dict[str, float] = None
    total_score: float = None
    review_summary: str = None

# Initialize the StateGraph with the state schema
graph = StateGraph(State,input=EvaluationInput,output=EvaluationOutput)

# Add nodes to the state graph
graph.add_node("extract_classes", extract_classes)
graph.add_node("extract_rubric_details", extract_rubric_details)
graph.add_node("evaluate_class", evaluate_class)
graph.add_node("review_evaluation", review_evaluation)
graph.add_node("extract_marks", extract_marks)
graph.add_node("calculate_total_marks", calculate_total_marks)
graph.set_entry_point("extract_classes")

# Define the edges (order of execution)
graph.add_edge("extract_classes", "extract_rubric_details")
graph.add_edge("extract_rubric_details", "evaluate_class")
graph.add_edge("evaluate_class", "review_evaluation")
graph.add_edge("evaluate_class", "extract_marks")
graph.add_edge("extract_marks", "calculate_total_marks")

app = graph.compile()

if __name__ == "__main__":
    inputs = EvaluationInput(
        problem_description="""
Implement a Java class called 'Rectangle' that has two private instance variables width and height. Provide appropriate constructors, getters, and setters. Also, include methods to calculate the area and the perimeter of the rectangle.
""",
        model_solution="""
public class Rectangle {
    private double width;
    private double height;

    // Default constructor
    public Rectangle() {
        this.width = 0;
        this.height = 0;
    }

    // Parameterized constructor
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    // Getter and Setter for width
    public double getWidth() { return width; }
    public void setWidth(double width) { this.width = width; }

    // Getter and Setter for height
    public double getHeight() { return height; }
    public void setHeight(double height) { this.height = height; }

    // Method to calculate area
    public double calculateArea() {
        return width * height;
    }

    // Method to calculate perimeter
    public double calculatePerimeter() {
        return 2 * (width + height);
    }
}
""",
        rubric="""
- Class Structure (2 points): The class is named 'Rectangle' and has appropriate access modifiers.
- Instance Variables (2 points): The class has two private instance variables: width and height.
- Constructors (2 points): The class includes a default constructor and a parameterized constructor.
- Getters and Setters (2 points): The class includes getters and setters for both width and height.
- calculateArea Method (1 point): The class includes a method to calculate the area of the rectangle.
- calculatePerimeter Method (1 point): The class includes a method to calculate the perimeter of the rectangle.
- Code Style and Formatting (1 point): The code follows standard Java coding conventions.

Total: 11 points
""",
        student_submission="""
public class Rectangle {
    private double width;
    private double height;

    // Only parameterized constructor
    public Rectangle(double w, double h) {
        width = w;
        height = h;
    }

    // Getter and Setter for width
    public double getWidth() { return width; }
    public void setWidth(double w) { width = w; }

    // Getter and Setter for height
    public double getHeight() { return height; }
    public void setHeight(double h) { height = h; }

    // Method to calculate area (incorrect method name)
    public double area() {
        return width * height;
    }

    // Method to calculate perimeter (incorrect method name)
    public double perimeter() {
        return 2 * (width + height);
    }
}
"""
    )
    result = evaluate_submission(inputs)
    print(result)
