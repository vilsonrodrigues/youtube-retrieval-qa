from qa.chains import retrieval_qa
from qa.loader import youtube_doc_loader
from qa.model import load_llm
from qa.split import split_document
from qa.vector_store import create_vector_store

class YoutubeQA:

    def __init__(self):
        pass

    def load_model(self) -> None:
        self.llm = load_llm()

    def load_vector_store(self, url: str) -> None:
        data = youtube_doc_loader(url=url)
        docs = split_document(data=data)
        self.retriver = create_vector_store(docs=docs)
     
    def load_retriever(self) -> None:
        self.retrieval_qa = retrieval_qa(llm=self.llm, retriever=self.retriver)

    def run(self, question: str) -> str:
        return self.retrieval_qa.run(question)
