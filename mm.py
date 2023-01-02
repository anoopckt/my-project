import json
data = open('out_try.json', 'r').read()
print(type(data))
res=json.loads(data)
data2 = open('out_try1.json', 'r').read()
res2=json.loads(data2)

text_list = [data2, data]

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
count_matrix = cv.fit_transform(text_list)
print(count_matrix)
a=cv.get_feature_names_out()
print(a)
from sklearn.metrics.pairwise import cosine_similarity
# get the match percentage
def match():
    matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
    matchPercentage = round(matchPercentage, 2) # round to two decimal
    return "Your resume matches about "+ str(matchPercentage)+ "% of the job description."
# a=[]
# for i in res.values():
#     if res.values() in res2.values():
#         a.append(res)
#         print(res.values)
# #         if res.values()==res2[j.values()]:
# #             print(i)
# # res.values() == res2.values()
# print(res2.values())
# print(sorted(res.items()) == sorted(res2.items()))
# print(sorted(res2.items()))
# matching_dict_values = {}
# for key in res.values():
#     if key in res2.values():
#         if res[key] == res2[key]:
#             matching_dict_values[key]=res[key]
# print(matching_dict_values)     
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_df=0.05, min_df=0.002)
words = tfidf.fit_transform(text_list)
sentence = " ".join(tfidf.get_feature_names())
print( sentence    )   