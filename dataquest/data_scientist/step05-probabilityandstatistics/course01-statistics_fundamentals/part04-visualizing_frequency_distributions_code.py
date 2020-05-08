# Create a horizontal bar plot to visualize the distribution of the Exp_ordinal variable.

#    Generate a frequency table for the Exp_ordinal variable.
#    Sort the table by unique labels in an ascending order.
#    Use the Series.plot.barh() method to generate the horizontal bar plot.
#    Add the following title to the plot: Number of players in WNBA by level of experience.


wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.barh(title = 'Number of players in WNBA by level of experience')

# 5/13 Use the Series.plot.pie() method to generate the pie plot.

#    Use the figsize parameter to specify a width and a height of 6 inches each.
#    Use the autopct parameter to have percentages displayed with a precision of 2 decimal places.
#    Add the following title to the plot: Percentage of players in WNBA by level of experience.
#    Remove the Exp_ordinal label.

wnba['Exp_ordinal'].value_counts().plot.pie(figsize = (6,6), autopct = '%.2f%%', title='Percentage of players in WNBA by level of experience')
plt.ylabel('')

# 6/13 The Statistics behind histograms

wnba['PTS'].plot.hist()

# 7/13 Histograms as modified bar plots

from numpy import arange

print(wnba['Games Played'].describe())

wnba['Games Played'].plot.hist()

# 8/13 Binning for Histograms

wnba['Games Played'].plot.hist(range=(1,32), bins=8, title='The distribution of players by games played')
plt.xlabel('Games played')

# 10/13

## 

wnba['AST'].plot.hist(bins=10)
assists_distro = 'right skewed'

wnba['FT%'].plot.hist(bins=10)
ft_percent_distro = 'left skewed'