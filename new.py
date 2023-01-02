import gensim
from gensim import corpora
from pprint import pprint
data = open('out_try.json', 'r').read()
data2 = open('out_try1.json', 'r').read()
texts = [[text for text in doc.split()] for doc in data]
dictionary = corpora.Dictionary(texts)

# Get information about the dictionary
print(dictionary)
print(dictionary.itervalues)