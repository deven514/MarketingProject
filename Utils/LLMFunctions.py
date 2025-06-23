from click import prompt
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_ollama import embeddings, OllamaEmbeddings, chat_models
from langchain_community.llms import ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.prompts import PromptTemplate



model = "gemma3:latest"


def getEmbeddings(reviews):
    print("getting Embeddings")
    reviewsEmbeddings = []
    embed = OllamaEmbeddings(base_url="http://localhost:11434")
    for review in reviews:
        reviewsEmbeddings.append(embed.embed_documents(review))
    print("done")
    return reviewsEmbeddings



def getSentiments(reviews):
    reviewSentiments = []
    llm = chat_models.ChatOllama(model=model, base_url="http://localhost:11434")
    systemMessage = SystemMessage("Provide a sentiment score between -1 and 1 where -1 is most negative review and 1 is most positive review.  Strickly provide a numerical value only.")

    for review in reviews:

        result = llm.invoke([systemMessage, review])
        reviewSentiments.append(result.content)
    return reviewSentiments


def getSummary(reviews):
    llm = chat_models.ChatOllama(model=model,  base_url="http://localhost:11434")
    textSplitter = RecursiveCharacterTextSplitter(separators=["."], chunk_size=10000, chunk_overlap=500)
    splitRevs = textSplitter.create_documents(reviews)


    summary = load_summarize_chain(llm=llm, chain_type="stuff")
    result = summary.invoke(splitRevs)


    return result["output_text"]





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