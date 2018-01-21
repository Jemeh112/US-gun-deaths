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
#print(sex_counts)

#Count sex
race_counts = {}
races = [row[7] for row in data]
for race in races:
    if race not in race_counts:
        race_counts[race] = 1
    else:
        race_counts[race] += 1
#print(race_counts)

#Import census.csv data
f_census = open("census.csv", "r")
census_reader = csv.reader(f_census)
census = list(census_reader)

#Creation of header and data lists
mapping = {}
census_header = census[:1][0]
census_data = census[1:][0]

#Mapping of census and data
for data in census_header:
    if data == "Race Alone - White":
        index = census_header.index("Race Alone - White")
        mapping["White"] = int(census_data[index])
    elif data == "Race Alone - American Indian and Alaska Native":
        index = census_header.index("Race Alone - American Indian and Alaska Native")
        mapping["Native American/Native Alaskan"] = int(census_data[index])
    elif data == "Race Alone - Hispanic":
        index = census_header.index("Race Alone - Hispanic")
        mapping["Hispanic"] = int(census_data[index])
    elif data == "Race Alone - Black or African American":
        index = census_header.index("Race Alone - Black or African American")
        mapping["Black"] = int(census_data[index])
    elif data == "Asian/Pacific Islander":
        index = census_header.index("Race Alone - Asian")
        if "Asian/Pacific Islander" not in mapping:
            mapping["Asian/Pacific Islander"] = int(census_data[index])
        else:
            mapping["Asian/Pacific Islander"] += int(census_data[index])
    elif data == "Race Alone - Asian":
        index = census_header.index("Race Alone - Asian")
        if "Asian/Pacific Islander" not in mapping:
            mapping["Asian/Pacific Islander"] = int(census_data[index])
        else:
            mapping["Asian/Pacific Islander"] += int(census_data[index])
    elif data == "Race Alone - Native Hawaiian and Other Pacific Islander":
        index = census_header.index("Race Alone - Native Hawaiian and Other Pacific Islander")
        if "Asian/Pacific Islander" not in mapping:
            mapping["Asian/Pacific Islander"] = int(census_data[index])
        else:
            mapping["Asian/Pacific Islander"] += int(census_data[index])

race_per_hundredk = {}

for key in race_counts:
    value = race_counts[key] / mapping[key]
    value = value * 100000
    race_per_hundredk[key] = round(value,2)

print(race_per_hundredk)
