#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from streamlit_chat import message
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
import tempfile
import openai
import base64
from PIL import Image


# In[2]:


# Set the GPT-3 api key
openai.api_key = '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'


# In[6]:


# Set the page background

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.title("***CHATBOT FOR PUBLIC & CUSTOM DATA***")
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    
add_bg_from_local('img1.jpg') 


# In[7]:


# Left pane
uploaded_file = st.sidebar.file_uploader("Upload file here for personal chatbot: ", type="csv")

if uploaded_file :
   #use tempfile because CSVLoader only accepts a file_path
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    loader = CSVLoader(file_path=tmp_file_path, encoding="utf-8", csv_args={'delimiter': ','})
    data = loader.load()


# In[10]:


with personal_chatbot:
    st.header("Ask questions to personal chatbot: ")

    if uploaded_file :
        #use tempfile because CSVLoader only accepts a file_path
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name

            loader = CSVLoader(file_path=tmp_file_path, encoding="utf-8", csv_args={'delimiter': ','})
            data = loader.load()
            embeddings = OpenAIEmbeddings()
            vectorstore = FAISS.from_documents(data, embeddings)
            chain = ConversationalRetrievalChain.from_llm(
            llm = ChatOpenAI(temperature=0.0,model_name='gpt-3.5-turbo'),
            retriever=vectorstore.as_retriever())

            def conversational_chat(query):
                placeholder = st.empty()
                result = chain({"question": query, "chat_history": st.session_state['history']})
                st.session_state['history'].append((query, result["answer"]))
                
                return result["answer"]
            
            if 'history' not in st.session_state:
                st.session_state['history'] = []
           
            if 'generated' not in st.session_state:
                st.session_state['generated'] = ["Hi! Ask anything from uploaded " + uploaded_file.name[:-4]]

            if 'past' not in st.session_state:
                st.session_state['past'] = ["Hi"]

            #container for the chat history
            response_container = st.container()
            #container for the user's text input
            container = st.container()

            with container:
                st.write("Please ask anything to your personal chatbot...")
                with st.form(key='my_form', clear_on_submit=True):
                
                    user_input = st.text_input("Query:", placeholder="Ask questions from personal csv file uploaded", key='input')
                    submit_button = st.form_submit_button(label='Send')
                    
                if submit_button and user_input:
                    output = conversational_chat(user_input)
                    st.session_state['generated'].append(output)
                    st.session_state['past'].append(user_input)
                    
                    

            if st.session_state['generated']:
                with response_container:
                    for i in range(len(st.session_state['generated'])):
                        message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style = "big-ears-neutral")
                        message(st.session_state["generated"][i], key=str(i), avatar_style="fun-emoji")


# In[ ]:




