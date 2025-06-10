from langchain_ollama import embeddings, OllamaEmbeddings



def getEmbeddings(reviews):
    print("getting Embeddings")
    reviewsEmbeddings = []
    embed = OllamaEmbeddings(model="llama3.2:latest")
    for review in reviews:
        reviewsEmbeddings.append(embed.embed_documents(review))
    print("done")
    return reviewsEmbeddings







