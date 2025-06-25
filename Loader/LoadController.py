from Utils import LLMFunctions, VectorDBUtils
from Helper import getDBData
from Utils.VectorDBUtils import createNewCollecttion


def main():

    # get all brands to load
    loadBrands()
    return None


def loadBrands():
    print("Loading Brands into VectorDB...")
    brandIds, brandNames = getDBData.getAllBrands()
    for i in range(len(brandIds)):
        brandId = brandIds[i]
        brandName = brandNames[i]
        print("Loading Brand %s into VectorDB..." % brandName)
        rowNum, Asins, starRatings, reviews = getDBData.getReviewsByBrand(brandId)
        embeddings = LLMFunctions.getEmbeddings(reviews)
        sentiments = LLMFunctions.getSentiments(reviews)
        metas = createDictValues(Asins, starRatings, sentiments, brandName)
        createNewCollecttion(brandName, embeddings, rowNum, reviews, metas)
    return None








def createDictValues(Asins, starRatings, sentiments, brandName):
    newDict = {}
    for i in range(len(Asins)):
        newDict['asin'] = Asins[i]
        newDict['starRating'] = starRatings[i]
        newDict['sentiment'] = sentiments[i]
        newDict['brandName'] = brandName
    return  newDict






main()