kvadrat = lambda  ededler: ededler **2

numbers = [6,7,8,2,9,13]

ededlerin_kvadrati = map(  kvadrat,   numbers  )
 
print( list(ededlerin_kvadrati ))


#numbers + [6,7,8,2,9,13]

#print(  set(  map(   lambda  ededler:  ededler **2,        numbers)  )    )