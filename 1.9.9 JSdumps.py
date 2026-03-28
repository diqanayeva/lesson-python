import json
melumatlar = {
    'ad': "Kamal",
    'yash': 21,
    'bal' : 655
}
json_melumatlar = json.dumps( melumatlar )

print ( (json_melumatlar) )
print( type (json_melumatlar ))