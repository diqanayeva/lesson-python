import json

with open( "products.json", "r", encoding = "utf-8" ) as file:
     data= json.load( file )

     #print( data )
print( " Mehsul siyahisi : \n")

for i in data [ "products"]:
     print(f"ID :     {i [ 'id']    } ")
     print(f"Ad:      {i ['name']   } ")
     print(f"Qiyimet:  {i ['price']  } ")
     print(f"Stock:   {i [ 'stock'] } ")