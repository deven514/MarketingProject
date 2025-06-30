from Utils import dbUtils
#  IMPORTANT NOTE:  For Stored procs that need parameters should be in a list.

def getAllData():
    rowNum = []
    Asin = []
    BrandId = []
    starRating = []
    reviews = []
    procName = "selectAllData"
    resultset = dbUtils.callStoredProc(procName)
    for row in resultset:
        rowNum.append(row[0])
        Asin.append(row[1])
        BrandId.append(row[2])
        starRating.append(row[3])
        reviews.append(row[4])
    return (rowNum, Asin, BrandId, starRating, reviews)


def getReviewsByBrand(brand):
    Asin = []
    starRating = []
    reviews = []
    productName = []
    procName = "SelectByBrand"
    args = []
    args.append(brand)
    resultset = dbUtils.callStoredProc(procName, args)
    for row in resultset:
        Asin.append(row[0])
        productName.append(row[1])
        starRating.append(row[2])
        reviews.append(row[3])
    return (Asin,productName ,starRating, reviews)


#

def getReviewsByAsin(asin):
    starRating = []
    reviews = []
    title = []
    procName = "SelectReviewsByAsin"
    args = []
    args.append(asin)
    resultset = dbUtils.callStoredProc(procName, args)
    for row in resultset:
        title.append(row[0])
        starRating.append(row[1])
        reviews.append(row[2])
    return (title, starRating, reviews)

#

def getAllBrands():
    brandId = []
    brandName = []
    procName = "selectAllBrands"
    resultset = dbUtils.callStoredProc(procName)
    for row in resultset:
        brandId.append(row[0])
        brandName.append(row[1])
    return(brandId, brandName)


def getBrandsNames():
    brandName = []
    procName = "SelectAllBrandNames"
    resultset = dbUtils.callStoredProc(procName)
    for row in resultset:
        brandName.append(row[0])
    return brandName


def getBrandsForSentiments(brandId):
    rowNum = []
    asin = []
    reviews = []
    procName = "SelectBrandsSentiment"
    args = []
    args.append(brandId)
    resultset = dbUtils.callStoredProc(procName, args)
    for row in resultset:
        rowNum.append(row[0])
        asin.append(row[1])
        reviews.append(row[2])
    return rowNum, asin, reviews


def updateSentimentScore(rowNum, sentimentScore):
    procName = "updateSentimentScore"
    args= []
    args.append(rowNum)
    args.append(sentimentScore)
    rowsUpd = dbUtils.callStoredUpdateProc(procName, args)
    if (rowsUpd > 0 ):
        return True
    return False


# title, starRating, reviews = getReviewsByBrand("Polo Store")
# print(reviews[1])




