import streamlit as st
import requests

# Define the backend URL
backend_url = "http://127.0.0.1:5000/process"

# Define the available languages
languages = ["English", "Spanish", "French", "German", "Chinese"]

# Inject custom CSS
st.markdown(
    """
    <style>
    .stSelectbox div[data-baseweb="select"] {
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Set up the theme toggle
def set_theme():
    if st.session_state["dark_mode"]:
        st.write(
            """
            <style>
            :root {
                --primary-color: #1a1a1a;
                --background-color: #333;
                --text-color: #f1f1f1;
                --button-color: #444;
                --button-text-color: #f1f1f1;
                --input-color: #444;
                --input-text-color: #f1f1f1;
            }
            body {
                background-color: var(--background-color);
                color: var(--text-color);
            }
            .stButton>button {
                background-color: var(--button-color);
                color: var(--button-text-color);
            }
            .stTextInput>div>div>input {
                background-color: var(--input-color);
                color: var(--input-text-color);
            }
            .stSelectbox>div>div>div {
                background-color: var(--input-color);
                color: var(--input-text-color);
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.write(
            """
            <style>
            :root {
                --primary-color: #ffffff;
                --background-color: #f1f1f1;
                --text-color: #000000;
                --button-color: #e0e0e0;
                --button-text-color: #000000;
                --input-color: #ffffff;
                --input-text-color: #000000;
            }
            body {
                background-color: var(--background-color);
                color: var(--text-color);
            }
            .stButton>button {
                background-color: var(--button-color);
                color: var(--button-text-color);
            }
            .stTextInput>div>div>input {
                background-color: var(--input-color);
                color: var(--input-text-color);
            }
            .stSelectbox>div>div>div {
                background-color: var(--input-color);
                color: var(--input-text-color);
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

# Create a toggle for dark mode
st.sidebar.title("Settings")
dark_mode = st.sidebar.checkbox("Dark Mode", value=False)
st.session_state["dark_mode"] = dark_mode

# Apply the theme
set_theme()

st.title("Language Translator")

# Create a form with three inputs
with st.form(key="translator_form"):
    from_language = st.selectbox("From this", languages)
    to_language = st.selectbox("To this", languages)
    text = st.text_input("Enter text to translate")
    
    # Submit button
    submit_button = st.form_submit_button(label="Translate")

# If the form is submitted
if submit_button:
    # Prepare the data to be sent to the backend
    data = {
        "from_language": from_language,
        "to_language": to_language,
        "text": text,
    }
    
    # Send a POST request to the backend
    response = requests.post(backend_url, json=data)
    
    # Get the response from the backend
    result = response.json().get("result")
    
    # Display the result
    st.write("Translation Result:")
    st.write(result)
