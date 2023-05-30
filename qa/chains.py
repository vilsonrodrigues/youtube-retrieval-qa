from typing import Callable

def retrieval_qa(llm: Callable, retriever: Callable) -> Callable: 
    from langchain.chains import RetrievalQA
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    return qa

def conversational_retrieval_qa(llm: Callable, retriever: Callable) -> Callable: 
    from langchain.memory import ConversationBufferMemory
    from langchain.chains import ConversationalRetrievalChain
    memory = ConversationBufferMemory(memory_key="chat_history", 
                                  return_messages=True)
    qa = ConversationalRetrievalChain.from_llm(
            llm, 
            retriever=retriever, 
            memory=memory)    
    return qa
