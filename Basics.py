
# coding: utf-8

# In[21]:


import csv

#Import raw csv files
f = open("guns.csv", "r")
csvreader = csv.reader(f)
data = list(csvreader)

header = data[0] #Extract header file
data = data[1:] #Data w/o header file

#Count number of deaths occuring each year
year_counts = {}
years = [row[1] for row in data]

for year in years:
    if year not in year_counts:
        year_counts[year] = 1
    else:
        year_counts[year] += 1
#print(year_counts)


#Count based on Month and Year
import datetime
dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]
date_counts = {}
for date in dates:
    if date not in date_counts:
        date_counts[date] = 1
    else:
        date_counts[date] += 1

#print(date_counts)

#Count sex
sex_counts = {}
sexs = [row[5] for row in data]
for sex in sexs:
    if sex not in sex_counts:
        sex_counts[sex] = 1
    else:
        sex_counts[sex] += 1
print(sex_counts)

#Count sex
race_counts = {}
races = [row[7] for row in data]
for race in races:
    if race not in race_counts:
        race_counts[race] = 1
    else:
        race_counts[race] += 1
print(race_counts)


