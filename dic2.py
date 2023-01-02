import json
x=open('out_try.json', 'r').read()
y = open('out_try1.json', 'r').read()
First_Dict = json.loads(x)
Second_Dict=json.loads(y)
key_lst=[]
values_lst=[]
for key, value in First_Dict.items() and Second_Dict.items():
    if key in First_Dict.keys() and Second_Dict.keys():
        if key in Second_Dict.keys() and First_Dict.keys() :
            continue
        else:
            key_lst.append(key)
    else:
        key_lst.append(key)
    if value in First_Dict.values() and Second_Dict.values():
        if value in Second_Dict.values() and First_Dict.values() :

            continue
        else:
            values_lst.append(value)
    else:
        values_lst.append(value)
for key, value in Second_Dict.items() and First_Dict.items():
    if key in First_Dict.keys() and Second_Dict.keys():
        if key in Second_Dict.keys() and First_Dict.keys() :
            continue
        else:
            key_lst.append(key)
    else:
        key_lst.append(key)
    if value in First_Dict.values() and Second_Dict.values():
        if value in Second_Dict.values() and First_Dict.values() :

            continue
        else:
            values_lst.append(value)
    else:
        values_lst.append(value)
print("Missing Keys: ",key_lst[0],": Missing Values",values_lst[0])
print("Missing Keys: ",key_lst[1],": Missing Values",values_lst[1])        