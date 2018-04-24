## Merge CSV Files for 8 UC Schools

import pandas as pd
import glob, os
import csv

os.chdir("UC_Project/oldSchoolFiles")

files = glob.glob('*deg.csv')
print (files)

# concatenate files ending with "deg.csv"
dfs = [pd.read_csv(i, sep=';').assign(New=os.path.basename(i)) for i in files]
df = pd.concat(dfs, ignore_index=True)

df.head(5)

df.columns = ['AcadYr', 'Major', "Level", "NumRecords", "School"]

# clean school name column
df = df.astype(str)
df = df.apply(lambda x: x.str.split("_").str[0])

df.head(5)

# export to csv
df.to_csv("SchoolsMerged.csv", encoding='utf-8', index=False)