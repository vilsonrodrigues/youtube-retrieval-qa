# 🤖ChatTube🎥

## Youtube Retrieval QA System

🤭 Hello! In this project we will dive into our exciting work carried out in the Postgraduate discipline of Sequential Models, taught by professor [Ivanovitch Silva](http://github.com/ivanovitchm), and offered by PPGEEC/UFRN. 

This simple system allows users to engage in conversations about a YouTube video with itself, without the need to watch it firsthand. For this project, our group participants are [Deborah Moreira](http://github.com/deborahmoreira), [Miguel Euripedes](https://github.com/MiguelEuripedes) and myself.

By using this app you can ask ChatGPT questions about things in a video. To minimize the cost per token, we use a Vector Store to perform a semantic search and return the most related documents.

The architecture is divided into two parts, data ingestion and information retrieval to feed ChatGPT (LLM).

We produced two explanatory materials about the architecture, a video about the architecture at a high level and a medium post with detailed content.

[![Open in Youtube](https://img.shields.io/badge/-Youtube-red?style=flat-square&logo=youtube)](https://youtu.be/SntK5OPyUXQ) [![Open in Medium](https://img.shields.io/badge/-Medium-black?style=flat-square&logo=medium)](https://vilsonrodrigues.medium.com/chattube-chat-with-youtube-video-46a0bfc0a2e9)

### Getting Started

![](images/app_hf_spaces.png)

#### HuggingFace Spaces 🚀

Simpler, 🎮 play on 

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/vilsonrodrigues/youtube-retrieval-qa)

#### Colab 👩🏼‍💻

Run notebook in <i>[notebooks/YoutubeRetrievalQA.ipynb](notebooks/YoutubeRetrievalQA.ipynb)</i>

#### To local run 🚴🏾‍♀️

Install dependencies:

``` pip3 install -r requirements.txt ``` 

Run Gradio app:

``` python3 app.py ``` 

### Architecture 

#### Ingestion

In short, in pipeline ingestion we have:

![](images/ingestion_pipeline.png)

#### Retrieval QA 

To retrieval, the first option is stateless app

![](images/retrieval_pipeline.png)

#### Conversational Retrieval QA 

The second option is a chain with a memory object

![](images/conversational_retrieval_pipeline.png)