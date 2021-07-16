import pandas as pd
import glob
import os 

path=os.getcwd()
path=str(path)+'\Compras'
print(path)


all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, names=['Nome', 'Preço', 'Data'])
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

test1=frame.groupby('Nome')['Preço'].apply(list).reset_index(name='Preço')

test2=frame.groupby('Nome')['Data'].apply(list).reset_index(name='Data')

aux1=pd.DataFrame(test1.Preço.values.tolist()).add_prefix('Preço_')
aux2=pd.DataFrame(test2.Data.values.tolist()).add_prefix('Data_')
result1 = pd.concat([test1, aux1], axis=1).reindex(test1.index)
result1.drop(columns=['Preço'], inplace=True)
result2 = pd.concat([test2, aux2], axis=1).reindex(test2.index)
result2.drop(columns=['Data'], inplace=True)
result=result1.merge(result2, how='inner', on='Nome')
#print(result)
lista_nomes=[]
for i in result.columns:
    if 'Preço_' in i:
        lista_nomes+=[i]
result['Preço_minimo'] = result[lista_nomes].min(axis=1)
result['Comparador']=1.25*result['Preço_minimo']
for i in range(len(lista_nomes)):
    result['Result'+str(i)]=result['Preço_'+str(i)]>result['Comparador']
result['Result'] = (result.iloc[:, 2*len(lista_nomes)+3:3*len(lista_nomes)+3].values==False).all(axis=1).astype(int)

result=result.loc[result.Result==0]
result.drop(columns=['Comparador', 'Preço_minimo'], inplace=True)
for column in result.columns:
    if 'Result' in column:
        result.drop(columns=[column], inplace=True)
result=result.dropna(axis=1, how='all')

result.to_csv('Relatorio.csv', index=False)


#result['Result'] = (result.iloc[:, 1:len(lista_nomes)].values-result[['Preço_minimo']].values >= 0.25*result[['Preço_minimo']].values).all(axis=1).astype(int)
#print(result)


