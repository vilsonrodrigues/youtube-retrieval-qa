import os 
from typing import List
import gradio as gr
from qa.manager import YoutubeQA 

DESCRIPTION = """

<h1> <center> 🤗 Hello. This App will help you do questions on youtube videos.</center> </h1>

<h4>
Follow these steps to use 😉:
</h4>

<ol>
  <li>Set your OpenAI Key</li>
  <li>Set your Youtube URL</li>
  <li>Ask!</li>
</ol> 
"""

qa = YoutubeQA()

def change_chat_mode(radio: str):
    if radio == "conversational":
        qa.change_chat_mode(radio)

def set_openai_key(key: str):    
    os.environ["OPENAI_API_KEY"] = key
    # Set status field to Not Ready
    return gr.update(lines=1, value="Not Ready 🥴")

def instanciate_retriver(url: str):
    qa.load_model()
    qa.load_vector_store(url)    
    qa.load_retriever()   
    # Set status field to Ready 
    return gr.update(lines=1, value="Ready 😎")

def respond(message: str, chat_history: List[str]):
    bot_message = qa.run(message)  
    chat_history.append((message, bot_message))
    return "", chat_history

with gr.Blocks() as app:

    gr.Markdown(DESCRIPTION)
    with gr.Tab("QA"):
        status = gr.Textbox(label="🤔 Vector DB Status:", interactive=False)            
        chatbot = gr.Chatbot(label="🤖 Bot Answer:")
        question = gr.Textbox(label="🕵️‍♀️ Question:", placeholder="Write your question here and press enter")    
        clear = gr.Button("Clear")
        question.submit(respond, [question, chatbot], [question, chatbot])
        clear.click(lambda: None, None, chatbot, queue=False)

    with gr.Tab("Youtube URL"):
        url = gr.Textbox(label="🎞️ URL:", lines=1, placeholder="Set your Youtube URL here...")
        url_button = gr.Button("Set URL")

    with gr.Tab("OpenAI Key"):
        key = gr.Textbox(label="🔑 Key:", type="password", placeholder="Set your OpenAI Key here...")
        key_button = gr.Button("Set Key")

    with gr.Tab("Chat Mode (optional)"):
        radio = gr.Radio(
            ["normal", "conversational"], 
            label="If conversational, history is kept in prompt",
            value="normal"
        )
        radio.change(fn=change_chat_mode, inputs=radio, outputs=None)

    with gr.Accordion("Click me. About this App"):        
        gr.Markdown("[![Open in Medium](https://img.shields.io/badge/-Medium-black?style=flat-square&logo=medium)](https://vilsonrodrigues.medium.com/chattube-chat-with-youtube-video-46a0bfc0a2e9)")

    url_button.click(instanciate_retriver, inputs=url, outputs=status)
    key_button.click(set_openai_key, inputs=key, outputs=status)      

app.launch()