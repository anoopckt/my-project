import json
import jsonpickle
from json import JSONEncoder
def common_words(res, res2):
        matching_words = set.intersection(set(res), set(res2))
        print(matching_words)
        return matching_words
data = open('out_try.json', 'r').read()
res=json.loads(data)
decodedSet = jsonpickle.decode(res)
print(type(decodedSet))
data2 = open('out_try1.json', 'r').read()
res2=json.loads(data2)   
#setEncoder().encode(res2)  
#common_words(res,res2)   