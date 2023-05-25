from typing import Callable

def retrieval_qa(llm: Callable, retriever: Callable) -> Callable: 
    from langchain.chains import RetrievalQA
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    return qa