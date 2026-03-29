import json
with open( "1.9.9products.json", "r", encoding="utf-8") as file:
    data = json.load(file)

    print(data)