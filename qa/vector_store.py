from typing import Callable, List

def create_vector_store(
    docs: List,
    metric: str = 'cos',
    top_k: int = 4
) -> Callable:
    
    from langchain.vectorstores import FAISS
    from langchain.embeddings.openai import OpenAIEmbeddings
    
    embeddings = OpenAIEmbeddings()
    
    # Embed your documents and combine with the raw text in a pseudo db. 
    # Note: This will make an API call to OpenAI
    docsearch = FAISS.from_documents(docs, embeddings)
    
    # Retriver object
    retriever = docsearch.as_retriever()
    
    # Retriver configs
    retriever.search_kwargs['distance_metric'] = metric
    retriever.search_kwargs['k'] = top_k

    return retriever