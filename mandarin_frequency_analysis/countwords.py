# A quick utility to counting the known and learning words of a Migaku json file
import matplotlib.pyplot as plt
import pandas as pd
import json
from random import sample

# fn = 'Migaku_Word_List_zh_2023_4_3.json'
# fn = 'Migaku_Word_List_zh_2023_6_28.json'
# fn = 'Migaku_Word_List_zh_2023_6_20.json'
# df = pd.read_json(fn)
# print(df.columns)

# with open(fn) as json_file:
#     data = json.load(json_file)
#     count1 = 0
#     count2 = 0
#     learning = []
#     for i in data:
#         if i[1] == 1:
#             count1+=1
#             learning.append(i[0])
#         elif i[1] == 2:
#             count2+=1
#         else:
#             print(i[1])
# 
#     print(count1,count2)
# 
#     print(sample(learning,10))

words_history = 'words_learned_history.txt'
df = pd.read_csv(words_history)
df.date = pd.to_datetime(df.date)
print(df.columns)
print(df.dtypes)
df.plot('date', 'count')
plt.title('Chinese words learned by time')
plt.xlabel('Date')
plt.ylabel('Words')
plt.legend('')
plt.show()
