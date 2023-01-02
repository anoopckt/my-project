import textdistance as td
import json
from collections import Counter, defaultdict
#from gensim.similarities import keywords
from gensim import corpora, models, similarities, downloader
import yake

# from multi_rake import Rake
# rake = Rake()
# keywords = rake.apply(full_text)
# print(keywords[:10])
data = open('out_try.json', 'r').read()
# value1=list(data.values())
# print(value1)
res=json.loads(data)
value1=list(res.values())
print(value1)
data2 = open('out_try1.json', 'r').read()
res2=json.loads(data2)
a={}
for key,value in res2.items():
    if key.startswith("Skills"):
        a.update({key:value})
    elif key.startswith("Education Level") :
        a.update({key:value}) 
    elif key.startswith("Additional Skills"):
        a.update({key:value})   
    elif key.startswith("Work Desgination"):  
        a.update({key:value}) 
    
print(a)
  
value2=list(res2.values())
print(value2)
b=str(a)

#a=td.similarity(get_jaccard_sim(res), set(job_skills)))
#c=data+data2

#kw_extractor = yake.KeywordExtractor(top=5, stopwords=None)
#keywords = kw_extractor.extract_keywords()
#print(keywords)
#for kw, v in keywords:
  #print("Keyphrase: ",kw, ": score", v)

# data = open('out_try.json', 'r').read()

# #print(keywords(data))
# #from gensim.summarization import keywords
# data2 = open('out_try1.json', 'rb').read()
# #print(type(data))
# def manage_duplicates(pairs):
#    d = {}
#    k_counter = Counter(defaultdict(int))
#    for k, v in pairs:
#        d[k+str(k_counter[k])] = v
#        k_counter[k] += 1
#    value = str(d).replace("'", '"')
#    return value
# a=json.loads(data, object_pairs_hook=manage_duplicates)

# b=json.loads(data2,object_pairs_hook=manage_duplicates)
# #print(b)
    
j = td.jaccard.similarity(data,b)



s = td.sorensen_dice.similarity(data,b)
#print(j)
c = td.cosine.similarity(data,b)
o = td.overlap.normalized_similarity(data,b)
total = (j+s+c+o)/4

#total = (s+o)/2
print (int(total*100),"%")
#print(data)
#print(data2)

#def match(resume, job_des):
   # j = td.jaccard.similarity(resume, job_des)
   # s = td.sorensen_dice.similarity(resume, job_des)
   # c = td.cosine.similarity(resume, job_des)
   # o = td.overlap.normalized_similarity(resume, job_des)
   # total = (j+s+c+o)/4
    # total = (s+o)/2
    #return int(total*100)


