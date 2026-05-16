#map()
#filter()
#reduce()
#map(   f--funksiya, i--iterable--sayila bilen)

def kvadrat ( ededler):
    
    return ededler **2

numbers = [6,7,8,2,9,13]

ededlerin_kvadrati = map(  kvadrat,   numbers  )
 
print( list(ededlerin_kvadrati ))