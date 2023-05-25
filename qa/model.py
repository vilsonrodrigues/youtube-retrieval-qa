from typing import Callable

def load_llm(temperature: float = 0.0, model: str = 'gpt-3.5-turbo') -> Callable:
	from langchain.chat_models import ChatOpenAI
	llm = ChatOpenAI(temperature=temperature, model=model)
	return llm