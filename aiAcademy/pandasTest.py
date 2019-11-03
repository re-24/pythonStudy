import numpy as np
import pandas as pd
# sns = pd.read_csv("sns_data.csv")
# sns.columns = ['user_id', 'follow', 'follower', 'like']
# sns.to_csv('output.csv', index=False)
d1 =pd.DataFrame( {"data1": ["a","b","c","d","c","a"], "data2": range(6)})
d1.to_csv('d1.csv', index=False)
d1.to_excel('d1.xlsx', index=False)