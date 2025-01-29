import os
import openai
import logging
import streamlit as st
from langchain import OpenAI
from langchain.agents import AgentExecutor, Tool
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.agents import tool
from langchain.agents import Tool
from langchain.agents import initialize_agent, AgentType

load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

################
# Tools
################

@tool("psychometric_tool")
def generate_psychometric_questions(query: str) -> str:
    """Generates 5 psychometric test questions with 4 options each based on the input query."""
    logger.info(f"Executing 'psychometric_tool' with input: {query}")
    prompt = (
        f"Generate 5 psychometric test questions for the topic: {query}. "
        "Each question should have 4 distinct options labeled as Option 1, Option 2, Option 3, and Option 4. "
        "Format the output as: Question: <question text>\nOption 1: <option 1>\nOption 2: <option 2>\nOption 3: <option 3>\nOption 4: <option 4>"
    )
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
    return llm.predict(prompt)

# Remove job description tool
# @tool("job_description_tool")
# def generate_jd_questions(query: str) -> str:
#     """Generates a checklist of questions based on a job description."""
#     logger.info(f"Executing 'job_description_tool' with input: {query}")
#     prompt = f"Generate a checklist of questions based on the following job description: {query}."
#     llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
#     return llm.predict(prompt)

@tool("reporting_tool")
def generate_report(answers: str) -> str:
    """Analyzes answers and generates a detailed report."""
    logger.info(f"Executing 'reporting_tool' with input: {answers}")
    prompt = f"Analyze these answers and generate a detailed report: {answers}."
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
    return llm.predict(prompt)

################
# Initialize the agents
################

# Sub-Agent 0: Psychometric Test Agent
tools_agent_0 = [
    Tool(name="Generate Psychometric", func=generate_psychometric_questions, description="Generate psychometric test questions based on topic.")
]

llm_agent_0 = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
agent_0 = initialize_agent(tools_agent_0, llm_agent_0, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Remove Sub-Agent 1: Job Description Agent
# tools_agent_1 = [
#     Tool(name="Generate JD Questions", func=generate_jd_questions, description="Generate questions based on job description.")
# ]

# llm_agent_1 = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
# agent_1 = initialize_agent(tools_agent_1, llm_agent_1, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Main Agent (Router Agent)
tools_main_agent = [
    Tool(name="General Queries", func=agent_0.run, description="Handles general queries like answering questions or web search.")
    # Remove Appointment Queries tool
    # Tool(name="Appointment Queries", func=agent_1.run, description="Handles appointment scheduling and rescheduling.")
]

llm_main_agent = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
main_agent = initialize_agent(tools_main_agent, llm_main_agent, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Streamlit app
st.title("Quiz App with LangChain Agents")
quiz_type = st.selectbox("Choose Quiz Type:", ["Psychometric"])
query = st.text_input("Enter Query (e.g., test topic):")

if st.button("Generate Quiz Questions"):
    if quiz_type == "Psychometric":
        questions = agent_0.run(query)
        st.session_state['questions'] = questions.split('\n\n')[:5]  # Split by double newline for better separation
        st.session_state['answers'] = [""] * 5

if 'questions' in st.session_state:
    st.write("### Quiz Questions")
    for i, question in enumerate(st.session_state['questions']):
        question_parts = question.split('\n')
        question_text = question_parts[0].replace("Question:", "").strip()
        options = [opt.replace(f"Option {j+1}:", "").strip() for j, opt in enumerate(question_parts[1:5])]
        st.session_state['answers'][i] = st.radio(f"Question {i+1}: {question_text}", options, key=f"q{i+1}")

if st.button("Generate Report"):
    answers = ", ".join(st.session_state['answers'])
    report = generate_report(answers)
    st.write(report)