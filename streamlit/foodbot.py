#!/usr/bin/env python
# coding: utf-8

# In[15]:


import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
import json
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex
from llama_index import download_loader

# In[19]:


# Set the GPT-3 api key
openai.api_key = st.secrets.openai_key

SimpleWebPageReader = download_loader("SimpleWebPageReader")
loader = SimpleWebPageReader()
documents = loader.load_data(urls=['https://www.metta.org.sg/donation-in-kind/'])
index = GPTVectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

class Chatbot:
    def __init__(self, api_key, index):
        self.index = index
        openai.api_key = api_key
        self.chat_history = []

    def generate_response(self, user_input):
        query_engine = index.as_query_engine()
        response = query_engine.query(user_input)

        message = {"role": "assistant", "content": response.response}
        self.chat_history.append({"role": "user", "content": user_input})
        self.chat_history.append(message)
        return message

    def load_chat_history(self, filename):
        try:
            with open(filename, 'r') as f:
                self.chat_history = json.load(f)
        except FileNotFoundError:
            pass

    def save_chat_history(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.chat_history, f)

# Create a Streamlit app
st.title("Chatbot Application")

# Initialize the Chatbot
bot = Chatbot(api_key, index=index)
bot.load_chat_history("chat_history.json")

user_input = st.text_input("You:", "")
if user_input.lower() in ["bye", "goodbye"]:
    st.write("Bot: Goodbye!")
    bot.save_chat_history("chat_history.json")
else:
    if st.button("Submit"):
        response = bot.generate_response(user_input)
        st.write(f"Bot: {response['content']}")
