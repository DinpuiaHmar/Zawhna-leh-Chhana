import streamlit as st
from deep_translator import GoogleTranslator
import ollama  # Ollama Python client

# Function to translate text
def translate(text, source_lang, target_lang):
    translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    return translated

# Function to generate an answer using Ollama
def generate_answer_with_ollama(question):
    try:
        # Use Ollama to generate an answer with deepseek-r1:1.5b
        response = ollama.generate(model="gemma2:2b", prompt=question)
        return response["response"]
    except Exception as e:
        return f"An error occurred while generating the answer: {e}"

# Custom CSS for aesthetics
def custom_css():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #000000;
        }
        .stTextInput input {
            background-color: #1a1a1a;
            color: #ffd700;
            border-radius: 10px;
            border: 1px solid #ffd700;
            padding: 10px;
        }
        .stButton button {
            background-color: #ffd700;
            color: #000000;
            border-radius: 10px;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #ffc107;
        }
        .answer-box {
            background-color: #1a1a1a;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #ffd700;
            margin-top: 20px;
            font-size: 18px;
            color: #ffd700;
            box-shadow: 0 4px 6px rgba(255, 215, 0, 0.1);
        }
        .disclaimer {
            background-color: #332f2c;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ffd700;
            margin-top: 10px;
            font-size: 14px;
            color: #ffd700;
            text-align: center;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #000000;
            color: #ffd700;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
        a {
            color: #ffc107;
            text-decoration: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Streamlit app
def main():
    # Apply custom CSS
    custom_css()

    # Title and description
    st.title("Zawhna leh Chhana")
    st.secrets["OLLAMA_API_KEY"]
    # Input text box for Mizo question
    mizo_question = st.text_input("I zawhna te zawt rawh", placeholder="I zawhna ziak rawh...")

    if mizo_question:
        # Translate Mizo question to English
        english_question = translate(mizo_question, source_lang="mizo", target_lang="en")
        
        # Generate answer in English using Ollama
        english_answer = generate_answer_with_ollama(english_question)
        
        # Translate English answer back to Mizo
        mizo_answer = translate(english_answer, source_lang="en", target_lang="mizo")
        
        # Display the answer in a styled box
        st.markdown(
            f"""
            <div class="answer-box">
                <strong>Chhana:</strong> {mizo_answer}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Disclaimer below the answer
        st.markdown(
            """
            <div class="disclaimer">
                <strong>Note:</strong> Chhana te hi a dik lo thei.
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Footer
    st.markdown(
        """
        <div class="footer">
            Developed by <strong>Laldinpuia Hmar</strong> | Email: <a href="mailto:hmardinpuia2002@gmail.com">hmardinpuia2002@gmail.com</a> | Model: <strong>gemma2:2b</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
