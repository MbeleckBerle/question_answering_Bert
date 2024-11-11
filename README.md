Instructions:
ran out of GIT large file upload limit and couldn't upload the trained model
but you can retrain yourself.

The current version is setup for text files and can take multiple text files

1. run the notebook in google colab to train the model
2. in the model_test.py replace model path with the path of the model checkpoint

question_answerer = pipeline(
    "question-answering",
    model="<model checkpoint path>",
    device=0,
)

3. run model_test.py using "streamlit run model_test.py"

asdf