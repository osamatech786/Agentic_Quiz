import json

def save_question(question_data):
    with open("quiz_bank.json", "a") as f:
        f.write(json.dumps(question_data) + "\n")

def load_questions():
    with open("quiz_bank.json", "r") as f:
        return [json.loads(line) for line in f]
