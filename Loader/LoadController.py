from Helper import getDBData, LLMFunctions


def main():
    rowNum, Asin, BrandId, starRating, reviews = getDBData.getAllData()
    reviewVector = LLMFunctions.getEmbeddings(reviews)
    return None






main()