a = dict(
    ad = 'Ali',
    soyad = 'Veliyev',
    yas = 30,
    gozrengi = 'qara'

)
#a={
  #'ad':'Ali'}
  
def meyveler( **bagmeyveleri):
    print(bagmeyveleri)


meyveler(ad='Ali', soyad='Veliyev', yas=30, gozrengi='qara')