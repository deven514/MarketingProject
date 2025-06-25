from Utils import LLMFunctions
from Helper import getDBData
import json




def getAllBrands():
    allBrands = getDBData.getBrands()
    return allBrands