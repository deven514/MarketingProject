import mysql.connector
from Utils import dbUtils


def getAllData():
    rowNum = []
    Asin = []
    BrandId = []
    starRating = []
    reviews = []


    connection = dbUtils.dbConnection()
    if (isinstance(connection, dict)):
        return connection
    else:
        sqlQuery = f"select sno, asin, brand_id, rating, cleaned_review_text from reviews where cleaned_review_text is not null"
        resultset = dbUtils.execStatement(connection, sqlQuery)
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
    connection = dbUtils.dbConnection()
    if (isinstance(connection, dict)):
        return connection
    else:
        sqlQuery = f"select asin, rating, reviews.cleaned_review_text from reviews  where brand_name is like %{brand}% and cleaned_review_text is not null and order by asin"
        resultset = dbUtils.execStatement(connection, sqlQuery)
        for row in resultset:
            Asin.append(row[0])
            starRating.append(row[1])
            reviews.append(row[2])
    return (Asin, starRating, reviews)


#

def getReviewsByAsin(asin):
    starRating = []
    reviews = []
    connection = dbUtils.dbConnection()
    if (isinstance(connection, dict)):
        return connection
    else:
        sqlQuery = f"select rating, reviews.cleaned_review_text from reviews  where brand_id = {asin} and cleaned_review_text is not null"
        resultset = dbUtils.execStatement(connection, sqlQuery)
        for row in resultset:
            starRating.append(row[0])
            reviews.append(row[1])
    return (starRating, reviews)

#

def getAllBrands():
    brandId = []
    brandName = []
    connection = dbUtils.dbConnection()
    if (isinstance(connection, dict)):
        return connection
    else:
        sqlQuery = f"select brand_id, brand_name from brands order by brand_id"
        resultset = dbUtils.execStatement(connection, sqlQuery)
        for row in resultset:
            brandId.append(row[0])
            brandName.append(row[1])
        return(brandId, brandName)





def getBrands():
    brandName = []
    connection = dbUtils.dbConnection()
    if (isinstance(connection, dict)):
        return connection
    else:
        sqlQuery = f"select brand_name from brands order by brand_name"
        resultset = dbUtils.execStatement(connection, sqlQuery)
        for row in resultset:
            brandName.append(row[0])
        return brandName


# rows, asin, BrandId, starRatings, reviews = getReviewsByBrand(207)
# print(reviews)











