# Frequency Distributions

* frequency distribution table, or, shorter, frequency table or frequency distribution - select a variable, count how many times each unique value occurs, and represent the frequencies (the number of times a unique value occurs) in a table

## Proportions and Percentages

* Because proportions and percentages are relative to the total number of instances in some set of data, they are called **relative frequencies**. In contrast, the frequencies we've been working with so far are called **absolute frequencies** because they are absolute counts and don't relate to the total number of instances.

## Percentiles and Percentile Ranks

* A percentile rank of a value x in a frequency distribution is given by the percentage of values that are equal or less than x. In our last exercise, x=23 , and the fact that 23 has a percentile rank of 19% means that 19% of the values are equal to or less than 23.

In this context, the value of 23 is called the 19th percentile. If a value is the 19th percentile, it means that 19% of all the values in the distribution are equal to or less than .

```python
from scipy.stats import percentileofscore
print(percentileofscore(a = wnba['Age'], score = 23, kind = 'weak'))
print(100 - percentileofscore(wnba['Age'], 29, kind = 'weak'))
```

## Grouped Frequency Distribution Tables

* For some frequency distributions, there's a lot of granularity -- for this reason it's not easy to find patterns. If the variable is measured on an interval or ratio scale, a common solution to this problem is to group the values in equal intervals.

```python
# Fortunately, pandas can handle this process gracefully. We only need to make use of the bins parameter of Series.value_counts(). We want ten equal intervals, so we need to specify bins = 10:

print(wnba['Weight'].value_counts(bins = 10).sort_index())
```

* Because we group values in a table to get a better sense of frequencies in the distribution, the table we generated above is also known as a grouped frequency distribution table. Each group (interval) in a grouped frequency distribution table is also known as a class interval.

## Readability for Grouped Frequency Tables

Strategy for making manual intervals for a grouped frequency table:

```python
#We start with creating the intervals using the pd.interval_range() function:
intervals = pd.interval_range(start = 0, end = 600, freq = 100)

# Next, we create a new Series using the intervals as indices, and, for now, 0 as values:
gr_freq_table = pd.Series([0,0,0,0,0,0], index = intervals)

# If the value belongs to an interval:

#    We update the counting for that interval in gr_freq_table by adding 1.
#    We exit the inner loop over the intervals with break because a value can belong to one interval only, and it makes no sense to continue the loop (without using break, we'll get the same output but we'll do many redundant iterations).

for value in wnba['PTS']:
    for interval in intervals:
        if value in interval:
            gr_freq_table.loc[interval] += 1
            break
print(gr_freq_table)

```

