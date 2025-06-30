from Helper import getDBData, LLMFunctions, reviewSummary
import numpy as np



def getBrandInfo(brandName):
    ASIN, productName, ratings, reviews = getDBData.getReviewsByBrand(brandName)
    sentimentScores =  LLMFunctions.getSentimentScores(reviews)
    summary = reviewSummary.summarizeReviews(reviews)
    overallSentimentScore = np.mean(np.array(sentimentScores))


    return None





getBrandInfo("Polo Store")








