from gensim.models import Word2Vec

# Load the word2vec model
model = Word2Vec.load("word2vec.model")

# Define the two dictionaries
dict1 = {"cat": "feline", "dog": "canine", "bird": "avian"}
dict2 = {"cat": "kitten", "dog": "puppy", "bird": "chick"}

# Find similar values in the two dictionaries
for key1, value1 in dict1.items():
    for key2, value2 in dict2.items():
        if key1 == key2:
            similarity = model.wv.similarity(value1, value2)
            print(f"Similarity between '{value1}' and '{value2}': {similarity:.2f}")
