import getpass
import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

llm_api_key = input("Please enter your LLM API key: ")

LLM_API_URL = "https://api.openai.com/v1/chat/completions"

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


_set_env("OPENAI_API_KEY")

from langchain_openai import ChatOpenAI
import os

def extract_text_from_markdown(file_path):
    """Extract text from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def separate_into_java_classes(text):
    """Use ChatOpenAI to separate text into Java classes."""
    # Initialize the ChatOpenAI model
    chat_model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))
    
    # Prepare the input message
    input_message = f"Separate the following text into Java classes:\n{text}"
    
    # Invoke the model and get the response
    response = chat_model.invoke([{"role": "user", "content": input_message}])
    
    return response['content']
    file_path = 'student solution.md'  # Path to your markdown file
    
    # Extract text from markdown file
    extracted_text = extract_text_from_markdown(file_path)
    
    # Call OpenAI API to separate text into Java classes
    java_classes = separate_into_java_classes(extracted_text)

def generate_java_classes_from_model_solution(file_path):
    """Extract Java class definitions from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression to find Java class definitions
    # This regex matches lines starting with 'public class' or 'class'
    class_pattern = r'(public\s+class\s+\w+\s*{[^}]*})|(\s*class\s+\w+\s*{[^}]*})'
    
    # Find all matches in the content
    java_classes = re.findall(class_pattern, content)

    # Extract only the matched classes from tuples
    return [cls[0] if cls[0] else cls[1] for cls in java_classes]

def extract_rubric_details(java_classes):
    """Invoke LLM to find rubric details for each Java class one by one."""
    chat_model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))
    
    # Initialize a list to store messages
    messages = []

    # Process each Java class
    for java_class in java_classes:
        # Prepare the prompt for extracting rubric details
        prompt = f"Extract rubric details for the following Java class:\n{java_class}"
        
        # Invoke the model and get the response
        response = chat_model.invoke([{"role": "user", "content": prompt}])
        
        # Store the response in messages
        messages.append({"role": "user", "content": prompt})
        messages.append({"role": "assistant", "content": response['content']})

    return messages

def evaluate_java_classes(student_classes, model_classes):
    """Evaluate student Java classes against model solutions."""
    chat_model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))
    
    # Initialize a list to store evaluation messages
    evaluations = []

    # Process each pair of student and model classes
    for student_class, model_class in zip(student_classes, model_classes):
        # Prepare the prompt for evaluation
        prompt = (
            f"Evaluate the following student Java class against the model solution:\n\n"
            f"Student Class:\n{student_class}\n\n"
            f"Model Class:\n{model_class}\n\n"
            "Assign a numeric score (0-100) and provide detailed feedback."
        )
        
        # Invoke the model and get the response
        response = chat_model.invoke([{"role": "user", "content": prompt}])
        
        # Store the response in evaluations
        evaluations.append({
            "student_class": student_class,
            "model_class": model_class,
            "evaluation": response['content']
        })

    return evaluations

def extract_and_sum_marks(evaluations):
    """Extract numeric scores from evaluations and calculate total marks."""
    total_marks = 0
    for evaluation in evaluations:
        # Extract numeric score from the evaluation content
        # Assuming the score is at the beginning of the response, e.g., "Score: 85"
        score_line = evaluation['evaluation'].splitlines()[0]
        score = int(score_line.split(":")[1].strip())  # Extracting the numeric part
        total_marks += score
        
    return total_marks

from langgraph.graph import ToolNode

def sum_marks(evaluations):
    """LangGraph tool to sum marks and save to a file."""
    total_marks = extract_and_sum_marks(evaluations)
    
    # Save the total marks to a file
    with open('final_evaluation.txt', 'w') as file:
        file.write(f"Total Marks: {total_marks}\n")
    
    return total_marks

def create_langgraph_workflow(student_file, model_file):
    """Create a LangGraph workflow for evaluating Java classes."""
    graph = StateGraph()

    # Start node
    start_node = graph.add_node("Start")

    # Step 1: Extract text from student markdown file
    extract_student_text_node = graph.add_node("Extract Student Text")
    graph.add_edge(start_node, extract_student_text_node)

    # Tool node to extract text from student markdown
    extract_student_tool = ToolNode(extract_text_from_markdown, inputs={"file_path": student_file})
    graph.add_edge(extract_student_text_node, extract_student_tool)

    # Step 2: Extract text from model markdown file
    extract_model_text_node = graph.add_node("Extract Model Text")
    graph.add_edge(extract_student_tool, extract_model_text_node)

    # Tool node to extract text from model markdown
    extract_model_tool = ToolNode(extract_text_from_markdown, inputs={"file_path": model_file})
    graph.add_edge(extract_model_text_node, extract_model_tool)

    # Step 3: Separate Java classes from student text
    separate_student_classes_node = graph.add_node("Separate Student Classes")
    graph.add_edge(extract_model_tool, separate_student_classes_node)

    # Tool node to separate student Java classes
    separate_student_classes_tool = ToolNode(separate_into_java_classes, inputs={"text": extract_student_tool.output})
    graph.add_edge(separate_student_classes_node, separate_student_classes_tool)

    # Step 4: Separate Java classes from model text
    separate_model_classes_node = graph.add_node("Separate Model Classes")
    graph.add_edge(separate_student_classes_tool, separate_model_classes_node)

    # Tool node to separate model Java classes
    separate_model_classes_tool = ToolNode(separate_into_java_classes, inputs={"text": extract_model_tool.output})
    graph.add_edge(separate_model_classes_node, separate_model_classes_tool)

    # Step 5: Evaluate student classes against model classes
    evaluate_classes_node = graph.add_node("Evaluate Classes")
    graph.add_edge(separate_model_classes_tool, evaluate_classes_node)

    # Tool node to evaluate classes
    evaluate_classes_tool = ToolNode(evaluate_java_classes, inputs={
        "student_classes": separate_student_classes_tool.output,
        "model_classes": separate_model_classes_tool.output
    })
    graph.add_edge(evaluate_classes_node, evaluate_classes_tool)

    # Step 6: Sum marks and save to file
    sum_marks_node = graph.add_node("Sum Marks")
    graph.add_edge(evaluate_classes_tool, sum_marks_node)

    # Tool node to sum marks
    sum_marks_tool = ToolNode(sum_marks, inputs={"evaluations": evaluate_classes_tool.output})
    graph.add_edge(sum_marks_node, sum_marks_tool)

    end_node = graph.add_node("End Evaluation")
    graph.add_edge(sum_marks_tool, end_node)
    evaluation_graph = create_langgraph_workflow(student_file, model_file)

    # Execute the workflow and print results
    state = evaluation_graph.execute()