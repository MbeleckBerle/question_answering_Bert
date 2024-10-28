import streamlit as st
from transformers import pipeline

# Load the question-answering pipeline with your fine-tuned model
question_answerer = pipeline(
    "BERLE_GPT",
    model="/home/mojo/projects/question_answering_Bert/question_answering_model/checkpoint-21900",
    device=0,
)


# Function to read text from a file
def load_context_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        context = file.read()
    return context


# Streamlit UI
st.title("Question Answering App")

# File uploader for the text file
uploaded_file = st.file_uploader("Upload a text file with context", type=["txt"])

if uploaded_file is not None:
    context = uploaded_file.read().decode("utf-8")
    st.text_area("Context", context, height=200)

    user_question = st.text_input("Enter your question:")

    if st.button("Get Answer"):
        if user_question:
            result = question_answerer(question=user_question, context=context)
            st.write("**Answer:**", result["answer"])

            st.write("**Confidence Score:**", result["score"])
        else:
            st.warning("Please enter a question.")
