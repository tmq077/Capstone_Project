# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Capstone Project: "DonateFoodGoWhere" - Chatbot for donating specific food items in Singapore

### Problem Statement

In 2022, Singapore generated 813 million kg of food waste, accounting for 11% of total waste generated. Annually, each household throws away $258 worth of food, equivalent of 52 plates of nasi lemak (assuming each plate cost $5). The amount of food waste has grown by 20% over the past 10 years, and is expected to rise further. At current rate of waste disposal, Singapore will need a new incineration plant every 7-10 years, and a new landfill every 30-35 years.

Households contribute around half of the food waste generated. As part of Singapore’s Zero Waste Masterplan, one key component of food waste management strategies is encouraging members of public to donate excess food. Organisations that accept food donations have specific wish list of food items and donation requirements, and it is time-consuming for individuals to find the right organisation for the food they wish to donate.

This project aims to explore how we can help link individuals up with organisations, by developing a chatbot for individuals to enquire about donating specific food items, and find out where and how to donate, along with the relevant donation instructions.

_Resources:_
- https://www.nea.gov.sg/our-services/waste-management/3r-programmes-and-resources/food-waste-management
- https://sec.org.sg/pdf/e-newsletter/e-news-23012020.pdf
- https://www.towardszerowaste.gov.sg/foodwaste/
- https://www.towardszerowaste.gov.sg/zero-waste-nation/
- https://www.towardszerowaste.gov.sg/zero-waste-masterplan/chapter3/food/

---

### Data Used

Data is saved from the website of various organisations that accept food donation, in PDF and html format. These are in [`webpages`](/code/webpages).

---

### Python Notebook Description

* [`rag_finetuning`](/code/rag_finetuning.ipynb): Workflow for implementing RAG and Fine-tuning, and evaluation of the model pipeline
* [`foodbot.py`](/streamlit/foodbot.py): Deployment of chatbot in streamlit

---

### Conclusion

- To build a custom chatbot, this project explored the use of OpenAI's ChatGPT Large Language Model (GPT-3.5-Turbo), Retrieval Augmented Generation (RAG), and Fine-tuning.
- The RAG + GPT-3.5-Turbo model pipeline yields an answer relevancy of 0.97 and faithfulness of 0.87, indicating the model is able to generate concise and informative answers that are derived from the external dataset with minimal hallucinations. 
- With this model pipeline, a chatbot is developed and deployed on streamlit ([https://donatefoodgowhere.streamlit.app/](https://donatefoodgowhere.streamlit.app/)) to help individual food donors find the right organisations for donating their specific food items, along with additional donation information. 
  
---

### Resources

How chatbot works:
- https://bea.stollnitz.com/blog/how-gpt-works-technical/
- https://www.linkedin.com/pulse/chatgpt-how-language-model-generating-response-base-text-manish-joshi/
- https://www.linkedin.com/pulse/demystifying-magic-behind-chatgpt-generative-ai-donovan-rittenbach/?trk=public_post

RAG and Fine-tuning
- https://www.rungalileo.io/blog/optimizing-llm-performance-rag-vs-finetune-vs-both#:~:text=Fine%2Dtuning%20helps%20adapt%20the,knowledge%20sources%20through%20retrieval%20mechanisms.
- https://medium.com/@sagarpatiler/fine-tuning-vs-rag-in-generative-ai-64d592eca407
- https://deci.ai/blog/fine-tuning-peft-prompt-engineering-and-rag-which-one-is-right-for-you/
- https://blog.gopenai.com/using-llm-for-q-a-with-retrieval-augmented-generation-bee905dea160
- https://blog.ml6.eu/leveraging-llms-on-your-domain-specific-knowledge-base-4441c8837b47
- https://iwasnothing.medium.com/how-to-build-custom-domain-q-a-chatbot-using-llm-13827fbcdbed

Evaluation
- https://github.com/explodinggradients/ragas/tree/main/docs/concepts/metrics
- https://medium.aiplanet.com/evaluate-rag-pipeline-using-ragas-fbdd8dd466c1
- https://cobusgreyling.medium.com/rag-evaluation-9813a931b3d4https://blog.langchain.dev/evaluating-rag-pipelines-with-ragas-langsmith/

