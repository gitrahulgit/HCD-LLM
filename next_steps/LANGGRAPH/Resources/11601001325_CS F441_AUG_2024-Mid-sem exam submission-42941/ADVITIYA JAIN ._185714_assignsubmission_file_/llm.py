import getpass
import os
import asyncio  # Import asyncio to handle the async function
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def _set_env(key: str):
    if key not in os.environ:
        os.environ[key] = getpass.getpass(f"{key}:")

_set_env("OPENAI_API_KEY")

# Step 1: Function to extract Java classes using LLM from a file
async def extract_classes_from_file(file_path: str) -> str:
    # Initialize the LLM (OpenAI) for parsing
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, streaming=True)
    
    # Define a prompt to extract Java classes
    prompt = PromptTemplate(
        template="""
        You are analyzing a Java code. 

        ---Code---
        {code}

        Please extract all Java class definitions as well as the code that is inside each class from the code in the format:
        ClassName {{
            --code--
        }}

        Provide only the class names and class definitions, nothing else. Do not include import statements, such as:
        import java.util.Scanner;
        """,
        input_variables=["code"]
    )
    
    # Read the content of the file (student or model solution)
    with open(file_path, "r") as f:
        code_content = f.read()

    # Chain the prompt with the LLM and output parser
    extraction_chain = prompt | llm | StrOutputParser()
    
    # Invoke the chain with the content from the file
    extracted_result = await extraction_chain.ainvoke({"code": code_content})
    
    # Return the extracted class definitions
    return extracted_result

# Step 2: Run the extraction for both student and model solution files
async def run_class_extraction():
    # File paths for student and model solution markdown files
    student_file = "student_solution.md"
    model_file = "model_solution.md"
    
    # Extract classes from the student file
    student_classes = await extract_classes_from_file(student_file)
    
    # Extract classes from the model solution file
    model_classes = await extract_classes_from_file(model_file)
    
    # Output the results
    # print("Extracted Student Classes:\n", student_classes)
    # print("\nExtracted Model Classes:\n", model_classes)


async def extract_evaluation_details(student_classes: str, rubric_file: str):
    # Initialize the LLM (OpenAI) for parsing
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, streaming=True)
    
    # Read the rubric content from the file
    with open(rubric_file, "r") as f:
        rubric_content = f.read()

    # Define a prompt to extract evaluation details from the rubric for each class
    prompt = PromptTemplate(
        template="""
        You are provided with a rubric that contains evaluation instructions for different Java classes. Here is the rubric:

        ---Rubric---
        {rubric_content}

        Here are the student's Java class names:

        ---Class Names---
        {student_classes}

        Please extract the evaluation details from the rubric for each class in the format:
        ClassName: Evaluation Instructions

        If there is no evaluation detail for a class, return "No instructions found" for that class.
        """,
        input_variables=["rubric_content", "student_classes"]
    )
    
    # Chain the prompt with the LLM and output parser
    evaluation_extraction_chain = prompt | llm | StrOutputParser()

    # Invoke the chain with both the student's classes and the rubric content
    class_wise_evaluation_scheme = await evaluation_extraction_chain.ainvoke({
        "rubric_content": rubric_content,
        "student_classes": student_classes
    })
    
    # Parse the result into a dictionary
    # Assuming the output is formatted as ClassName: Evaluation Instructions
    # evaluation_dict = {}
    # for line in evaluation_result.splitlines():
    #     if ": " in line:
    #         class_name, instructions = line.split(": ", 1)
    #         evaluation_dict[class_name.strip()] = instructions.strip()
    
    return {student_classes: class_wise_evaluation_scheme}

async def class_wise_evaluation(student_classes: str, model_classes: str, evaluation_scheme: dict) -> dict:
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, streaming=True)

    # Define the prompt for class-wise evaluation
    prompt = PromptTemplate(
        template="""
        You are evaluating the correctness of Java classes based on the following scheme:

        ---Class-wise Evaluation Scheme---
        {evaluation_scheme}

        Here are the model class definitions(Along with the Class-wise Evaluation Scheme
        you can take reference from the model_solution also whereever required):

        ---Model Classes---
        {model_classes}
        
        Here are the student class definitions(You have to evaluate this):

        ---Student Classes---
        {student_classes}


        Please provide an evaluation for each class, including:
        - A score for each criterion mentioned in the evaluation scheme, the maximum marks for each criteria are also mentioned 
        in the evaluation scheme
        - Detailed comments about correctness, errors, and suggestions for improvement.

        Format your response as follows:
        ClassName: 
        - Score: Y
        - Comments: [Detailed comments here]
        """,
        input_variables=["evaluation_scheme", "student_classes", "model_classes"]
    )

    # Create the evaluation chain
    evaluation_chain = prompt | llm | StrOutputParser()

    # Invoke the evaluation chain
    evaluation_result = await evaluation_chain.ainvoke({
        "evaluation_scheme": evaluation_scheme,
        "student_classes": student_classes,
        "model_classes": model_classes
    })

    return evaluation_result


# Step 4: Run the extraction and evaluation
async def run_class_extraction_and_evaluation():
    # File paths for student, model solution, and rubric markdown files
    student_file = "student_solution.md"
    model_file = "model_solution.md"
    rubric_file = "rubric.md"
    
    # Extract classes from the student file
    student_classes = await extract_classes_from_file(student_file)
    
    # Extract classes from the model solution file
    model_classes = await extract_classes_from_file(model_file)

    # Extract evaluation details for each class from the rubric
    evaluation_details = await extract_evaluation_details(student_classes, rubric_file)

    # Perform class-wise evaluation using the extracted classes and evaluation details
    class_evaluation = await class_wise_evaluation(student_classes, model_classes, evaluation_details)

    # Output the results
    print("\nClass-wise Evaluation Results:\n", class_evaluation)

# Step 5: Execute the main function properly using asyncio
if __name__ == "__main__":
    # Use asyncio.run() to run the async function
    asyncio.run(run_class_extraction_and_evaluation())