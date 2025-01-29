import streamlit as st
import openai
from jsonschema import validate
from database import save_question
import getpass
import os
from langchain_openai import ChatOpenAI
from schemas import (
    schema_mcq,
    schema_true_false,
    schema_likert,
    schema_open_ended,
    schema_sjt,
    schema_time_problem_solving,
    schema_adaptive,
    schema_hypothetical,
    schema_personality_scenario
)


if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

llm = ChatOpenAI(model="gpt-4o-mini")


def generate_questions(prompt, schema, num_questions=1):
    """
    Generate one or more structured questions using the OpenAI API.
    """
    structured_llm = llm.with_structured_output(schema)
    
    # Format the prompt with the number of questions
    extended_prompt = prompt.format(num_questions=num_questions)

    # Debug: Print the extended prompt
    print(f"Extended Prompt Sent to OpenAI:\n{extended_prompt}\n")
    
    response = structured_llm.invoke(extended_prompt)

    # Debug: Print the raw response
    print(f"Raw Response from OpenAI:\n{response}\n")

    # If the response is a single dictionary, wrap it in a list
    if isinstance(response, dict) and "properties" in response:
        response = response["properties"]

    # If the response is a list, ensure it's properly formatted
    if not isinstance(response, list):
        response = [response]  # Convert to list if it's a single question

    # Validate and flatten each question
    validated_questions = []
    for question_data in response[:num_questions]:
        # Flatten nested data if needed
        if "properties" in question_data:
            question_data = question_data["properties"]

        question_data["title"] = schema["title"]  # Add title
        validate(instance=question_data, schema=schema)  # Validate schema
        validated_questions.append(question_data)
        save_question(question_data)  # Save question

    return validated_questions


def split_response_into_questions(response_text, num_questions):
    """
    Split a text response into multiple JSON questions.
    """
    try:
        # Assuming JSON objects are separated by newlines or specific markers
        questions = response_text.split("\n\n")
        return [eval(question.strip()) for question in questions if question.strip()][:num_questions]
    except Exception as e:
        raise ValueError(f"Unable to split response into questions: {e}")
