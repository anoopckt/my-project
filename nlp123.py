import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity

# define your dictionaries
dict1 = {"Role0": "Python Developer", "Role1": "Python Developer", "Yrs. of Exp.0": "4+ Years", "Role2": "Python Developer", "Tools and technologies0": "python", "Tools and technologies1": "Django", "Tools and technologies2": "Flask", "Concepts0": "data collection", "Concepts1": "APIs", "Concepts2": "Design"}
dict2 = {"Name0": "H/NO", "Phone0": "+919109067567", "Email0": "1947tharwani@gma1l.com", "Career Objective0": "Im looking for possibilities to work for a firm that can help me improve my abilities. broaden my knowledge. and realize my full potential. Im open to a wide range of poss1b1l1t1es that might assist me acquire perspective", "Additional Skills0": "Communication skills"}

# combine the values from both dictionaries into a single list
all_values = list(dict1.values()) + list(dict2.values())

# tokenize the values
tokens = []
for value in all_values:
    tokens += word_tokenize(value)

# remove stop words
filtered_tokens = [token for token in tokens if token.lower() not in stopwords.words('english')]

# create a vocabulary of unique tokens
vocab = list(set(filtered_tokens))
print(vocab)

# create a bag-of-words representation for each dictionary
dict1_bow = [0] * len(vocab)
dict2_bow = [0] * len(vocab)

# count the number of occurrences of each token in each dictionary
for i, token in enumerate(vocab):
    dict1_bow[i] = filtered_tokens.count(token)
    dict2_bow[i] = filtered_tokens.count(token)
sim=cosine_similarity([dict1_bow],[dict2_bow])   
print(sim)

# identify missing and matching keywords
missing_keywords = []
matching_keywords = []
for i, token in enumerate(vocab):
    if dict1_bow[i] > 0 and dict2_bow[i] == 0:
        missing_keywords.append(token)
    elif dict1_bow[i] > 0 and dict2_bow[i] > 0:
        matching_keywords.append(token)

# calculate percentage of matching keywords
percent_matching = len(matching_keywords) / len(vocab)
print(f"Matching keywords: {matching_keywords}")
print(f"Missing keywords: {missing_keywords}")
print(f"Percentage of matching keywords: {percent_matching}")