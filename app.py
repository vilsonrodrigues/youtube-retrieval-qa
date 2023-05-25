import os 
from typing import List
import gradio as gr
from qa.manager import YoutubeQA 

DESCRIPTION = """
Hello. This App will help you do questions on youtube videos.

1. Set your OpenAI Key
2. Set your Youtube URL
3. Ask
"""

qa = YoutubeQA()

def set_openai_key(key: str) -> None:    
    os.environ["OPENAI_API_KEY"] = key

def instanciate_retriver(url: str) -> None:
    qa.load_model()
    qa.load_vector_store(url)    
    qa.load_retriever()    

def generate(question: str) -> str:
    return qa.run(question)    

def respond(message: str, chat_history: List[str]):
    bot_message = qa.run(message)  
    chat_history.append((message, bot_message))
    return "", chat_history

with gr.Blocks() as app:

    gr.Markdown(DESCRIPTION)
    with gr.Tab("QA"):
        chatbot = gr.Chatbot(label="Bot Answer")
        question = gr.Textbox(label="Question", placeholder="Write your question here and press enter")    
        clear = gr.Button("Clear")
        question.submit(respond, [question, chatbot], [question, chatbot])
        clear.click(lambda: None, None, chatbot, queue=False)

    with gr.Tab("Youtube URL"):
        url = gr.Textbox(label="url", lines=1, placeholder="Set your Youtube URL here...")
        url_button = gr.Button("Set URL")

    with gr.Tab("OpenAI Key"):
        key = gr.Textbox(label="key", lines=1, placeholder="Set your OpenAI Key here...")
        key_button = gr.Button("Set Key")

    with gr.Accordion("Click me. About this App"):
        gr.Markdown("Look at me...")

    url_button.click(instanciate_retriver, inputs=url, outputs=None)
    key_button.click(set_openai_key, inputs=key, outputs=None)      

app.launch()