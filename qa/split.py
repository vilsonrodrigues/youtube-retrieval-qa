from typing import List

def split_document(data: List, chunk_size: int = 3000) -> List:
	from langchain.text_splitter import RecursiveCharacterTextSplitter
	text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=400)
	docs = text_splitter.split_documents(data)
	return docs