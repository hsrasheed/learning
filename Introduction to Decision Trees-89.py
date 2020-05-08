## 3. Converting Categorical Variables ##

def convert_categorical_vars(df):
    text_cols = df.select_dtypes(include=['object']).columns
    for col in text_cols:
        cat_col = pandas.Categorical(df[col])
        df[col] = cat_col.codes
        
# Convert a single column from text categories to numbers
#col = pandas.Categorical(income["workclass"])
#income["workclass"] = col.codes
#print(income["workclass"].head(5))
convert_categorical_vars(income)

## 5. Creating Splits ##

private_incomes = income[income['workclass'] == 4]
print("Total private incomes: "+str(len(private_incomes)))
public_incomes = income[income['workclass'] != 4]
print("Total public incomes: "+str(len(public_incomes)))# Enter your code here


## 9. Overview of Data Set Entropy ##

import math

def compute_entropy(df,column):
    col_unique_vals = list(df[column].value_counts().index)
    total_rows = len(df)
    entropy = 0
    for i in col_unique_vals:
        value_instances = len(df[df[column] == i])
        entropy += (value_instances/total_rows) * math.log((value_instances/total_rows), 2)
    return -entropy

# We'll do the same calculation we did above, but in Python
# Passing in 2 as the second parameter to math.log will take a base 2 log
#entropy = -(2/5 * math.log(2/5, 2) + 3/5 * math.log(3/5, 2))
#print(entropy)
total_income_number = len(income)
high_income_number = len(income[income['high_income'] == 1])
low_income_number = len(income[income['high_income'] == 0])
income_entropy = compute_entropy(income,'high_income')
print(income_entropy)

## 11. Information Gain ##

import numpy

def calc_entropy(column):
    """
    Calculate entropy given a pandas series, list, or numpy array.
    """
    # Compute the counts of each unique value in the column
    counts = numpy.bincount(column)
    # Divide by the total column length to get a probability
    probabilities = counts / len(column)
    
    # Initialize the entropy to 0
    entropy = 0
    # Loop through the probabilities, and add each one to the total entropy
    for prob in probabilities:
        if prob > 0:
            entropy += prob * math.log(prob, 2)
    
    return -entropy

# Verify that our function matches our answer from earlier
entropy = calc_entropy([1,1,0,0,1])
print(entropy)

information_gain = entropy - ((.8 * calc_entropy([1,1,0,0])) + (.2 * calc_entropy([1])))
print(information_gain)

median_age = income['age'].median()
left_branch = income[income['age']<=median_age]
right_branch = income[income['age']>median_age]
age_information_gain = calc_entropy(income['high_income']) - (len(left_branch)/len(income)*calc_entropy(left_branch['high_income']) + len(right_branch)/len(income)*calc_entropy(right_branch['high_income']))

## 12. Finding the Best Split ##

def calc_information_gain(data, split_name, target_name):
    """
    Calculate information gain given a data set, column to split on, and target
    """
    # Calculate the original entropy
    original_entropy = calc_entropy(data[target_name])
    
    # Find the median of the column we're splitting
    column = data[split_name]
    median = column.median()
    
    # Make two subsets of the data, based on the median
    left_split = data[column <= median]
    right_split = data[column > median]
    
    # Loop through the splits and calculate the subset entropies
    to_subtract = 0
    for subset in [left_split, right_split]:
        prob = (subset.shape[0] / data.shape[0]) 
        to_subtract += prob * calc_entropy(subset[target_name])
    
    # Return information gain
    return original_entropy - to_subtract

# Verify that our answer is the same as on the last screen
print(calc_information_gain(income, "age", "high_income"))

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

information_gains = []

for col in columns:
    information_gains.append(calc_information_gain(income, col, "high_income"))
    
highest_gain = columns[information_gains.index(max(information_gains))]
print("Highest gain from split: "+ highest_gain)