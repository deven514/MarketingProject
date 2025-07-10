from fastapi import FastAPI
import pandas as pd
from Helper import LLMFunctions



import uvicorn

from Helper import getDBData
from Utils import generalUtils

app = FastAPI()

@app.get("/")
async def root():
    return ({"Info:": "Marketing API"} )

@app.get("/getAllBrands")
async def getAllBrands():
    brands = getDBData.getBrandsNames()
    table = pd.DataFrame(brands)
    return table.to_csv()


@app.get("/getBrand")
async def getBrand(brandName: str):
    asin, productNames, starRatings, reviews, sentimentScores = getDBData.getReviewsByBrand(brandName.strip('"'))
    table = pd.DataFrame()
    table["asin"] = asin
    table["productNames"] = productNames
    table["starRatings"] = starRatings
    table["reviews"] = reviews
    table["sentimentScores"] = sentimentScores
    return table.to_csv()

@app.get("/getByAsin")
async def getByAsin(asin: str):
    brandNames, starRatings, reviews, sentimentScores = getDBData.getReviewsByAsin(asin.strip('"'))
    table = pd.DataFrame()
    table["brandName"] = brandNames
    table["starRatings"] = starRatings
    table["reviews"] = reviews
    table["sentimentScores"] = sentimentScores
    return table.to_csv()

@app.get("/getBrandReviewSummary")
async def getBrandReviewSummary(brandName: str):
    reviews = getDBData.getBrandReviews(brandName)
    summary = LLMFunctions.summarizeReviews(reviews)
    return summary

@app.get("/comparitiveReviewsAnalysis")
async def getComparitiveReviewsAnalysis(brandName1:str, brandName2: str):
    reviews1 = getDBData.getBrandReviews(brandName1)
    reviews2 = getDBData.getBrandReviews(brandName2)
    summary = LLMFunctions.getComparativeAnalysis(brandName1, reviews1, brandName2, reviews2)
    return summary




if __name__ == "__main__":
    uvicorn.run(app)