'''python
from jsonschema import validate

question_data = {
    "question": "What is 2 + 2?",
    "options": [
        {"option_text": "3", "is_correct": False, "explanation": "Incorrect, it's not 3."},
        {"option_text": "4", "is_correct": True, "explanation": "Correct, 2 + 2 equals 4."}
    ],
    "difficulty": "easy",
    "category": "numerical reasoning"
}

schema = { ... }  # Your MCQ schema from schemas.py
validate(instance=question_data, schema=schema)
'''

import openai
from jsonschema import validate

# OpenAI API Key
openai.api_key = "your_openai_api_key"

# Prompt to generate a multiple-choice question
prompt = """
Generate a multiple-choice question for a verbal reasoning test. 
Provide 4 options, indicate the correct one, and include explanations for each.
"""

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=300
)

# Assume the response contains JSON-like structure
question_data = eval(response.choices[0].text.strip())

# Validate against the schema
schema = {
    "title": "multiple_choice_question",
    "description": "A multiple-choice question for psychometric testing.",
    "type": "object",
    "properties": {
        "question": {"type": "string"},
        "options": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "option_text": {"type": "string"},
                    "is_correct": {"type": "boolean"},
                    "explanation": {"type": "string"}
                },
                "required": ["option_text", "is_correct"]
            }
        },
        "difficulty": {"type": "string"},
        "category": {"type": "string"}
    },
    "required": ["question", "options", "category"]
}

validate(instance=question_data, schema=schema)
print("Question validated successfully!")
