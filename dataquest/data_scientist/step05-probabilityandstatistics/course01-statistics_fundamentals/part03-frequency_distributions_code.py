## 1/13

## Try to get a sense for how difficult it is to analyze the basketball data set in its original form.

##    Read in the basketball data set (the name of the CSV file is wnba.csv) using pd.read_csv().
##    Using DataFrame.shape, find the number of rows and columns of the data set.
##    Print the entire data set, and try to analyze the output to find some patterns.

import pandas as pd

pd.options.display.max_rows = 200
pd.options.display.max_columns = 50

wbna = pd.read_csv('wnba.csv')

wbna.shape

## 2/13
## Using the Series.value_counts() method, generate frequency distribution tables for the following columns:

##    Pos. Assign the frequency distribution table to a variable named freq_distro_pos.
##    Height. Assign the frequency distribution table to a variable named freq_distro_height.


wnba = pd.read_csv('wnba.csv')

print(wnba['Pos'].value_counts())

freq_distro_height = wnba['Height'].value_counts()

freq_distro_pos = wnba['Pos'].value_counts()

## 3/13

wnba = pd.read_csv('wnba.csv')

print(wnba['Height'].value_counts().sort_index())

age_ascending = wnba['Age'].value_counts().sort_index(ascending = True)
age_descending = wnba['Age'].value_counts().sort_index(ascending = True)

## 4/13

## TOOLBOX: How to create a lambda function which will make a new dataframe column with ordinal values.

def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <=  80):
        return 'few points'
    if (80 < row['PTS'] <=  150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <=  450):
        return 'more than average'
    else:
        return 'much more than average'
    
wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)

# Type your answer below
pts_ordinal_val_counts = wnba['PTS_ordinal_scale'].value_counts()
positions_list_ascending = [5,1,2,0,3,4]
pts_ordinal_desc = wnba['PTS_ordinal_scale'].value_counts().iloc[[4,3,0,2,1,5]]

## 5/13

## Answer the following questions about the Age variable:

##    What proportion of players are 25 years old? Assign your answer to a variable named proportion_25.
##    What percentage of players are 30 years old? Assign your answer to a variable named percentage_30.
##    What percentage of players are 30 years or older? Assign your answer to a variable named percentage_over_30.
##    What percentage of players are 23 years or younger? Assign your answer to a variable named percentage_below_23.

## Solution notes: 
# 
# * the value_counts method creates a series where the Ages become indexes and the values are the variable value
# * the indexes are sorted in order by value, not by index
# * .loc selects the series elements by index
wnba = pd.read_csv('wnba.csv')

age_proportions = wnba['Age'].value_counts(normalize = True).sort_index(ascending = True)
age_percentages = wnba['Age'].value_counts(normalize = True).sort_index(ascending = True)*100

proportion_25 = age_proportions.loc[25]
percentage_30 = age_percentages.loc[30]
percentage_over_30 = age_percentages.loc[30:].sum()
percentage_below_23 = age_percentages.loc[:23].sum()

## 6/13

# Import percentileofscore() from scipy.stats, and then use it to answer the following questions:

#    What percentage of players played half the number of games or less in the 2016-2017 season (there are 34 games in the WNBA’s regular season)? Use the Games Played column to find the data you need, and assign your answer to a variable named percentile_rank_half_less.
#    What percentage of players played more than half the number of games of the season 2016-2017? Assign your result to percentage_half_more.

wnba = pd.read_csv('wnba.csv')

from scipy.stats import percentileofscore

num_games = 34

percentile_rank_half_less = percentileofscore(a=wnba['Games Played'], score = num_games/2, kind = 'weak')

percentage_half_more = 100 - percentileofscore(a=wnba['Games Played'], score = num_games/2, kind = 'weak')

## 7/13

wnba = pd.read_csv('wnba.csv')

age_upper_quartile = wnba['Age'].describe(percentiles = [.75]).iloc[5]
age_middle_quartile = wnba['Age'].describe(percentiles = [.50]).iloc[4]
age_95th_percentile = wnba['Age'].describe(percentiles = [.95]).iloc[5]

# Q1: A percentile is a value of a variable, and it corresponds to a certain percentile rank in the distribution of that variable.
question1 = True
# Q2: A percentile rank is a numerical value from the distribution of a variable.
question2 = False
# Q3: The 25th percentile is the same thing as the lower quartile, and the upper quartile is the same thing as the third quartile.
question3 = True

## 8/13

## Examine the frequency table for the PTS (total points) variable trying to find some patterns in the distribution of values. Then, generate a grouped frequency distribution table for the PTS variable with the following characteristics:

#    The table has 10 class intervals.
#    For each class interval, the table shows percentages instead of frequencies.
#    The class intervals are sorted in descending order.

wnba = pd.read_csv('wnba.csv')

freq_table = wnba['PTS'].value_counts()
print(freq_table)

grouped_freq_table = wnba['PTS'].value_counts(normalize = True, bins = 10).sort_index(ascending=False)*100

## 9/13

# simple excercise

## 10/13

## Using the techniques above, generate a grouped frequency table for the PTS variable. The table should have the following characteristics:

##    There are 10 class intervals.
##    The first class interval starts at 0 (not included).
##    The last class interval ends at 600 (included).
##    Each interval has a range of 60 points.

## Assign the table to a variable named gr_freq_table_10.

wnba = pd.read_csv('wnba.csv')

myintervals = pd.interval_range(start=0,end=600,freq=60)

gr_freq_table_10 = pd.Series([0,0,0,0,0,0,0,0,0,0], index=myintervals)

print(gr_freq_table_10.index)

for ptvalue in wnba['PTS']:
    for interval in myintervals:
        if ptvalue in interval:
            gr_freq_table_10.loc[interval] += 1
            break
            
print(gr_freq_table_10)