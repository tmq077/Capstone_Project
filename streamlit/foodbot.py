#!/usr/bin/env python
# coding: utf-8

# In[15]:


import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader
from llama_index import download_loader
from PIL import Image


# In[19]:


# Set the GPT-3 api key
openai.api_key = st.secrets.openai_key


# In[16]:


SimpleWebPageReader = download_loader("SimpleWebPageReader")


# In[6]:

st.header("Chat with the Streamlit docs 💬 📚")

if "messages" not in st.session_state.keys(): # Initialize the chat message history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about Food Donation"}
    ]


# In[20]:


@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the Streamlit docs – hang tight! This should take 1-2 minutes."):
        loader = SimpleWebPageReader()
        urls = ['https://www.foodfromtheheart.sg/in-kind-donations','https://www.metta.org.sg/donation-in-kind/']        
        docs = loader.load_data(urls=urls)
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on Food Donations and your job is to answer questions. Assume that all questions are related to food donations."))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()


# In[21]:


chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)


# In[31]:


# Initialize session_state if not already defined
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Prompt for user input and save to chat history
if prompt := st.text_input("Your question"):  
    st.session_state.messages.append({"role": "user", "content": prompt})

# Display the prior chat messages
for message in st.session_state.messages:  
    with st.chat_message(message["role"]):
        st.write(message["content"])


# In[26]:


# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history


# In[ ]:




