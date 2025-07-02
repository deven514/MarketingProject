from click import prompt
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_ollama import embeddings, OllamaEmbeddings, chat_models
from langchain.chains.summarize import load_summarize_chain
from langchain.chains.llm import LLMChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
import re
import logging
from Utils import generalUtils



#   NOTE:  For all sentiment analytics including getting a summary and a sentiment score Gemma 3 will be used.
#   Found that the sentiment Scoring and summaries are better with the Gemma model.
#   Llama can be used for any RAG and Chat functionality development.

modelLlama = "llama3.2:latest"
modelGemma = "Gemma3n:latest"

## Leaving out the Embeddings for now.
# def getEmbeddings(reviews):
#     reviewEmbeddings = []
#     llm = OllamaEmbeddings(model=modelLlama, base_url="http://localhost:11434")
#
#     reviewEmbeddings.append(llm.embed_documents(reviews))
#     return reviewEmbeddings
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s',
                    filename='F:/devprojects/python\MarketingProject/logs/llama.log', filemode='w')


def getSentimentScores(reviews):
    reviewSentiments = []
    logging.info("getSentimentScores")



    llm = chat_models.ChatOllama(model=modelGemma, base_url="http://localhost:11434")
    systemMessage = SystemMessage("""You are a helpful agent that provides a sentiment score for product reviews.
                    The score should have a value between -1 to 1.  Where -1 is the most negative sentiment for a review.
                    0 is a neutral sentiment and 1 is a positive sentiment. The output should only be the sentiment score.""")
    scoreFloat = 0.0
    for review in reviews:
       logging.info("The Review is: " + review)
       result = llm.invoke([systemMessage, review])
       logging.info("The Sentiment Score is: " + result.content)
       score = result.content
       score = re.sub(r"-[0-9]", "", score)
       score = score.strip("\n")
       logging.info("The Sentiment Score after clean up is: " + score)
       if ((score == "") or (len(score) > 5)):
          logging.info("RETRYYING: " + review)
          msg = "Provide a numerical sentiment score for the review."
          result = llm.invoke([msg, review])
          logging.info("The Sentiment Score is: " + result.content)
       if ((len(score) > 0) and (generalUtils.floatConvertible(score))):
           scoreFloat = float(score)
           reviewSentiments.append(scoreFloat)




    return reviewSentiments





def getSummary(reviews):
    llm = chat_models.ChatOllama(model=modelGemma,  base_url="http://localhost:11434")
    textSplitter = RecursiveCharacterTextSplitter(separators=["."], chunk_size=10000, chunk_overlap=500)
    splitRevs = textSplitter.create_documents(reviews)
    summary = load_summarize_chain(llm=llm, chain_type="stuff")
    result = summary.invoke(splitRevs)
    return result["output_text"]



# def getComparativeAnalysis(prod1Name, prod1Reviews, prod2Name, prod2Reviews):
#     llm = chat_models.ChatOllama(model=modelGemma, base_url="http://localhost:11434")
#     textSplitter = RecursiveCharacterTextSplitter(separators=["."], chunk_size=10000, chunk_overlap=500)
#     splitRev1 = textSplitter.create_documents(prod1Reviews)
#     splitRev2 = textSplitter.create_documents(prod2Reviews)
    








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