import pandas as p
data = {
    'kdet':['kdet_thom', 'kdet_saouy', 'kdet ju'],
    'pukudt':['Pu Kdet', 'kdetkdet', 'myKdet']
}
result = p.DataFrame(data= data)
 
result.columns = ['kon_kdet', 'may_kdet']
print(result)