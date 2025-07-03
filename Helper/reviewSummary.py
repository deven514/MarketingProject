from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_ollama import chat_models
from langchain_core.documents import Document
from langchain.chains import LLMChain



def summarizeReviews(reviews):

   modelGemma = "Gemma3n:latest"
   llm = chat_models.ChatOllama(model=modelGemma, base_url="http://localhost:11434")
   documents = []
   for review in reviews:
       documents.append(Document(page_content=review))
   prompt = ChatPromptTemplate.from_template("Summarize the reviews: {context}")
   chain = create_stuff_documents_chain(llm, prompt)
   result = chain.invoke({"context":documents})
   return result



