# 1. Multiple-Choice Questions (MCQs) Schema

schema_mcq = {
    "title": "multiple_choice_question",
    "description": "A multiple-choice question for psychometric testing.",
    "type": "object",
    "properties": {
        "question": {
            "type": "string",
            "description": "The question text."
        },
        "options": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "option_text": {
                        "type": "string",
                        "description": "The text of the option."
                    },
                    "is_correct": {
                        "type": "boolean",
                        "description": "Indicates whether this option is correct."
                    },
                    "explanation": {
                        "type": "string",
                        "description": "Explanation for the correctness or incorrectness of this option."
                    }
                },
                "required": ["option_text", "is_correct"]
            },
            "description": "List of answer options."
        },
        "difficulty": {
            "type": "string",
            "description": "The difficulty level of the question.",
            "enum": ["easy", "medium", "hard"]
        },
        "category": {
            "type": "string",
            "description": "The category of the question, e.g., 'numerical reasoning', 'verbal reasoning'."
        }
    },
    "required": ["question", "options", "category"]
}


# 2. True/False Questions Schema

schema_true_false = {
    "title": "true_false_question",
    "description": "A true/false question for psychometric testing.",
    "type": "object",
    "properties": {
        "statement": {
            "type": "string",
            "description": "The statement to evaluate as true or false."
        },
        "correct_answer": {
            "type": "boolean",
            "description": "Indicates whether the statement is true (true) or false (false)."
        },
        "explanation": {
            "type": "string",
            "description": "Explanation for why the statement is true or false."
        },
        "category": {
            "type": "string",
            "description": "The category of the question, e.g., 'logical reasoning', 'workplace scenarios'."
        }
    },
    "required": ["statement", "correct_answer", "explanation", "category"]
}


# 3. Likert Scale Questions Schema

schema_likert = {
    "title": "likert_scale_question",
    "description": "A Likert scale question for psychometric testing.",
    "type": "object",
    "properties": {
        "statement": {
            "type": "string",
            "description": "The statement to rate on the Likert scale."
        },
        "scale": {
            "type": "object",
            "properties": {
                "min_value": {
                    "type": "integer",
                    "description": "Minimum value on the scale."
                },
                "max_value": {
                    "type": "integer",
                    "description": "Maximum value on the scale."
                },
                "labels": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "description": "Labels for each scale point."
                    }
                }
            },
            "required": ["min_value", "max_value", "labels"]
        },
        "category": {
            "type": "string",
            "description": "The category of the question, e.g., 'stress tolerance', 'teamwork'."
        }
    },
    "required": ["statement", "scale", "category"]
}


# 4. Open-Ended Questions Schema

schema_open_ended = {
    "title": "open_ended_question",
    "description": "An open-ended question for psychometric testing.",
    "type": "object",
    "properties": {
        "question": {
            "type": "string",
            "description": "The question text."
        },
        "expected_keywords": {
            "type": "array",
            "items": {
                "type": "string",
                "description": "Key points or keywords expected in the answer."
            },
            "description": "The list of expected keywords or points in the answer."
        },
        "category": {
            "type": "string",
            "description": "The category of the question, e.g., 'leadership', 'conflict resolution'."
        }
    },
    "required": ["question", "category"]
}


# 5. Situational Judgment Questions (SJT) Schema

schema_sjt = {
    "title": "situational_judgment_question",
    "description": "A situational judgment question for psychometric testing.",
    "type": "object",
    "properties": {
        "scenario": {
            "type": "string",
            "description": "The scenario description."
        },
        "options": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "option_text": {
                        "type": "string",
                        "description": "The text of the option."
                    },
                    "effectiveness_rating": {
                        "type": "integer",
                        "description": "Rating of the option's effectiveness on a scale of 1-5."
                    },
                    "explanation": {
                        "type": "string",
                        "description": "Explanation of why this option is effective or ineffective."
                    }
                },
                "required": ["option_text", "effectiveness_rating"]
            },
            "description": "List of possible actions."
        },
        "category": {
            "type": "string",
            "description": "The category of the question, e.g., 'leadership', 'problem-solving'."
        }
    },
    "required": ["scenario", "options", "category"]
}


# 6. Timed Problem-Solving Questions Schema

schema_time_problem_solving = {
    "title": "timed_problem_solving_question",
    "description": "A timed problem-solving question for psychometric testing.",
    "type": "object",
    "properties": {
        "question": {
            "type": "string",
            "description": "The problem statement or question."
        },
        "correct_answer": {
            "type": "string",
            "description": "The correct answer to the problem."
        },
        "explanation": {
            "type": "string",
            "description": "Explanation of how to arrive at the correct answer."
        },
        "time_limit_seconds": {
            "type": "integer",
            "description": "The time limit to solve the problem, in seconds."
        },
        "category": {
            "type": "string",
            "description": "The category of the question, e.g., 'numerical reasoning', 'logical reasoning'."
        }
    },
    "required": ["question", "correct_answer", "time_limit_seconds", "category"]
}


# 7. Adaptive Questions Schema

schema_adaptive = {
    "title": "adaptive_question",
    "description": "A set of adaptive questions with increasing difficulty for psychometric testing.",
    "type": "object",
    "properties": {
        "questions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "question_text": {
                        "type": "string",
                        "description": "The text of the question."
                    },
                    "difficulty": {
                        "type": "string",
                        "description": "The difficulty level of the question.",
                        "enum": ["easy", "medium", "hard"]
                    }
                },
                "required": ["question_text", "difficulty"]
            },
            "description": "List of questions with increasing difficulty."
        },
        "category": {
            "type": "string",
            "description": "The category of the questions, e.g., 'numerical reasoning', 'verbal reasoning'."
        }
    },
    "required": ["questions", "category"]
}

# 8. Hypothetical or Role-Playing Questions Schema

schema_hypothetical = {
    "title": "hypothetical_question",
    "description": "A hypothetical or role-playing question for psychometric testing.",
    "type": "object",
    "properties": {
        "scenario": {
            "type": "string",
            "description": "The hypothetical scenario description."
        },
        "question": {
            "type": "string",
            "description": "The question text related to the scenario."
        },
        "expected_response": {
            "type": "string",
            "description": "The expected response or key points to look for in the answer."
        },
        "category": {
            "type": "string",
            "description": "The category of the question, e.g., 'decision-making', 'conflict resolution'."
        }
    },
    "required": ["scenario", "question", "category"]
}

# 9. Personality-Based Scenario Questions Schema

schema_personality_scenario = {
    "title": "personality_scenario_question",
    "description": "A scenario-based question to assess personality traits for psychometric testing.",
    "type": "object",
    "properties": {
        "scenario": {
            "type": "string",
            "description": "The scenario description."
        },
        "question": {
            "type": "string",
            "description": "The question text related to the scenario."
        },
        "traits_assessed": {
            "type": "array",
            "items": {
                "type": "string",
                "description": "List of personality traits assessed by the question."
            },
            "description": "List of personality traits assessed."
        },
        "category": {
            "type": "string",
            "description": "The category of the question, e.g., 'empathy', 'teamwork'."
        }
    },
    "required": ["scenario", "question", "traits_assessed", "category"]
}