import re
import json
data = open('out_try.json', 'r').read()
text = re.sub("Tools and technologies","Skills",data)
text=  re.sub("Role","Work Desgination",text)
text = re.sub("Education","Education Level",text)
#print(text)

#print(text)
res=json.loads(text)
#print(res)
data2 = open('out_try1.json', 'r').read()
res2=json.loads(data2)
x = res.get("Skills1")
print(x)
# for key in res.items():
#     if res.get("s")
#     if key=="Skills1":
        #print([key])
    
    #print(key)
dictionary1 = {"a": 1, "b": 2}
dictionary2 = {"a": 3, "b": 2}
common_pairs = dict()
for key in res:
    if (key in res2 and res[key] == res2[key]):

        common_pairs[key] = res[key]
print(common_pairs)