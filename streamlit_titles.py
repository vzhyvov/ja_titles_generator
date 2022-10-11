import torch
import streamlit as st
from transformers import pipeline
text1 = "Married, but getting a divorce. Husband filed for emergency custody of my child. He is not biologically related. Haven't been served yet. What are my options to getting my child back"
text2 = 'What is the most likely cause of a single small low density liver lesion?'
text3 = "Hello, my ex husband and I already have a order in place since 2013 with joint custody for our 2 daughter. They moved on 8/3/2019 to Tennessee. My youngest daughter who is 14 wants to move home. She is unhappy and misses her family and myself. How do I go about modifying the order or what steps do I have to take to get her home. When they moved I wrote a statement that was notarized that they were able to go with stipulations. She really wants to come home. She is unhappy and depressed. I'm afraid he won't be understanding and force her to stay. He does not work. My eldest daughter who is 17, soon to be 18 works and supports the Bill's"

st.title('Title generation Demo')

_max_length = 11

col_1, col_2, col_3 = st.columns(3)
_max_length = col_1.number_input("Title max number of words", value=_max_length)

text = st.text_area('Text Input', text1)

def run_model(input_text):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = pipeline("summarization", model="google/pegasus-xsum", max_length=_max_length)
    input_text = str(input_text)
    output = model(input_text)[0]['summary_text']
    st.write('Title')
    st.success(output)

if st.button('Convert'):
    run_model(text)
