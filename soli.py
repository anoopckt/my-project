#from sklearn.feature_extraction._dict_vectorizer import 
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
data = open('out_try.json', 'r').read()
res=json.loads(data)
data2 = open('out_try1.json', 'r').read()
res2=json.loads(data2)
for key in res.keys():
    print(res["skills
    "])
compare = [res,res2]
cVect = DictVectorizer()
cMatrix = cVect.fit_transform(compare)
print(cMatrix)

#prints how well the resume matches as a percentage
matPercent = cosine_similarity(cMatrix)[0][1] * 100
matPercent = round(matPercent, 2) # round to two decimal
print("Resume is a "+ str(matPercent)+ "% match to the job.")
a=cVect.get_feature_names()
print(a)