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
    brands = getDBData.getBrandsNames()
    return jsonable_encoder(brands)


if __name__ == "__main__":
    uvicorn.run(app)