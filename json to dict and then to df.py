import json

f = open("file.json","r")

s = f.read()

d = json.loads(s)

import pandas as pd

df = pd.DataFrame.from_dict(d)

df = df[['vendor','accountId','_id','clientId','currentStatus']]

print(df.head())

df.to_csv("file.tsv", sep='\t', index=False)
