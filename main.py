import streamlit as st
from report_generator import generate_report
from question_generator import generate_questions
from utils import generate_unique_id
import time

from prompts import (
    mcq_prompt,
    true_false_prompt,
    rating_scale_prompt,
    open_ended_prompt,
    sjt_prompt,
    timed_problem_prompt,
    adaptive_prompt,
    hypothetical_prompt,
    personality_scenario_prompt
)
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

from quiz_renderer import (
    display_mcq,
    display_true_false,
    display_likert,
    display_open_ended,
    display_sjt,
    display_timed_problem_solving,
    display_adaptive,
    display_hypothetical,
    display_personality_scenario
)

st.set_page_config(page_title="Psychometric Test App", layout="wide")

# Generate a unique test ID
if 'uid' not in st.session_state:
    st.session_state.uid = generate_unique_id()

st.title("Psychometric Test App")

# Navigation Menu
menu = ["Generate Questions", "Take Quiz", "View Answers"]
choice = st.sidebar.selectbox("Menu", menu)

# Define Question Types and Associated Prompts/Schemas
question_types = {
    "Multiple-Choice Questions (MCQs)": (mcq_prompt, schema_mcq),
    "True/False Questions": (true_false_prompt, schema_true_false),
    "Likert Scale Questions": (rating_scale_prompt, schema_likert),
    "Open-Ended Questions": (open_ended_prompt, schema_open_ended),
    "Situational Judgment Questions (SJT)": (sjt_prompt, schema_sjt),
    "Timed Problem-Solving Questions": (timed_problem_prompt, schema_time_problem_solving),
    "Adaptive Questions": (adaptive_prompt, schema_adaptive),
    "Hypothetical or Role-Playing Questions": (hypothetical_prompt, schema_hypothetical),
    "Personality-Based Scenario Questions": (personality_scenario_prompt, schema_personality_scenario)
}

# Checkbox Selection for Question Types
selected_types = []
for question_type in question_types.keys():
    # Use st.session_state to manage the disabled state
    if f"disabled_{question_type}" not in st.session_state:
        st.session_state[f"disabled_{question_type}"] = False  # Initialize as enabled
    
    # Create checkboxes with dynamic disabled state
    if st.sidebar.checkbox(
        question_type,
        key=f"checkbox_{question_type}",  # Ensure unique key
        disabled=st.session_state[f"disabled_{question_type}"]
    ):
        selected_types.append(question_type)


# Generate Questions
if choice == "Generate Questions":
    st.write("Your Unique Test ID:")
    st.text(st.session_state.uid)

    # Initialize a dictionary to store the number of questions for each type
    if 'num_questions' not in st.session_state:
        st.session_state['num_questions'] = {}

    # Display sliders on the main screen for selected types
    st.write("### Select Number of Questions for Each Type")
    for idx, question_type in enumerate(selected_types):
        slider_key = f"{question_type}_slider_{idx}"  # Unique key for each slider
        st.session_state['num_questions'][question_type] = st.slider(
            f"Number of {question_type} questions:", 
            min_value=1, 
            max_value=5, 
            value=3,  # Default value
            key=slider_key
        )

    # Generate questions on button click
    if st.button("Generate Selected Questions"):
        if selected_types:
            with st.spinner("Generating..."):
                st.session_state['questions'] = []
                for question_type in selected_types:
                    st.write(f"Generating {question_type}...")
                    prompt, schema = question_types[question_type]
                    num_questions = st.session_state['num_questions'][question_type]

                    # Debug: Print prompt and number of questions
                    # st.write(f"Prompt: {prompt}")
                    # st.write(f"Number of questions requested: {num_questions}")
                    
                    # Call the generator
                    questions = generate_questions(prompt, schema, num_questions=num_questions)
                    st.session_state['questions'].extend(questions)
                    
                    # Debug: Print generated questions
                    # st.write("Generated Questions:", questions)
            
            # Disable checkboxes after generation
            for question_type in selected_types:
                st.session_state[f"disabled_{question_type}"] = True

            st.success("Questions generated successfully!")
            st.info("""Now go to "Take Quiz" option!""")
        else:
            st.warning("Please select at least one type of question from the side menu.")


    # Reset button to clear the session state
    if st.sidebar.button("Reset Test"):
        for question_type in question_types.keys():
            st.session_state[f"disabled_{question_type}"] = False
        st.session_state.pop('questions', None)
        st.session_state.pop('answers', None)
        st.success("Test reset successfully!")
        time.sleep(1)
        st.rerun()


# Take Quiz
if choice == "Take Quiz":
    if 'questions' in st.session_state and st.session_state['questions']:
        st.write("### Quiz Questions")

        # Initialize 'answers' if not already done
        if 'answers' not in st.session_state:
            st.session_state['answers'] = [None] * len(st.session_state['questions'])

        for i, question in enumerate(st.session_state['questions']):
            question_type = question.get('title')  # Identifies the question type
            try:
                if question_type == "multiple_choice_question":
                    st.session_state['answers'][i] = display_mcq(question, i)
                elif question_type == "true_false_question":
                    st.session_state['answers'][i] = display_true_false(question, i)
                elif question_type == "likert_scale_question":
                    st.session_state['answers'][i] = display_likert(question, i)
                elif question_type == "open_ended_question":
                    st.session_state['answers'][i] = display_open_ended(question, i)
                elif question_type == "situational_judgment_question":
                    st.session_state['answers'][i] = display_sjt(question, i)
                elif question_type == "timed_problem_solving_question":
                    st.session_state['answers'][i] = display_timed_problem_solving(question, i)
                elif question_type == "adaptive_question":
                    st.session_state['answers'][i] = display_adaptive(question, i)
                elif question_type == "hypothetical_question":
                    st.session_state['answers'][i] = display_hypothetical(question, i)
                elif question_type == "personality_scenario_question":
                    st.session_state['answers'][i] = display_personality_scenario(question, i)
                else:
                    st.warning(f"Unknown question type: {question_type}")
            except KeyError as e:
                st.error(f"Error displaying question {i+1}: {e}")
                
        # Add Submit Quiz button
        if st.button("Submit Quiz"):
            st.session_state["quiz_completed"] = True
            st.success("Quiz submitted successfully!")
            st.info("""Now go to "View Answers" option!""")
    else:
        st.warning("No questions available. Please generate questions first.")


# View Answers
elif choice == "View Answers":
    if 'quiz_completed' in st.session_state and st.session_state['quiz_completed']:
        st.write("### Quiz Report")

        for i, (question, answer) in enumerate(zip(st.session_state['questions'], st.session_state['answers'])):
            # Display question text or statement
            st.write(f"**Question {i + 1}:** {question.get('statement') or question.get('question')}")
            
            # Display user's answer
            st.write(f"**Your Answer:** {answer}")
            
            # Display correct answer if available
            if 'correct_answer' in question:
                st.write(f"**Correct Answer:** {question['correct_answer']}")
            
            # Display explanation if available
            if 'explanation' in question:
                st.write(f"**Explanation:** {question['explanation']}")
            
            # Display category if available
            if 'category' in question:
                st.write(f"**Category:** {question['category']}")

            # Handle question-type-specific fields
            if question.get('title') == "multiple_choice_question" and 'options' in question:
                st.write("**Options and Explanations:**")
                for option in question['options']:
                    st.write(f"- {option['option_text']} (Correct: {option['is_correct']})")
                    if 'explanation' in option:
                        st.write(f"  Explanation: {option['explanation']}")

            if question.get('title') == "situational_judgment_question" and 'options' in question:
                st.write("**Options and Effectiveness Ratings:**")
                for option in question['options']:
                    st.write(f"- {option['option_text']} (Effectiveness: {option['effectiveness_rating']})")
                    if 'explanation' in option:
                        st.write(f"  Explanation: {option['explanation']}")

            st.write("---")  # Separator between questions

        # Allow downloading the report
        st.download_button("Download Report", data="Report content here", file_name="report.txt")
    else:
        st.warning("No answers available. Please complete the quiz first.")
