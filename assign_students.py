""" This is a little piece of code I wrote to try to assign problems to students based on their preferences. It's a poor solution/implementation of the assignment problem. Which I believe has been resolved by something called the hungarian algorithm. The strategy here was to "fill in" the students who made no choices by making a random sample weighted towards what choices have not been made.  i.e. the counts for all the requested problems were counted and those were the weights. The more popular the choice, the higher the number. So the random sampling is weighted toward what was not chosen. It's then truncated to 2 (the number of problems I wanted to assign to each student)

Issues: seed isn't working. So my "final" variable was just one of the random samples. It doesn't optimize for choices, those students who made a selection were essentially just given their first 2 choices. So if for instance, everyone choice one popular choice, there's nothing smoothing that out

"""

from random import sample
from random import seed
import pandas as pd
import matplotlib.pyplot as plt

seed(10)

choices = list(range(21,33))


students = {
        'Anastasia':[26,27,28],
        'Aveuca':[],
        'Bella':[25,27,28],
        'Carina':[25,27,28],
        'Dalia':[],
        'Dash':[],
        'Diana':[22,23,25,29],
        'Dino':[],
        'Ellie':[],
        'Evan':[23,26,30],
        'Frank':[],
        'Harry':[],
        'Isaac':[23,24,31],
        'Jason':[23,25,29],
        'Jerry':[],
        'Leo':[],
        'Michael(王)':[],
        'Michael(甘)':[],
        'Newton':[],
        'Oscar':[],
        'Peter':[],
        'Queena':[26,28,27],
        'Ryan':[],
        'Sarah':[],
        'Sherry':[],
        'Sylvia':[30,32,23],
        'Xinjiller': [],
        'Zoey':[],
        }

counts = {}
for c in choices:
    counts[c] = [0]


for k,v in students.items():
    for i in v:
        counts[i][0] += 1


counts_df = pd.DataFrame.from_dict(counts).transpose().rename(columns={0:'count'})

def assign_problem():
    largest = counts_df['count'].max()
    smallest = counts_df['count'].min()
    if largest == smallest:
        # All choices have the same  weight, choose now
        # to avoid division by 0 error below
        return counts_df.sample(1)

    weights = largest -  counts_df['count']
    weights = weights / weights.sum()
    choice = counts_df.sample(1, weights=weights).index[0]
    return choice

for k,v in students.items():
    while len(v) < 2:
        choice = assign_problem()
        v.append(choice)
        students[k] = v


print(counts_df)

print(students)

final = {'Anastasia': [26, 27, 28], 'Aveuca': [21, 31], 'Bella': [25, 27, 28], 'Carina': [25, 27, 28], 'Dalia': [31, 28], 'Dash': [21, 22], 'Diana': [22, 23, 25, 29], 'Dino': [31, 21], 'Ellie': [21, 31], 'Evan': [23, 26, 30], 'Frank': [21, 32], 'Harry': [31, 31], 'Isaac': [23, 24, 31], 'Jason': [23, 25, 29], 'Jerry': [30, 24], 'Leo': [22, 29], 'Michael(王)': [27, 22], 'Michael(甘)': [28, 30], 'Newton': [31, 21], 'Oscar': [28, 22], 'Peter': [32, 26], 'Queena': [26, 28, 27], 'Ryan': [30, 21], 'Sarah': [29, 25], 'Sherry': [29, 29], 'Sylvia': [30, 32, 23], 'Xinjiller': [32, 27], 'Zoey': [26, 22]}

final = {'Anastasia': [26, 27],
'Aveuca': [21, 24],
'Bella': [25, 28],
'Carina': [25, 27],
'Dalia': [31, 28],
'Dash': [21, 29],
'Diana': [22, 23],
'Dino': [31, 21],
'Ellie': [29, 31],
'Evan': [23, 26],
'Frank': [21, 32],
'Harry': [31, 24],
'Isaac': [23, 24],
'Jason': [23, 25],
'Jerry': [30, 24],
'Leo': [22, 29],
'Michael(王)': [27, 22],
'Michael(甘)': [28, 30],
'Newton': [31, 21],
'Oscar': [28, 22],
'Peter': [32, 26],
'Queena': [26, 28],
'Ryan': [30, 24],
'Sarah': [29, 25],
'Sherry': [29, 27],
'Sylvia': [30, 32],
'Xinjiller': [32, 27],
'Zoey': [26, 22]}

for k,v in final.items():
    v = v[:2]
    final[k] = v

bins = {}

for k,v in final.items():
    for i in v:
        try:
            bins[i] += 1
        except:
            bins[i] = 1




plt.bar(bins.keys(), bins.values())
plt.show()

