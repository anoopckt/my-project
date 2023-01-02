#x = {'key1': 1, 'key2': 3, 'key3': 2}
#y = {'key1': 1, 'key2': 2}
#for (key, value) in set(x.items()) & set(y.items()):
    #print( (key, value))
import json    
data = open('out_try.json', 'r').read()
res=json.loads(data)
print(type(res))
data2 = open('out_try1.json', 'r').read()	
res2=json.loads(data2)
diffrent_keys = res.values() - res2.values()   
print(diffrent_keys)
for (key, value) in set(res.values()) & set(res2.values()):
    print( (key, value))