## Implementation Plan  

1. **Phase 1**: Set up the basic structure and test each module individually.  
   - Start with `main.py` for basic navigation.  
   - Create a simple UI to choose question types.  

2. **Phase 2**: Integrate question generation.  
   - Implement `question_generator.py` and connect it to OpenAI.  
   - Validate generated questions against schemas.  
   - Test the `database.py` module for saving and loading questions.  

3. **Phase 3**: Build the quiz-taking UI.  
   - Use `quiz_renderer.py` to display questions and collect answers.  

4. **Phase 4**: Implement report generation.  
   - Process answers and use `report_generator.py` to create detailed AI-generated reports.  

5. **Phase 5**: Add scalability features.  
   - Implement user authentication (optional).  
   - Add more question types and reports.  


## Scalability Considerations  

- **Database**: Use SQLite or PostgreSQL for better scalability if JSON becomes cumbersome.  
- **APIs**: Modularize OpenAI API calls to switch to different providers if needed.  
- **UI Enhancements**: Add CSS styling for a polished look.  
- **Cloud Deployment**: Deploy the app using Streamlit Cloud or Heroku. 
- **Implement schema_validation.py using utils.pt** : Validate LLM output for robust app.
- **Add Diagram based question** : Generate image using midjourney/flux/dalle for image based question.
