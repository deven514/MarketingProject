import collections

import chromadb

# chromaDir is the location where the data will be stored.
chromaDir = "d:/database/chroma"



# This function will return a colletion.  It a list of existing collections to determine if the
# particular collection exits.  If it does, then returns a pointer to the exising collection.
# If the collection does not exist, then create a new collection and return the pointer.

def getChromaCollection(name):
    chromaClient = chromadb.PersistentClient(chromaDir)
    return chromaClient.get_or_create_collection(name)

# This will delete the entire collection.
def deleteCollection(name):
   client = chromadb.PersistentClient(chromaDir)
   client.delete_collection(name)
   return True

#Delete all data from the collection with the specific Ids.
def deleteCollectionDataById(name, idList):
   client = chromadb.PersistentClient(chromaDir)
   collection = client.get_collection(name)
   collection.delete(idList)
   return True



#create a new datacollection and store the data.
# meta will consist of dictionary of ASIN and Sentiment score from the LLM.

def createNewCollecttion(name, embeddings, ids, reviews, meta ):
    collection = getChromaCollection(name)
    collection.add(
        ids = ids,
        embeddings = embeddings,
        documents=reviews,
        metadatas= meta
    )

def addDataCollection(name, embeddings, ids, reviews, meta):
    createNewCollecttion(name, embeddings, ids, reviews, meta)


def getDataCollection(name, ids):
    collection = getChromaCollection(name)
    return collection.get(
                            ids=ids,
                            include=["documents", "metadatas", "embeddings"]
                          )





# brand = "DevensBrand"
# my_ids = ['1','2','3']
# embeds= [[1,1,1], [2,2,2], [3,3,3]]
# my_reveiws = ["This is a great product, ",  "I Love this proudct", "This Product was just OK"]
# metaData = [{"ASIN": "B1234", "Sentiment": .123}, {"ASIN": "B123", "Sentiment": -.5}, {"ASIN": "B222", "Sentiment": 1}]
# ids_to_get = ['1','3']
#
# print("Creating new collection")
# # createNewCollecttion(barnd, embeds, my_ids, m
# # print("fetch data")y_reveiws, metaData)
# print("collection created.")
# include = getDataCollection(brand, ids_to_get)
# em = include["embeddings"]
# met = include["metadatas"]
# doc = include["documents"]
# print(met[0]["Sentiment"])










