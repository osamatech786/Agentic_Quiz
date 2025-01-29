### 1. Multiple-Choice Questions (MCQs)

**Feasibility**: Very easy.  
**Example Use**: Cognitive ability (numerical, verbal, or logical reasoning).  
**How to Generate**: Prompt OpenAI to create a question and multiple answer choices.  

`prompt = "Generate a multiple-choice question for a numerical reasoning test with 4 answer options."`

---

### 2. True/False or Yes/No Questions  

**Feasibility**: Very easy.  
**Example Use**: Personality traits or work preferences.  
**How to Generate**: Prompt the model to create simple statements for candidates to agree or disagree with.  

`prompt = "Generate a true/false question to assess teamwork skills."`  

---

### 3. Rating Scale (Likert Scale) Questions  

**Feasibility**: Easy.  
**Example Use**: Measure agreement with personality traits or job-related behaviors.  
**How to Generate**: Ask OpenAI to generate a statement for a rating scale.  

`prompt = "Generate a statement for a personality test using a 1-5 Likert scale."`  

---

### 4. Open-Ended Questions  

**Feasibility**: Easy.  
**Example Use**: Assess problem-solving, conflict resolution, or leadership qualities.  
**How to Generate**: Use OpenAI to create reflective or situational questions.  

`prompt = "Generate an open-ended question to assess a candidate's conflict resolution skills."`  

---

### 5. Diagram-Based or Visual Questions  

**Feasibility**: Moderate (requires additional tools for image generation).  
**Example Use**: Abstract reasoning or pattern recognition.  
**How to Generate**: Use OpenAI to describe patterns or sequences, then generate diagrams with tools like DALL-E.  

`prompt = "Describe a pattern recognition question for an abstract reasoning test."`  

---

### 6. Situational Judgment Questions (SJT)  

**Feasibility**: Easy.  
**Example Use**: Evaluate decision-making and interpersonal skills.  
**How to Generate**: Prompt OpenAI to provide scenarios with multiple actions.  

`prompt = "Generate a situational judgment test question for a leadership role."`  

---

### 7. Timed Problem-Solving Questions  

**Feasibility**: Easy to generate but requires timer implementation in the app.  
**Example Use**: Numerical reasoning or coding challenges.  
**How to Generate**: Use OpenAI to create a challenging problem-solving question.  

`prompt = "Generate a challenging math problem for a timed psychometric test."`  

---

### 8. Personality-Based Scenario Questions  

**Feasibility**: Easy.  
**Example Use**: Assess personality traits like empathy, leadership, or adaptability.  
**How to Generate**: Ask OpenAI to create role-specific scenarios.  

`prompt = "Generate a scenario-based question to assess empathy in customer service."`  

---

### 9. Adaptive Questions  

**Feasibility**: Advanced (requires logic to adjust question difficulty).  
**Example Use**: Dynamic tests where questions get harder or easier based on performance.  
**How to Generate**: Prompt OpenAI to generate progressively harder or easier questions.  

`prompt = "Generate a set of 3 numerical reasoning questions with increasing difficulty."`  

---

### 10. Hypothetical or Role-Playing Questions  

**Feasibility**: Easy.  
**Example Use**: Assess candidates' decision-making in hypothetical scenarios.  
**How to Generate**: Prompt OpenAI to simulate a workplace scenario.  

`prompt = "Generate a hypothetical workplace scenario to assess decision-making."`  

---

## Example Code for Generating Questions  

```python
import openai

# OpenAI API key
openai.api_key = "your_openai_api_key"

# Prompt to generate a question
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Generate a multiple-choice question for a verbal reasoning test.",
    max_tokens=150
)

# Extract and print the question
print(response.choices[0].text.strip())
```

---

## Summary of Feasibility

![Summary of Feasibility](resources/Summary%20of%20Feasibility.png)

## Summary of Question Types Feasible with OpenAI API

![Summary of Question Types Feasible with OpenAI API](resources/Summary%20of%20Question%20Types%20Feasible%20with%20OpenAI%20API.png)