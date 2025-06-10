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



# rows, asin, BrandId, starRatings, reviews = getAllData()
# print(reviews)











