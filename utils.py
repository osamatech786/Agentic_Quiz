import requests
import streamlit as st
from jsonschema import validate

def validate_data(data, schema):
    try:
        validate(instance=data, schema=schema)
        return True
    except Exception as e:
        return False

def generate_unique_id():
    try:
        response = requests.get("https://www.uuidtools.com/api/generate/v1")
        if response.status_code == 200:
            unique_id = response.json()[0]
            return unique_id
        else:
            st.warning("Error generating unique ID, fallback to internal ID.")
            return "fallback_id_1234"  # Use a fallback ID in case of API failure
    except Exception as e:
        st.warning(f"Error generating unique ID: {e}, using fallback.")
        return "fallback_id_1234"  # Fallback to a safe default ID