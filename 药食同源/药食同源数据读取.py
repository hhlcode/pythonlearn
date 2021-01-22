import pandas as pd 
def dataSource():
    data = pd.read_csv("药食同源.xlsx",encoding='uttf-8')
    return data
data = dataSource()
print(data.info())
