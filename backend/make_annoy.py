from annoy import AnnoyIndex
import pickle

annoy_index = AnnoyIndex(2048, "angular")

train_embeddings = None

with open("./instance/database/embeddings.pkl", "rb") as file:
    train_embeddings = pickle.load(file)

for i, item in enumerate(train_embeddings):
    annoy_index.add_item(i, item)

annoy_index.build(20)
annoy_index.save("./instance/database/annoy_index.ann")