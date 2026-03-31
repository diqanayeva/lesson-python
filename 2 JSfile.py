import json

with open( "products.json", "r", encoding = "utf-8" ) as file:
     data= json.load( file )

     #print( data )
print( " Mehsul siyahisi : \n")

for i in data [ "products"]:
     print("ID :"  + str( i [ 'id'] ) )
     print("Ad:" + i ['name'])
     print("Qiymet:" + str( i ['price']))
     print("Stock:" + str( i [ 'stock']))

