from Helper import getDBData, getLLMEmbeddings


def main():
    rowNum, Asin, BrandId, starRating, reviews = getDBData.getAllData()
    reviewVector = getLLMEmbeddings.getEmbeddings(reviews)
    return None






main()