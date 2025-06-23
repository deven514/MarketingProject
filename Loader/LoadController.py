from Utils import LLMFunctions
from Helper import getDBData


def main():
    rowNum, Asin, BrandId, starRating, reviews = getDBData.getReviewsByBrand(207)
    reviewVector = LLMFunctions.getEmbeddings(reviews)
    sentiments = LLMFunctions.getSentiments(reviews)
    print(sentiments)
    return None






main()
