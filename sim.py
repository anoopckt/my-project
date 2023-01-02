a = {"django": "web framework"}
b = {"python": "programming language"}
for key, value in a.items():
    if key in b:
        print(f"Similar key found: {key}")
        print(f"Value in dictionary a: {value}")
        print(f"Value in dictionary b: {b[key]}")

a_keys = set(a.keys())
b_keys = set(b.keys())

similar_keys = a_keys.intersection(b_keys)

print(similar_keys)
