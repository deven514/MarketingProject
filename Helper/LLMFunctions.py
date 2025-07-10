from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import embeddings, OllamaEmbeddings, chat_models
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
import re
import logging

from langchain_ollama import chat_models
from langchain.chains import LLMChain



from sqlalchemy.testing.suite.test_reflection import metadata

from Utils import generalUtils



#   NOTE:  For all sentiment analytics including getting a summary and a sentiment score Gemma 3 will be used.
#   Found that the sentiment Scoring and summaries are better with the Gemma model.
#   Llama can be used for any RAG and Chat functionality development.


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
       if (review != ""):
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








def getComparativeAnalysis(brand1,  prod1Reviews,  brand2, prod2Reviews):
    llm = chat_models.ChatOllama(model=modelGemma, base_url="http://localhost:11434")
    reviews = []
    textSplitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=500)
    splitRev1 = textSplitter.create_documents(prod1Reviews)
    splitRev2 = textSplitter.create_documents(prod2Reviews)
    template = """ You are an expert in product review comparison and analysis.  Compare the following two sets of reviews
    context:{context}
    """
    for i in range(min(len(splitRev1), len(splitRev2))):
        reviews.append(splitRev1[i])
        reviews.append(splitRev2[i])

    prompt = ChatPromptTemplate.from_template(template=template)
    chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
    response=chain.invoke({"context": reviews})



    return response





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


#
# Messages1 = ["I love this product.",
#              "This product was good.",
#              "Just wished it had more colors.",
#              "Colors fade after the washed.",
#              "This is made with very poor quality products",
#              "It gave me an itch when wearing it.  Would not recomment it.",
#              "I did not like the product."
#              ]
#
#
# Messages2 = ["The fit was too tight. need to order a larger size.",
#              "This product is of  good quality.",
#              "I liked the wide range of colors.",
#              "Colors fade after the washed.",
#              "The shirt streatched after using them and wasing once.",
#              "I have had better quality products.",
#              "I did not like the product."
#              ]
# #
# print(summarizeReviews(Messages1))