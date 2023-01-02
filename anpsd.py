import textdistance as td
import json
from collections import Counter, defaultdict
#from gensim.similarities import keywords
from gensim import corpora, models, similarities, downloader
import yake

data = open('out_try.json', 'r').read()
data2 = open('out_try1.json', 'r').read()
import difflib
def string_similarity(data, data2):
    result =  difflib.SequenceMatcher(a=data.lower(), b=data2.lower())
    return result.ratio()
data = open('out_try.json', 'r').read()
data2 = open('out_try1.json', 'r').read()  
print(string_similarity(data,data2))  
str1 = 'Python Exercises'
str2 = 'Python Exercises'
print("Original string:")
print(str1)
print(str2)
print("Similarity between two said strings:")
print(string_similarity(str1,str2))
str1 = 'Python Exercises'
str2 = 'Python Exercise'
print("\nOriginal string:")
print(str1)
print(str2)
print("Similarity between two said strings:")
print(string_similarity(str1,str2))
str1 = 'Python Exercises'
str2 = 'Python Ex.'
print("\nOriginal string:")
print(str1)
print(str2)
print("Similarity between two said strings:")
print(string_similarity(str1,str2))
str1 = 'Python Exercises'
str2 = 'Python'
print("\nOriginal string:")
print(str1)
print(str2)
print("Similarity between two said strings:")
print(string_similarity(str1,str2))
str1 = 'Python Exercises'
str1 = 'Java Exercises'
print("\nOriginal string:")
print(str1)
print(str2)
print("Similarity between two said strings:")
print(string_similarity(str1,str2))
