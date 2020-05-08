## 4/14

import pandas as pd

def getkeywithmaxvalue(mydict):
    all_values = list(mydict.values())
    all_keys = list(mydict.keys())
    return all_keys[all_values.index(max(all_values))]

wnba = pd.read_csv('wnba.csv')

wnba.head()
wnba.tail()

parameter = wnba["Games Played"].max()
#print(parameter)

sample = wnba.sample(n=30,random_state=1)

statistic = sample["Games Played"].max()

sampling_error = parameter - statistic

## 5/15 
## Goal 1: Using simple random sampling, take 100 samples from our WNBA data set, and for each sample measure the average points scored by a player during the 2016-2017 season.

## Goal 2: Display the discrepancy between the parameter of interest (the mean of the PTS column) and the statistics obtained in the previous step.

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')
averages_list = []
parameter = wnba['PTS'].mean()

for i in range(100):
    samples = wnba.sample(n=10, random_state=i)
    averages_list.append(samples['PTS'].mean())

plt.scatter(range(1,101), averages_list)
plt.axhline(parameter)

## 7/14 Stratified Sampling

## Goal 1: Perform stratified sampling: stratify the data set by player position, and then do simple random sampling on every stratum. At the end, use the sample to find which position has the greatest number of points per game.

import pandas as pd

def getkeywithmaxvalue(mydict):
    all_values = list(mydict.values())
    all_keys = list(mydict.keys())
    return all_keys[all_values.index(max(all_values))]

wnba = pd.read_csv('wnba.csv')
wnba['Points Per Game'] = wnba['PTS']/wnba['Games Played']

wnba_guards = wnba[wnba['Pos'] == 'G']
wnba_forwards = wnba[wnba['Pos'] == 'F']
wnba_centers = wnba[wnba['Pos'] == 'C']
wnba_guard_forwards = wnba[wnba['Pos'] == 'G/F']
wnba_forward_centers = wnba[wnba['Pos'] == 'F/C']

strata = [wnba_guards, wnba_forwards, wnba_centers, wnba_guard_forwards, wnba_forward_centers]
points_per_position = {}

for stratum in strata:
    sample = stratum.sample(n=10, random_state=0)
    mean_points = sample['Points Per Game'].mean()
    points_per_position[sample.iloc[0]['Pos']] = mean_points

position_most_points = getkeywithmaxvalue(points_per_position)

print(position_most_points)

## 8/14 Proportional Stratified Sampling

## Figure out the proportions

print(wnba['Games Played'].min())
print(wnba['Games Played'].max())
print(wnba['Games Played'].value_counts(bins = 3, normalize = True) * 100)

## (22.0, 32.0]     72.727273
## (12.0, 22.0]     18.181818
## (1.969, 12.0]     9.090909
## Name: Games Played, dtype: float64

## Perform the stratification

## Goals:

## Perform stratified sampling 100 times. For each of the 100 iterations of a for loop:

## Sample each stratum proportionally. Sample at random: one sample observation from the first stratum, two sample observations from the second, and seven sample observations from the third stratum.
##    random_state should vary from 0 to 99: 0 for the first iteration, 99 for the last iteration.
##    Once you're done with the sampling for the current iteration of the loop, concatenate all the sample observations into one final sample. You can use pd.concat().
##    Compute the mean of the final sample, and append it to a list defined outside the loop. The mean should be for the PTS column.

## Display the entire sampling process.

##    Using plt.scatter(), display the sampling means on a scatter plot. Place the means on the y-axis, and the sample numbers on the x-axis (the numbers should range from 1 to 100 - both endpoints included).
##    Using plt.axhline(), display the population mean for the total points in the form of a horizontal line.

import pandas as pd

wnba = pd.read_csv('wnba.csv')

strata = [wnba[wnba['Games Played']<=12],
          wnba[(wnba['Games Played']<=22) & (wnba['Games Played']>12)],
          wnba[wnba['Games Played']>22]]

sample_means = []

for i in range(100):
    samples1 = strata[0].sample(n=1, random_state=i)
    samples2 = strata[1].sample(n=2, random_state=i)
    samples3 = strata[2].sample(n=7, random_state=i)
    all_samples = pd.concat([samples1, samples2, samples3])
    sample_means.append(all_samples['PTS'].mean())

plt.scatter(range(1,101),sample_means)
plt.axhline(wnba['PTS'].mean())

## Conclusion: not much better than simple random sampling because of a bad choice of strata

## 10/14 Cluster Sampling

## Instructions:

##    Pick four team clusters randomly using the technique we've learned (use random_state = 0).

##    Collect the data from each cluster without sampling the clusters. Create a new DataFrame object that stores the data collected from all clusters.

##    Use the data collected to estimate the mean for the following player attributes:
##        Height;
##        Age;
##        BMI;
##        Total points.

##    Finally, measure the sampling error of your estimates, and assign the errors to the following variables: sampling_error_height, sampling_error_age, sampling_error_BMI, sampling_error_points.


import pandas as pd

wnba = pd.read_csv('wnba.csv')

clusters = pd.Series(wnba['Team'].unique()).sample(n=4, random_state=0)

clusters_data = pd.DataFrame(columns=wnba.columns)

for cluster in clusters:
    current_elements = wnba[wnba['Team'] == cluster]
    clusters_data = clusters_data.append(current_elements)

avg_height = clusters_data['Height'].mean()
avg_age = clusters_data['Age'].mean()
avg_bmi = clusters_data['BMI'].mean()
avg_total_pts = clusters_data['PTS'].mean()

sampling_error_BMI = wnba['BMI'].mean() - avg_bmi
sampling_error_age = wnba['Age'].mean() - avg_age
sampling_error_height = wnba['Height'].mean() - avg_height
sampling_error_points = wnba['PTS'].mean() - avg_total_pts

