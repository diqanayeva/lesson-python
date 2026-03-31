import json

with open ( "products.json", "r", encoding= "utf-8") as file:

    print( file )

    data = json.load( file )

    print( data )