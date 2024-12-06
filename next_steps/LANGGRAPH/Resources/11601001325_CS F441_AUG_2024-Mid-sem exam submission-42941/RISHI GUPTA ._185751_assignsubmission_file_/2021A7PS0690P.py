import getpass
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict
from typing import Dict, Annotated, Sequence
from langgraph.graph import END, START, StateGraph
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage
from langgraph.graph.message import add_messages
import pprint



#Link to ChatGPT Chat History: https://chatgpt.com/share/670659c7-a48c-8001-8f86-5b9e5eb21dde


def _set_env(key: str):
    if key not in os.environ:
        os.environ[key] = getpass.getpass(f"{key}:")

_set_env("OPENAI_API_KEY")

model = ChatOpenAI(temperature=0, model="gpt-4o-mini")


class extracted_code(TypedDict):
    extracted_class : str

class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

def class_extraction(state):
    student_solution_file = 'student_solution.md'
    model_solution_file = 'model_solution.md'
    student_solution_file_contents = read_md_file(student_solution_file)
    model_solution_file_contents = read_md_file(model_solution_file)

    prompt = PromptTemplate(
        template = """You are Java code extractor. You are given a submitted Java Code which is in string format. \n
        You have to read the code, identify and parse all the classes. \n
        The code contains only one class, so just extract the actual code of that class and return it as it is.\n
        Only keep the contents of the class, not any other code or import statements declared at the beginning.\n
        Here is the java code (as string)\n\n
        {file_content}""",
        input_variables=["file_content"]
    )
    llm = model.with_structured_output(extracted_code)
    chain = prompt | llm
    student_output = chain.invoke({"file_content": student_solution_file_contents})
    model_output = chain.invoke({"file_content": model_solution_file_contents})
    studentMessage = HumanMessage("Student Code: \n"+student_output['extracted_class'])
    modelMessage = HumanMessage("Model Code: \n"+model_output['extracted_class'])
    return {"messages": [studentMessage, modelMessage]}
    

def rubric_extraction(state):
    rubric = 'rubric.md'
    extracted_rubric = rubric_extraction(read_md_file(rubric))
    prompt = PromptTemplate(
        template="""You are a Java code evaluator. You are given a rubric which contains the criteria for evaluating a Java code. \n
        Read and parse this rubric. Extract the relevant details for code evaluation like criteria and marks.\n
        The rubric is meant for only one class solution since the code contains only one class.\n
        Here is the rubric:\n\n
        {rubric_content}""",
        input_variables=["rubric_content"]
    )
    chain = prompt | model
    output = chain.invoke({"rubric_content": extracted_rubric})
    # print(output.content)
    return {"messages": [HumanMessage("Rubrik: \n"+output.content)]}

def evaluation(state):
    student_solution = state["messages"][-3]
    model_solution = state["messages"][-2]
    rubrik = state["messages"][-1]

    prompt = PromptTemplate(
        template="""You are a Java code evaluator. You are given a rubric which contains the criteria for evaluating a Java code. \n
        You are given the student solution, model solution and evaluation rubrik.\n
        Analyse, and compare both to evaluate the student solution.\n
        Return appropriate feedback and total marks scored by the student.\n
        Here is the student solution:\n\n
        {student_solution}\n\n
        Here is the model solution:\n\n
        {model_solution}\n\n
        Here is the rubric:\n\n
        {rubric}""",
        input_variables=["student_solution", "model_solution", "rubric"]
    )
        
    class Evaluation(TypedDict):
        feedback: str
        marks: int
    
    llm = model.with_structured_output(Evaluation)
    chain = prompt | llm
    response = chain.invoke({"student_solution": student_solution, "model_solution": model_solution, "rubric": rubrik})
    print(response)
    return {"messages": [AIMessage("Evaluation: \n"+response['feedback']), HumanMessage("Marks: "+response['marks'])]}



def read_md_file(file_path):
    """
    Reads a markdown (.md) file and returns its contents as a string.
    
    :param file_path: Path to the markdown file
    :return: String containing the entire file contents
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


if __name__=='__main__':
    
    #Created nodes for the 3 modules, assuming code contains only one class (Simple Solution)
    #Code Compiles
    workflow = StateGraph(State)
    workflow.add_node("class_extractor", class_extraction)
    workflow.add_node("rubric_extractor", rubric_extraction)
    workflow.add_node("evaluation", evaluation)

    workflow.add_edge(START, "class_extractor")
    workflow.add_edge("class_extractor", "rubric_extractor")
    workflow.add_edge("rubric_extractor", "evaluation")
    workflow.add_edge("evaluation", END)

    graph = workflow.compile()


    # inputs = {
    #     "messages": [
    #         ("user", "Evaluate the Java code as an instructor."),
    #     ]
    # }
    # for output in graph.stream(inputs):
    #     for key, value in output.items():
    #         pprint.pprint(f"Output from node '{key}':")
    #         pprint.pprint("---")
    #         pprint.pprint(value, indent=2, width=80, depth=None)
    #     pprint.pprint("\n---\n")
