import os
import getpass
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, StateGraph, START
from typing import Annotated, Sequence
from typing_extensions import TypedDict
from pydantic import BaseModel, Field

# Step 1: Set environment key for OpenAI
def _set_env(key: str):
    if key not in os.environ:
        os.environ[key] = getpass.getpass(f"{key}:")

_set_env("OPENAI_API_KEY")

### Classes extraction process ###

# Load student submission and model solution
def load_documents():
    """
    Load the student submission and model solution from local files.
    Returns the content of the files.
    """
    try:
        with open("student_solution.java", "r") as f:
            student_code = f.read()
        with open("model_solution.java", "r") as f:
            model_code = f.read()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    return student_code, model_code

# Step 2: Define the LLM-based class extraction model
class ExtractClassesStep(BaseModel):
    """
    Uses an LLM to extract class information from the Java code.
    """
    code: str = Field(description="Java code for extraction")
    problem_description: str = Field(description="Description of the problem or class expectations")

    def extract_classes(self):
        """
        Extracts class information (names, visibility, and types) from the provided Java code.
        """
        prompt = f"""
        The following Java code contains multiple classes:
        {self.code}
        
        Based on the problem description: "{self.problem_description}", extract and list all the individual class names, visibility (public, private), and types (class, interface, enum) that are present in the code.
        """
        model = ChatOpenAI(temperature=0, model="gpt-4-turbo")
        response = model.invoke([HumanMessage(content=prompt)])
        return response.content

# Step 3: Compare the extracted classes
def compare_classes(student_classes, model_classes):
    """
    Compare the classes extracted from the student's submission and the model solution.
    Returns missing and extra classes.
    """
    student_class_set = set(student_classes.splitlines())
    model_class_set = set(model_classes.splitlines())

    missing_classes = model_class_set - student_class_set
    extra_classes = student_class_set - model_class_set

    return missing_classes, extra_classes

# Step 4: Define LangGraph nodes and workflow
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], ...]  # Keeps track of messages exchanged between nodes

# Agent Node
def agent(state):
    """
    Invokes the agent model to decide the next step based on the current state.
    """
    print("---CALL AGENT---")
    messages = state["messages"]
    
    # Add a prompt if messages are empty
    if not messages:
        messages.append(HumanMessage(content="What classes are expected based on the code provided?"))

    model = ChatOpenAI(temperature=0, streaming=True, model="gpt-4-turbo")
    response = model.invoke(messages)
    return {"messages": [response]}

# Class Generation Node
def generate(state):
    """
    Generates a response by extracting classes from student submission and model solution,
    then compares them.
    """
    print("---GENERATE CLASSES---")
    
    # Load student and model solution code
    student_code, model_code = load_documents()
    
    # Extract classes using LLM
    student_extractor = ExtractClassesStep(code=student_code, problem_description="Check if the classes match.")
    model_extractor = ExtractClassesStep(code=model_code, problem_description="Expected classes.")

    extracted_student_classes = student_extractor.extract_classes()
    extracted_model_classes = model_extractor.extract_classes()

    # Compare the extracted classes
    missing, extra = compare_classes(extracted_student_classes, extracted_model_classes)

    # Prepare the response
    return {"messages": [f"Missing classes: {missing}, Extra classes: {extra}"]}

# Step 5: Define the LangGraph workflow
workflow = StateGraph(AgentState)

# Define the workflow nodes
workflow.add_node("agent", agent)  # Agent decision node
workflow.add_node("generate", generate)  # Class generation node

# Add edges (workflow logic)
workflow.add_edge(START, "agent")  # Start with agent
workflow.add_edge("agent", "generate")  # Connect agent to generate
workflow.add_edge("generate", END)  # End after class comparison

# Compile workflow graph
graph = workflow.compile()

# Step 6: Run the workflow
try:
    result = graph.invoke({"messages": []})  # Starting with an empty message state
    print(result)  # Final output will be printed
except Exception as e:
    print(f"An error occurred: {e}")

