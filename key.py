import json
import textdistance as td
# a={"role0":"python","role2":"django","role3":"mongodb","name":"adarsh","skills":"html","skills2":"css"}
# b={"role1":"django","role3":"mysql","role5":"mongodb","name":"adarsh"}
# c=str(a)
# print(type(c))
# d=str(b)
data = open('out_try.json', 'r').read()

p=data.capitalize()
a=json.loads(p)
j={}
for key,value in a.items():
    #print(value)
    if key.startswith("concepts"):
        print(key,value)
        




#print(type(p))
#print(p)
#print(data)
a=json.loads(p)
# for i,k in a.items():
#     if i.startswith
# kl={}
# for k,v in sorted(a.items()):
#     print(k,v)
data2 = open('out_try1.json', 'r').read()
t=data2.capitalize()
#print(t)
b=json.loads(t)
#values1 = list(a.values())
#values2 = list(b.values())
#print(values1)
#print(values2)
# match=[]
# missing=[]
# for state in a:
#     if a[state] not in b.values():
#         missing.append(a[state])
#     for j in b:
#         #print(a[state],j[b])
#         if a[state]==b[j]:
#             #a[state]=a[state]+1
#             match.append(a[state])
    # if a[state]!=b[j]:
    #     l.append(a[state])
jd_keywords={"missing_keywords":[],"match_keywords":[],"score":[]}
for state in a:
        if a[state] not in b.values():
            jd_keywords["missing_keywords"].append(a[state])
        for j in b: 
            if a[state]==b[j]:   
                jd_keywords["match_keywords"].append(a[state])
j={"concept":[],"role":[],"tools and technologies":[]}
# for k,y in a.items():
#     if a[y] not in b.values():
#         jd_keywords["missing_keywords"].append(a[y])
        
for key,value in a.items():
    #print(value)
    if key.startswith("concepts"):
        #print(value)
        j["concept"].append(value)

    elif key.startswith("role"):
        j["role"].append(value)
    elif key.startswith("tools and technologies"):
        j["tools and technologies"].append(value)

print(j)
a_values = set([item for sublist in j.values() for item in sublist])
b_values = set([item for sublist in b.values() for item in sublist])
matching_values = a_values.intersection(b_values)
print(matching_values)
        #print(value)          
#print(jd_keywords)        
# for key,state in a.items():
#     if key.startswith("concepts":state") not in b.values():

#         print(state)
#         jd_keywords["missing_keywords"].append(state)
        
    # for j in b:
    #     #print(a[state],j[b])
    #     if a[state]==b[j]:
    #         #a[state]=a[state]+1
    #         jd_keywords["match_keywords"].append(a[state])    
print(jd_keywords)    
#print(missing)  
j = td.jaccard.similarity(data,data2)
print(j)


s = td.sorensen_dice.similarity(data,data2)
print(s)
#print(j)
c = td.cosine.similarity(data,data2)
print(c)
o = td.overlap.normalized_similarity(data,data2)
print(o)
total = (j+s+c+o)/4
sc=(int(total*100))
f=str(sc)
jd_keywords["score"].append(f)      
#print(jd_keywords)
p=json.dumps(jd_keywords)
#print(p)
#total = (s+o)/2
#print (int(total*100),"%")      
            
        #print(state,j)
#keys = a.keys()
#print(keys)

# an=str(a)
# anp=str(b)
# print(type(a))
# c=int(anp)
# d=int(an)
# for key in d:
#     for jey in c:
#         if d[key]==jey[c]:
#            print(d[key])
#      print(a[key],"=",key)
# for k,v in (a.items()):
#     print(k[0],v)
    # for j,l in (b.items()):

    #     print(k,v,j,l)
        # if a[v]==b[l]:
        #     print(a[v[0]])
        # else:
        #     print("so sad")
# my_list = ['apple', 'banana', 'melon']

# for index, item in enumerate(my_list):
#     print(index, item)  # 👉️ 0 apple, 1 banana, 2 melon


