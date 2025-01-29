import streamlit as st

def display_mcq(question, index):
    st.write(f"### Question {index + 1}: {question['question']}")
    options = [opt['option_text'] for opt in question['options']]
    selected = st.radio("Select an option:", options, key=f"mcq_{index}")
    st.session_state['answers'][index] = selected  # Store answer
    return selected
    
def display_true_false(question, index):
    st.write(f"### Question {index + 1}: {question['statement']}")
    selected = st.radio("Is this statement true or false?", ["True", "False"], key=f"true_false_{index}")
    st.session_state['answers'][index] = selected  # Store answer
    return selected

# Similar updates for other functions...
def display_likert(question, index):
    st.write(f"### Question {index + 1}: {question['statement']}")
    min_value = question['scale']['min_value']
    max_value = question['scale']['max_value']
    labels = question['scale']['labels']
    selected = st.slider(
        "Rate your agreement:", 
        min_value=min_value, 
        max_value=max_value, 
        step=1, 
        format=f"{labels[min_value - 1]}: %d"
    )
    st.session_state['answers'][index] = selected  # Store answer
    return selected

def display_open_ended(question, index):
    st.write(f"### Question {index + 1}: {question['question']}")
    answer = st.text_area("Your Answer:", key=f"open_ended_{index}")
    st.session_state['answers'][index] = answer  # Store answer
    return answer

def display_sjt(question, index):
    st.write(f"### Question {index + 1}: {question['scenario']}")
    options = [opt['option_text'] for opt in question['options']]
    answer = st.radio("Select the best action:", options, key=f"sjt_{index}")
    st.session_state['answers'][index] = answer  # Store answer
    return answer

def display_timed_problem_solving(question, index):
    st.write(f"### Question {index + 1}: {question['question']}")
    answer = st.text_input("Your Answer:", key=f"timed_{index}")
    st.session_state['answers'][index] = answer  # Store answer
    st.write(f"Time limit: {question['time_limit_seconds']} seconds")
    return answer

def display_adaptive(question, index):
    st.write(f"### Question {index + 1}: {question['questions'][0]['question_text']} (Easy)")
    easy_answer = st.text_input("Your Answer (Easy):", key=f"adaptive_easy_{index}")
    
    st.write(f"Follow-up (Hard): {question['questions'][1]['question_text']}")
    hard_answer = st.text_input("Your Answer (Hard):", key=f"adaptive_hard_{index}")
    
    # Store both answers as a tuple
    st.session_state['answers'][index] = {"easy": easy_answer, "hard": hard_answer}
    return st.session_state['answers'][index]

def display_hypothetical(question, index):
    st.write(f"### Question {index + 1}: {question['scenario']}")
    st.write(f"{question['question']}")
    answer = st.text_area("Your Answer:", key=f"hypothetical_{index}")
    st.session_state['answers'][index] = answer  # Store answer
    return answer

def display_personality_scenario(question, index):
    st.write(f"### Question {index + 1}: {question['scenario']}")
    st.write(f"{question['question']}")
    answer = st.text_area("Your Answer:", key=f"personality_{index}")
    st.session_state['answers'][index] = answer  # Store answer
    return answer
