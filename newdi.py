import json
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
data = open('out_try.json', 'r').read()
res=json.loads(data)
print(summarize(data,ratio=0.2))
print(keywords(data))
data2 = open('out_try1.json', 'r').read()
res2=json.loads(data2)
match=[]
missing=[]
if "skills"=="data":

  print("skills")
#print(res2)
for key,v in res.items():
  print(key,v[0])
  
#       if ["skill0"]==["Tools and technologies10"]:
#         print (jey)
#         res2[jey]+=1
#         match.append(key)
#        #res2[jey]+=1
#       else:
#         if key!=jey:
#           missing.append(key)
          


# print(missing)
# print(match)      # for jey in res2.values():
      #     print(jey)
#           if key == jey:
#             #key=key+1
#             match.append(key)
#                 #print (key)
#           else:
#             if key!=jey:
#               missing.append(jey)
# print(match)
# print(missing)
# for x in res.values():
#   for y in res2.values():
#       if res[x]==res2[y+1]:
#         print(res[x])
# for k, v in res, res2:
#     total = total + res*res2      
#     print(total)  
# from itertools import izip
# for k, k2 in izip(res,res2):
#     print(res[k],res2[k2])    


# if any(x in res for x in res2):
#           print set(res2)&set(res)
# new_dict = {k: res[k] for k in res2.values() if k in res.values()}        
# for k in res2.values():
#   print(k)
# for j in res.values():
#   print(j)  
# print(new_dict)  
