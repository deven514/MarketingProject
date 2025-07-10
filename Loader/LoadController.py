from Helper import getDBData, LLMFunctions
import logging
from Utils.VectorDBUtils import createNewCollecttion

debug = False

def main(debugStatus = False):

   # get all brands to load
    debug = debugStatus
 #  loadBrands()

    return None


def loadBrands():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s',
                        filename='F:/devprojects/python\MarketingProject/logs/llama.log', filemode='w')
    print("Updating Sentiment Score for reviews.")

    brandIds, brandNames = getDBData.getAllBrands()
    for i in range(len(brandIds)):
        brandId = brandIds[i]
        brandName = brandNames[i]
        rowNum, ASIN, reviews = getDBData.getBrandsForSentiments(brandId)
        logging.info("The Brand is: " + brandName)
        print("Updating %s sentiment Scores..." % brandName)
        logging.info("Updating %s sentiment Scores..." % brandName)
        sentiments = LLMFunctions.getSentimentScores(reviews)
        if len(sentiments) > 1:
            for i in range(len(sentiments)):
                executed = getDBData.updateSentimentScore(rowNum[i], sentiments[i])
                if (not executed):
                    print("Failed to update sentiment score for %s." % brandName)
    return None









main(True)