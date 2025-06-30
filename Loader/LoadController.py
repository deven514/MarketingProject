from Helper import getDBData, LLMFunctions
from Utils.VectorDBUtils import createNewCollecttion


def main():

    # get all brands to load
    loadBrands()
    return None


def loadBrands():
    print("Updating Sentiment Score for reviews.")
    brandIds, brandNames = getDBData.getAllBrands()
    for i in range(len(brandIds)):
        brandId = brandIds[i]
        brandName = brandNames[i]
        rowNum, ASIN, reviews = getDBData.getBrandsForSentiments(brandId)
        print("Updating %s sentiment Scores..." % brandName)
        sentiments = LLMFunctions.getSentimentScores(reviews)
        if len(sentiments) > 1:
            for i in range(len(sentiments)):
                executed = getDBData.updateSentimentScore(rowNum[i], sentiments[i])
                if (not executed):
                    print("Failed to update sentiment score for %s." % brandName)

    return None








main()