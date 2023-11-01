#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import the required libraries
import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import StorageContext, load_index_from_storage


# In[ ]:


# Set OpenAI API key through the streamlit app's secrets
openai.api_key = st.secrets.openai_key


# In[ ]:


# Add a heading for the app
st.header("Ask me about food donations in Singapore!")


# In[ ]:


# Session state to keep track of chatbot's message history
if "messages" not in st.session_state.keys(): # Initialize the chat message history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about food donation in Singapore"}
    ]


# In[ ]:


# Load and index data
@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing food donation docs – hang tight! This should take 1-2 minutes."):
        # Rebuild the storage context
        storage_context = StorageContext.from_defaults(persist_dir="streamlit/data/index.vecstore")

        # Load the index
        index = load_index_from_storage(storage_context)

        # Load the model 
        gpt_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0), context_window=2048, system_prompt="You are an expert in helping individual food donor looking to donate specific food items and your job is to answer questions using the provided context from documents on different food support organisations. All questions are related to the food support organisations documents. Restrict the answer to the context information provided, and answer with the name of the food support organisations, any requirements for the donated food, methods to donate the food, and contact information – do not hallucinate features.")
        return index

index = load_data()


# In[ ]:


# Create chat engine
chat_engine = index.as_chat_engine(chat_mode="context", verbose=True)


# In[ ]:


# Prompt for user input and display message history
if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])


# In[ ]:


# Pass query to chat engine and display response
# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history

