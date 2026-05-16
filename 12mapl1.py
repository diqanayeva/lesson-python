euro_ile_qiymet = lambda data: (  data[0],   data[1]  * 0.82  )

bazar_dollar_ile = [
                        ( "kofta", 20.00),
                        ( "salvar", 25.00),
                        ( "jaket", 50.00),
                        ( "corab", 10.00),

]
bazar_euro_ile = map(   euro_ile_qiymet,    bazar_dollar_ile     )

print(  list(bazar_euro_ile ) )