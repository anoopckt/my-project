# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
# from sklearn.feature_extraction.text import CountVectorizer
import textdistance as td
# # Extract the values from the dictionaries and store them in lists
# dict1 = {'key1': 'value1', 'key2': 'value2'}
# dict2 = {'key3': 'value3', 'key4': 'value4'}
# values1 = list(dict1.values())
# values2 = list(dict2.values())
# print(values1)

# # Preprocess the values by removing stopwords and performing stemming
# stop_words = set(stopwords.words('english'))
# stemmer = PorterStemmer()
# processed_values1 = []
# for value in values1:
#     words = [stemmer.stem(word) for word in value.split() if word not in stop_words]
#     processed_values1.append(' '.join(words))
# processed_values2 = []
# for value in values2:
#     words = [stemmer.stem(word) for word in value.split() if word not in stop_words]
#     processed_values2.append(' '.join(words))

# # Create a vocabulary of unique words from the processed values
# print(processed_values1)
# all_values = processed_values1 + processed_values2
# vectorizer = CountVectorizer().fit(all_values)
# print(vectorizer)
# vocabulary = vectorizer.vocabulary_
# print(vocabulary)

# # Create document-term matrices for the processed values
# matrix1 = vectorizer.transform(processed_values1)
# matrix2 = vectorizer.transform(processed_values2)
# print(matrix1)

# # Calculate the cosine similarity between the matrices

# cosine_similarity = nltk.cluster.util.cosine_distance(matrix1, matrix2)

# print(cosine_similarity)
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

# Extract the values from the dictionaries and store them in lists
dict1 = {'key1': 'value1', 'key2': 'value2'}
dict2 = {'key3': 'value1', 'key4': 'value4'}
values1 = list(dict1.values())
print(values1)
values2 = list(dict2.values())
j = td.jaccard.similarity(values1,values2)
print(j)


s = td.sorensen_dice.similarity(values1,values2)
print(s)
#print(j)
c = td.cosine.similarity(values1,values2)
print(c)
o = td.overlap.normalized_similarity(values1,values2)
print(o)
total = (j+s+c+o)/4
print(int(total))
# Preprocess the values by removing stopwords and performing stemming
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
processed_values1 = []
for value in values1:
    words = [stemmer.stem(word) for word in value.split() if word not in stop_words]
    processed_values1.append(' '.join(words))
processed_values2 = []
for value in values2:
    words = [stemmer.stem(word) for word in value.split() if word not in stop_words]
    processed_values2.append(' '.join(words))

# Create a vocabulary of unique words from the processed values
all_values = processed_values1 + processed_values2
vectorizer = CountVectorizer().fit(all_values)
vocabulary = vectorizer.vocabulary_

# Create document-term matrices for the processed values
matrix1 = vectorizer.transform(processed_values1)
matrix2 = vectorizer.transform(processed_values2)

# Calculate the cosine similarity between the matrices
cosine_similarity = nltk.cluster.util.cosine_distance(matrix1, matrix2)

print(cosine_similarity)
