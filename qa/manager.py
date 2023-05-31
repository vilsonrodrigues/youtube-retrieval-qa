from qa.chains import conversational_retrieval_qa, retrieval_qa
from qa.loader import youtube_doc_loader
from qa.model import load_llm
from qa.split import split_document
from qa.vector_store import create_vector_store

class YoutubeQA:

    def __init__(self):
        self.CHAT_MODE = 'normal' 

    def change_chat_mode(self, mode: str) -> None:       
        self.CHAT_MODE = mode

    def load_model(self) -> None:
        self.llm = load_llm()

    def load_vector_store(self, url: str) -> None:
        data = youtube_doc_loader(url=url)
        docs = split_document(data=data)
        self.retriver = create_vector_store(docs=docs)
     
    def load_retriever(self) -> None:
        if self.CHAT_MODE == 'normal':
            self.retrieval_qa = retrieval_qa(llm=self.llm, retriever=self.retriver)
        elif self.CHAT_MODE == 'conversational':
            self.retrieval_qa = conversational_retrieval_qa(llm=self.llm, retriever=self.retriver)
        else:
            raise ValueError('Chat Mode not implemented')

    def run(self, question: str) -> str:
        if self.CHAT_MODE == 'normal':
            return self.retrieval_qa.run(question)
        elif self.CHAT_MODE == 'conversational':
            return self.retrieval_qa({'question': question})['answer']