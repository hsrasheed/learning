# 1/11
# For each segment, generate a frequency distribution table for the Pos variable.

#    For the rookies segment, assign the frequency distribution table to a variable named rookie_distro.
#    For the little experience segment, assign the table to little_xp_distro.
#    For the experienced segment, assign the table to experienced_distro.
#    For the very experienced segment, assign the table to very_xp_distro.
#    For the veterans segment, assign the table to veteran_distro.


rookies = wnba[wnba['Exp_ordinal'] == 'Rookie']
little_xp = wnba[wnba['Exp_ordinal'] == 'Little experience']
experienced = wnba[wnba['Exp_ordinal'] == 'Experienced']
very_xp = wnba[wnba['Exp_ordinal'] == 'Very experienced']
veterans =  wnba[wnba['Exp_ordinal'] == 'Veteran']

rookie_distro = rookies['Pos'].value_counts()
print(rookie_distro)
little_xp_distro = little_xp['Pos'].value_counts()
print(little_xp_distro)
experienced_distro = experienced['Pos'].value_counts()
print(experienced_distro)
very_xp_distro = very_xp['Pos'].value_counts()
print(very_xp_distro)
veteran_distro = veterans['Pos'].value_counts()
print(veteran_distro)

# 2/11

# Usng sns.countplot(), generate a grouped bar plot similar to the one above.
#        Place the Exp_ordinal variable on the x-axis.
#        Generate the bar plots for the Pos variable. The data set is stored in wnba variable.
#        Using the order parameter of sns.countplot(), order the values on the x-axis in ascending order. The order parameter takes in a list of strings, so you should use order = ['Rookie', 'Little experience', ..........].
#        Using the hue_order parameter, order the bars of each bar plot in ascending alphabetic order. hue_order takes in a list of strings, so you can use hue_order = ['C', 'F', ......].

import seaborn as sns
sns.countplot(x = 'Exp_ordinal', hue = 'Pos', data = wnba, 
order = ['Rookie', 'Little experience', 'Experienced', 'Very experienced', 'Veteran'], 
hue_order = ['C', 'F', 'F/C','G','G/F'])

# 3/11
## 

#    Generate a grouped bar plot to confirm or reject our hypothesis. Using sns.countplot():
##        Place the age_mean_relative variable on the x-axis. The age_mean_relative and min_mean_relative are already defined.
##        Generate the frequency distributions for the min_mean_relative variable.

#    Analyze the graph and determine whether the data confirms or rejects our hypothesis. If it's a confirmation assign the string 'confirmation' to a variable named result. If it's a rejection, assign the string 'rejection' to the variable result.

import seaborn as sns

def make_age_ordinal(row):
    if row['Age'] >= 27:
        return 'old'
    else:
        return 'young'

def make_min_ordinal(row):
    if row['MIN'] >= 497:
        return 'average or above'
    else:
        return 'below average'

wnba['age_mean_relative'] = wnba.apply(make_age_ordinal, axis=1)
## lamba method
# wnba['age_mean_relative'] = wnba['Age'].apply(lambda x: 'old' if x >= 27 else 'young')
wnba['min_mean_relative'] = wnba.apply(make_min_ordinal, axis=1)
## lambda method
# wnba['min_mean_relative'] = wnba['MIN'].apply(lambda x: 'average or above' if x >= 497 else 'below average')
#wnba.head()
sns.countplot(x = 'age_mean_relative', hue = 'min_mean_relative' , data=wnba)
result = 'rejection'

