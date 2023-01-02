import json
import textdistance as td
data1=open('out_try.json','r').read()
res1=json.loads(data1)
data2 = open('out_try1.json', 'r').read()
res2=json.loads(data2)
# a = dict([("missing", dict(role=["python"]))])
# print(a)
jd_keywords={}
jd_keywords["missing_keywords"]={"Tools and technologies":[],"Role":[],"Concepts":[],"Education":[],"Yrs. of Exp.":[]}
jd_keywords["match_keywords"]={"Tools and technologies":[],"Role":[],"Concepts":[],"Education":[],"Yrs. of Exp.":[]}
jd_keywords["score"]=[]
# find all tool and technologies and Skills in data1 and data2
a={}
b={}
for key,value in res1.items():
    if key.startswith("Tools and technologies"):
        a.update({key:value}) 
for key,value in res2.items():
    if key.startswith("Skills"):
        b.update({key:value})
# jd_keywords={}
# jd_keywords["missing_keywords"]={"Tools and technologies":[],"Role":[],"Concepts":[],"Education":[],"Yrs. of Exp.":[]}
# jd_keywords["match_keywords"]={"Tools and technologies":[],"Role":[],"Concepts":[],"Education":[],"Yrs. of Exp.":[]}
# jd_keywords["score"]=[]
# find missing and matching keywords in dictionary a and dictionary b
for state in a:
        if a[state] not in b.values():
            jd_keywords["missing_keywords"]["Tools and technologies"].append(a[state])
        for j in b: 
            if a[state]==b[j]:   
                jd_keywords["match_keywords"]["Tools and technologies"].append(a[state])   
c={}
d={}
for key,value in res1.items():
    if key.startswith("Role"):
        c.update({key:value}) 
for key,value in res2.items():
    if key.startswith("Work Desgination"):
        d.update({key:value})
for state in c:
        if c[state] not in d.values():
            jd_keywords["missing_keywords"]["Role"].append(c[state])
        for j in d: 
            if c[state]==d[j]:   
                jd_keywords["match_keywords"]["Role"].append(c[state])   
e={}
f={}
for key,value in res1.items():
    if key.startswith("Concepts"):
        e.update({key:value}) 
for key,value in res2.items():
    if key.startswith("Additional Skills"):
        f.update({key:value})
for state in e:
        if e[state] not in f.values():
            jd_keywords["missing_keywords"]["Concepts"].append(e[state])
        for j in f: 
            if e[state]==f[j]:   
                jd_keywords["match_keywords"]["Concepts"].append(e[state])        
g={}
h={}
for key,value in res1.items():
    if key.startswith("Education Level"):
        g.update({key:value}) 
for key,value in res2.items():
    if key.startswith("Education"):
        h.update({key:value})
for state in g:
        if g[state] not in h.values():
            jd_keywords["missing_keywords"]["Education"].append(g[state])
        for j in h: 
            if g[state]==h[j]:   
                jd_keywords["match_keywords"]["Education"].append(g[state])   
i={}
j={}
for key,value in res1.items():
    if key.startswith("Work DurationT2"):
        i.update({key:value}) 
for key,value in res2.items():
    if key.startswith("Yrs. of Exp."):
        j.update({key:value})
for state in i:
        if g[state] not in j.values():
            jd_keywords["missing_keywords"]["Yrs. of Exp."].append(i[state])
        for j in j: 
            if g[state]==h[j]:   
                jd_keywords["match_keywords"]["Yrs. of Exp."].append(j[state])   
j = td.jaccard.similarity(data1,data2)
s = td.sorensen_dice.similarity(data1,data2)
c = td.cosine.similarity(data1,data2)
o = td.overlap.normalized_similarity(data1,data2)
total = (j+s+c+o)/4
sc=(int(total*100))
f=str(sc)
#print(type(sc))
jd_keywords["score"].append(f)                 


print(c)      
print(d)  

                         
print(jd_keywords)   
l=json.dumps(jd_keywords)  
print(l)      