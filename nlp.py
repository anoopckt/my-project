import json
fridge = {
    "orange": 5,
    "citron": 3,
    "sel": 100,
    "sucre": 50,
    "farine": 250,
    "tomates": 6,
    "huile": 100,
    "pomme": 1,
    "lait": 1,
    "pois chiche": 1,
}

recipes = {
    "jus_de_fruit": {"orange": 3, "citron": 1, "pomme": 2},
    "salad": {"tomates": 4, "huile": 10, "sel": 3},
    "crepes": {"lait": 1, "farine": 250, "oeufs": 2},
    "glace": {"bac a glace": 1, "coulis abricot": 1, "batonnet": 1},
}

data = open('out_try.json', 'r').read()
res = json.loads(data)
data2 = open('out_try1.json', 'r').read()
res2 = json.loads(data2)

for recipe_name, ingredients in res2.items():
    print(f"Recipe: {recipe_name}")
    if (missing := ingredients.keys() - res.keys()) :
        print("Missing ingredients:", missing)
    else:
        common = {
            k: data[k] - ingredients[k]
            for k in ingredients.keys() & res.keys()
        }

        if all(v >= 0 for v in common.values()):
            print("All ingredients are OK")
        else:
            for i, v in common.items():
                if v < 0:
                    print(f"Ingredient {i}: missing {-v} items")
    print("-" * 80)