import json
data = open('out_try.json', 'r').read()
res=json.loads(data)
data2 = open('out_try1.json', 'r').read()
res2=json.loads(data2)
c=res.items.values()&res2.items.values()
print(c)
new_dict = {} 
for k, v in res.iteritems(): 
    new_dict.setdefault(v, []).append(k)