from click import prompt
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_ollama import embeddings, OllamaEmbeddings, chat_models
from langchain_google_vertexai import VertexAIEmbeddings

from langchain_community.llms import ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate

#   NOTE:  For all sentiment analytics including getting a summary and a sentiment score Gemma 3 will be used.
#   Found that the sentiment Scoring and summaries are better with the Gemma model.
#   Llama can be used for any RAG and Chat functionality development.

modelLlama = "llama3.2:latest"
modelGemma = "Gemma3:latest"

## Leaving out the Embeddings for now.
# def getEmbeddings(reviews):
#     reviewEmbeddings = []
#     llm = OllamaEmbeddings(model=modelLlama, base_url="http://localhost:11434")
#
#     reviewEmbeddings.append(llm.embed_documents(reviews))
#     return reviewEmbeddings



def getSentimentScores(reviews):
    reviewSentiments = []
    llm = chat_models.ChatOllama(model=modelGemma, base_url="http://localhost:11434")
    systemMessage = SystemMessage("""Strickly provide a numerical value only between -1 and 1. Where -1 is most negative review, 
                      0 is a neutral review, and 1 is most positive review.""")
    for review in reviews:
        result = llm.invoke([systemMessage, review])
        reviewSentiments.append(float(result.content.strip("\n")))
    return reviewSentiments


def getSummary(reviews):
    llm = chat_models.ChatOllama(model=modelGemma,  base_url="http://localhost:11434")
    textSplitter = RecursiveCharacterTextSplitter(separators=["."], chunk_size=10000, chunk_overlap=500)
    splitRevs = textSplitter.create_documents(reviews)
    summary = load_summarize_chain(llm=llm, chain_type="stuff")
    result = summary.invoke(splitRevs)

    return result["output_text"]

def getComparativeAnalysis(prod1Name, prod1Reviews, prod2Name, prod2Reviews):
    llm = chat_models.ChatOllama(model=modelGemma, base_url="http://localhost:11434")
    textSplitter = RecursiveCharacterTextSplitter(separators=["."], chunk_size=10000, chunk_overlap=500)
    splitRev1 = textSplitter.create_documents(prod1Reviews)
    splitRev2 = textSplitter.create_documents(prod2Reviews)
    








# Messages = ["I love this product.",
#             "This product was good.",
#             "Just wished it had more colors.",
#             "Colors fade after the washed.",
#             "This is made with very poor quality products",
#             "It gave me an itch when wearing it.  Would not recomment it.",
#             "I did not like the product."
#             ]
# sentimentSummary = getSummary(Messages)
#
# print(sentimentSummary)