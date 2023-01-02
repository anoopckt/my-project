import json
x=open('out_try.json', 'r').read()
y = open('out_try1.json', 'r').read()
res = json.loads(x)
res2=json.loads(y)

for (key, value) in set(res.values()) & set(res2.values()):
   print('%s: %s is present in both x and y' % (key, value))
	