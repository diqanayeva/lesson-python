a = ( 'alma', 'armud','heyva')

print(a[0])
print(a[1])
print(a[2])

def meyveler( * bagmeyveleri):
    for i in bagmeyveleri:
    #print( type(bagmeyveleri))
     print(bagmeyveleri)


meyveler('alma','armud','heyva','nar','mandarin')