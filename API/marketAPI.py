from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from APIHelper import APIFunctions

import uvicorn

from Helper import getDBData

app = FastAPI()

@app.get("/")
async def root():
    return ({"Info:": "Marketing API"} )

@app.get("/getAllBrands")
async def getAllBrands():
    brands = getDBData.getBrands()
    return jsonable_encoder(brands)

@app.get("/getBrandInfo(brand")
async def getBrandInfo(brandId: int):




if __name__ == "__main__":
    uvicorn.run(app)