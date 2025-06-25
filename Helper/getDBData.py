from Utils import dbUtils


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
    procName = "SelectByBrand"
    args = []
    args.append(brand)
    resultset = dbUtils.callStoredProc(procName, args)
    for row in resultset:
        Asin.append(row[0])
        starRating.append(row[1])
        reviews.append(row[2])
    return (Asin, starRating, reviews)


#

def getReviewsByAsin(asin):
    starRating = []
    reviews = []
    title = []
    procName = "SelectReviewsByAsin"
    resultset = dbUtils.callStoredProc(procName, asin)
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





def getBrands():
    brandName = []
    procName = "SelectAllBrandNames"
    resultset = dbUtils.callStoredProc(procName)
    for row in resultset:
        brandName.append(row[0])
    return brandName







# title, starRating, reviews = getReviewsByBrand("Polo Store")
# print(reviews[1])




