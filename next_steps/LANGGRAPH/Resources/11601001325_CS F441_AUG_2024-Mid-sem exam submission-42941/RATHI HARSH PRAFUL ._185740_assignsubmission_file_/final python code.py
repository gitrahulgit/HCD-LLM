import getpass
import os
from typing import List, Tuple
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain.schema import HumanMessage
from langgraph.graph import END, StateGraph, START
from pprint import pprint

# Function to set environment variables securely
def _set_env(key: str):
    if key not in os.environ:
        os.environ[key] = getpass.getpass(f"{key}:")

_set_env("OPENAI_API_KEY")


class RubricMappingEntry(BaseModel):
    student_code_piece: str = Field(
        ...,
        description="A specific part of the student's code."
    )
    rubric_section: str = Field(
        ...,
        description="The corresponding section of the rubric, also include the marks for each section and capture the total decscription from the rubric here"
    )
    model_answer_key: str = Field(
        ...,
        description="The code from the model answer, corresponding to the rubric sectiona nd the student_code_piece"
    )

class RubricMapping(BaseModel):
    mappings: List[RubricMappingEntry] = Field(
        ...,
        description="List of rubric mapping entries each containing student code piece, rubric section, and model answer key."
    )

class AgentState(TypedDict):
    messages: List[AnyMessage]  # For logging LLM interactions or other details
    student_code: str           # To store the student's code submission
    model_solution: str         # To store the instructor's model solution
    class_mappings: List[Tuple[str, str]]  # List of (student_class, model_class) tuples
    rubric: str                 # To store the rubric for the exam
    rubric_mapping: List[RubricMappingEntry]  # Updated rubric mapping entries
    student_classes: List[str]  # List of student's classes
    model_classes: List[str]    # List of model's classes
    evaluation: dict            # To store evaluation results
    total_marks: int            # To store the total marks calculated
    final_assessment:dict

# Initialize the LLM model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Data model for structured class extraction output
class ClassExtraction(BaseModel):
    classes: List[str] = Field(description="A list of classes with their names and corresponding code blocks.")

# Prompt template for extracting class names and code blocks
class_extraction_prompt = PromptTemplate(
    template="""
    Extract the class names and corresponding code blocks from the following Java code.

    Student code:
    {student_code}

    Model solution:
    {model_solution}

    Ensure that the class names in the student submission match those in the model solution.

    Return the classes and their code blocks in a structured form, where each class is represented as a string in the format: "ClassName: <class_code>".
    """,
    input_variables=["student_code", "model_solution"]
)

# Prompt template for generating rubric mapping
rubric_prompt = PromptTemplate(
    template="""You are a grader matching student code to a grading rubric. 
    Here is the student's code: 

    {code} 

    Here is the rubric, also include the total marks in the rubric, we will need that for grading later on: 

    {rubric} 

    Here is the model answer key:

    {model_answer_key}

    Match each part of the student's code (like class names or functions) with the most appropriate section of the rubric.
    Provide structured output in the form of a list of objects containing the student code piece, the corresponding rubric section, and the model answer key.
    """,
    input_variables=["code", "rubric", "model_answer_key"]
)

# Initialize LLM with structured output for class extraction
llm_with_structured_output = model.with_structured_output(ClassExtraction)

# Function to extract class names and code blocks
def class_extraction_node(state: AgentState):
    # Prepare the input data
    student_code = state['student_code']
    model_solution = state['model_solution']
    
    # Run LLM with the prompt and structured output for student classes
    student_chain = class_extraction_prompt | llm_with_structured_output
    student_output = student_chain.invoke({"student_code": student_code, "model_solution": ""})
    
    # Run LLM with the prompt and structured output for model classes
    model_chain = class_extraction_prompt | llm_with_structured_output
    model_output = model_chain.invoke({"student_code": "", "model_solution": model_solution})
    
    # Extract the classes from the LLM responses
    student_classes = [cls for cls in student_output.classes]
    model_classes = [cls for cls in model_output.classes]
    
    # Ensure class names match between student and model
    # if sorted(student_classes) != sorted(model_classes):
    #     state['evaluation'] = {"error": "Class names do not match between student submission and model solution."}
    #     return state
    
    # Update state with extracted class information
    state['student_classes'] = student_classes
    state['model_classes'] = model_classes
    
    return state

# Initialize LLM with structured output for rubric mapping
llm_rubric_with_structured_output = model.with_structured_output(RubricMapping)

# Function to extract rubric mappings dynamically using LLM
def rubric_extraction_module(state: AgentState):
    # Prepare the input data
    code = state["student_code"]
    rubric = state["rubric"]
    model_answer_key = state["model_solution"]  # Assuming model_solution contains the answer key

    # Run LLM with the prompt and structured output format
    chain = rubric_prompt | llm_rubric_with_structured_output
    structured_output = chain.invoke({
        "code": code,
        "rubric": rubric,
        "model_answer_key": model_answer_key
    })

    # Update the state with the structured output (student_code_piece, rubric_section, model_answer_key)
    state['rubric_mapping'] = [
        {
            "student_code_piece": mapping.student_code_piece,
            "rubric_section": mapping.rubric_section,
            "model_answer_key": mapping.model_answer_key
        }
        for mapping in structured_output.mappings
    ]
    
    return state


def initial_evaluation_module(state: AgentState):
    from langchain.schema import HumanMessage
    from typing import Dict, Any
    from pydantic import BaseModel, Field
    from typing_extensions import TypedDict

    class EvaluationEntry(BaseModel):
        rubric_section: str
        score: int
        comments: str
        suggestions: str

    class EvaluationResult(BaseModel):
        evaluations: List[EvaluationEntry]
        total_score: int

    # Prompt template for initial evaluation
    evaluation_prompt = PromptTemplate(
        template="""
        You are an automated grading assistant. Evaluate the following student code segment based on the given rubric section.

        Rubric Section: {rubric_section}
        Model Answer Key: {model_answer_key}
        Student Code: {student_code_piece}

        Provide a numeric score (out of {max_score}) for the rubric section.
        Include comments on the correctness of the implementation.
        Suggest improvements for the student's code.

        Structure your response in JSON format as follows:
        {{
            "score": <int>,
            "comments": "<string>",
            "suggestions": "<string>"
        }}
        """,
        input_variables=["rubric_section", "model_answer_key", "student_code_piece", "max_score"]
    )

    # Define a structured output model for evaluation
    class StructuredEvaluation(BaseModel):
        score: int
        comments: str
        suggestions: str

    # Initialize LLM with structured output for evaluations
    llm_evaluation = ChatOpenAI(model="gpt-4-0613", temperature=0).with_structured_output(StructuredEvaluation)

    evaluations = []
    total_score = 0

    for mapping in state['rubric_mapping']:
        rubric_section = mapping['rubric_section']
        model_answer_key = mapping['model_answer_key']
        student_code_piece = mapping['student_code_piece']

        # Define maximum score based on rubric_section
        rubric_scores = {
            "Compilation and Execution": 10,
            "User Input Handling": 10,
            "Displaying Original String": 5,
            "Converting to Uppercase": 10,
            "Reversing the String": 15,
            "Counting Characters": 10,
            "Output Formatting": 10,
            "Readability and Organization": 10,
            "Best Practices and Resource Management": 5,
            "Comments and Documentation": 5,
            "Single Class Requirement": 5,
            "Code Length Limit": 5
        }

        max_score = rubric_scores.get(rubric_section, 5)  # Default to 5 if not defined

        # Prepare the input for the LLM
        prompt_input = evaluation_prompt.format(
            rubric_section=rubric_section,
            model_answer_key=model_answer_key,
            student_code_piece=student_code_piece,
            max_score=max_score
        )

        # Invoke the LLM to get the evaluation
        try:
            evaluation = llm_evaluation.invoke(prompt_input)
        except Exception as e:
            # Handle exceptions and assign zero score if evaluation fails
            evaluation = StructuredEvaluation(
                score=0,
                comments=f"Error during evaluation: {str(e)}",
                suggestions="Unable to provide suggestions due to evaluation error."
            )

        evaluations.append(EvaluationEntry(
            rubric_section=rubric_section,
            score=evaluation.score,
            comments=evaluation.comments,
            suggestions=evaluation.suggestions
        ))
        total_score += evaluation.score

    # Update the state with the evaluation results
    state['evaluation'] = {
        "evaluations": [
            {
                "rubric_section": eval_entry.rubric_section,
                "score": eval_entry.score,
                "comments": eval_entry.comments,
                "suggestions": eval_entry.suggestions
            }
            for eval_entry in evaluations
        ],
        "total_score": total_score
    }

    return state

# Function to review the evaluation done by the initial evaluation module
def review_evaluation_module(state: AgentState):
    from pydantic import BaseModel, Field
    from langchain_openai import ChatOpenAI
    from langchain.prompts import PromptTemplate
    from typing import List

    class FinalAssessmentEntry(BaseModel):
        class_name: str
        final_comments: str
        final_score: int

    class FinalAssessmentResult(BaseModel):
        final_assessment: List[FinalAssessmentEntry]

    # Prompt template for reviewing evaluations
    review_prompt = PromptTemplate(
        template="""
        You are an automated grading assistant tasked with reviewing the initial evaluations of student code.

        Initial Evaluations:
        {initial_evaluations}

        Provide the final assessment for each Java class in the student's code. Ensure that the assessments are fair and consider all aspects of the rubric.

        Structure your response in JSON format as follows:
        {
            "final_assessment": [
                {
                    "class_name": "<ClassName>",
                    "final_comments": "<Final comments on the class>",
                    "final_score": <int>
                },
                ...
            ]
        }
        """,
        input_variables=["initial_evaluations"]
    )

    # Initialize LLM with structured output for final assessment
    llm_review = ChatOpenAI(model="gpt-4o-mini", temperature=0).with_structured_output(FinalAssessmentResult)

    initial_evaluations = state.get('evaluation', {}).get('evaluations', [])

    # Prepare the evaluations in a readable format
    evaluations_summary = ""
    for eval_entry in initial_evaluations:
        evaluations_summary += f"Rubric Section: {eval_entry['rubric_section']}\n"
        evaluations_summary += f"Score: {eval_entry['score']}\n"
        evaluations_summary += f"Comments: {eval_entry['comments']}\n"
        evaluations_summary += f"Suggestions: {eval_entry['suggestions']}\n\n"

    # Prepare the input for the LLM
    prompt_input = {
        "initial_evaluations": evaluations_summary
    }

    # Invoke the LLM to get the final assessment
    try:
        final_assessment = llm_review.invoke(prompt_input)
    except Exception as e:
        # Handle exceptions and assign default final assessment if needed
        final_assessment = FinalAssessmentResult(
            final_assessment=[]
        )

    # Update the state with the final assessment
    state['final_assessment'] = [
        {
            "class_name": fa.class_name,
            "final_comments": fa.final_comments,
            "final_score": fa.final_score
        }
        for fa in final_assessment.final_assessment
    ]

    return state

def marks_extraction_module(state: AgentState):
    pass

def total_marks_calculation_module(state: AgentState):
    pass

# Build the workflow graph
graph = StateGraph(AgentState)

# Add the nodes to the graph
graph.add_node("class_extraction", class_extraction_node)
graph.add_node("rubric_extraction", rubric_extraction_module)
graph.add_node("initial_evaluation", initial_evaluation_module)
graph.add_node("review_evaluation", review_evaluation_module)
graph.add_node("marks_extraction", marks_extraction_module)
graph.add_node("total_marks_calculation", total_marks_calculation_module)

# Define the edges (flow) between the nodes
graph.add_edge(START, "class_extraction")
graph.add_edge("class_extraction", "rubric_extraction")
graph.add_edge("rubric_extraction", "initial_evaluation")
graph.add_edge("initial_evaluation", "review_evaluation")
graph.add_edge("review_evaluation", "marks_extraction")
graph.add_edge("marks_extraction", "total_marks_calculation")
graph.add_edge("total_marks_calculation", END)

final_graph = graph.compile()

# Workflow to start the graph execution and test the first node
def test_class_extraction():
    # Initialize the agent state with student and model solutions
    state = {
        "messages": [],
        "student_code": '''import java.util.Scanner;

public class StringManipulator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String input = sc.next();

        System.out.println("Original String: " + input);
        System.out.println("Uppercase String: " + input.toLowerCase());

        String reversed = "";
        for (int i = 0; i < input.length(); i++) { 
            reversed += input.charAt(i); 
        }
        System.out.println("Reversed String: " + reversed);

        System.out.println("Number of Characters: " + input.length()); 
    }
}
''',
        "model_solution": '''import java.util.Scanner;

public class StringManipulator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String input = sc.nextLine();
        System.out.println("Original String: " + input);
        System.out.println("Uppercase String: " + input.toUpperCase());
        String reversed = new StringBuilder(input).reverse().toString();
        System.out.println("Reversed String: " + reversed);
        System.out.println("Number of Characters: " + input.length());
        sc.close();
    }
}
''',
        "rubric": """
        1. Compilation and Execution (10 marks)
        2. User Input Handling (10 marks)
        3. String Manipulations:
            - Displaying Original String (5 marks)
            - Converting to Uppercase (10 marks)
            - Reversing the String (15 marks)
            - Counting Characters (10 marks)
        4. Output Formatting (10 marks)
        5. Readability and Organization (10 marks)
        6. Best Practices and Resource Management (5 marks)
        7. Comments and Documentation (5 marks)
        8. Single Class Requirement (5 marks)
        9. Code Length Limit (5 marks)
        """
    }

    # Define the thread context for streaming
    thread = {"configurable": {"thread_id": "1"}}

    # Stream the execution of the graph
    for s in final_graph.stream(state):
        pprint(s)

# Call the test function to execute the workflow
test_class_extraction()