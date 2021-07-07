import pandas as pd
import json
df1 = pd.read_excel('input_example.xlsx', sheet_name='constant') # if you need to run for another excel sheet please rename here. if your sheet name is different please also rename it
df2 = pd.read_excel('input_example.xlsx', sheet_name='variable') # if you need to run for another excel sheet please rename here. if your sheet name is different please also rename it
df3 = pd.concat([df1, df2],axis=1)

dic_data = {}

for index, row in df3.iterrows():
    head = row['head']
    field = row['field1']
    col = row['col1']
    doc = row['doc1']
    field2 = row['field2']
    field3 = row['field3']
    var1 = row['var1']
    var2 = row['var2']
    var3 = row['var3']
    dem_dic_data = {head: {
        field: var1,
        col: {
            doc: {
                field2: var2,
                field3: var3
            }
        }
    }}
    dic_data.update(dem_dic_data)

with open('python_dictionary.json','a') as file: # when you need another json for another excel sheet, please rename here.
    file.write(json.dumps(dic_data,indent=4))