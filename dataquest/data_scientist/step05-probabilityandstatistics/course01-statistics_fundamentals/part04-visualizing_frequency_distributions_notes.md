# Visualizing Frequency Distributions

## Horizontal Bar Plots

* We can rotate the labels using the rot parameter of Series.plot.bar() method we used. 

```python
wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.bar(rot = 45)
```

* Add a title

```python
wnba['Pos'].value_counts().plot.barh(title = 'Number of players in WNBA by position')
```

| Scale of measurement | Graph Types |
|---|---|
| Nominal | Bar, Pie |
| Ordinal | Bar, Pie |
| Interval | Histogram |
| Ratio | Histogram |

* The main difference is that in the case of a histogram there are no gaps between bars, and each bar represents an interval, not a single value.
* For bar plots we add gaps because in most cases we don't know whether the unique values of ordinal variables are adjacent to one another in the same way as two class intervals are. It's safer to assume that the values are not adjacent, and add gaps.
* For nominal variables, values can't be numerically adjacent in principle, and we add gaps to emphasize that the values are fundamentally distinct.

## Skewed Distributions

* In a skewed distribution:
    * The values pile up toward the end or the starting point of the range, making up the body of the distribution.
    * Then the values decrease in frequency toward the opposite end, forming the tail of the distribution.
    * If the tail points to the left, then the distribution is said to be left skewed. When it points to the left, the tail points at the same time in the direction of negative numbers, and for this reason the distribution is sometimes also called negatively skewed. 
    * If the tail points to the right, then the distribution is right skewed. The distribution is sometimes also said to be positively skewed because the tail points in the direction of positive numbers.
* If the shape of the histogram is symmetrical, then we say that we have a symmetrical distribution.
* A very common symmetrical distribution is one where the values pile up in the middle and gradually decrease in frequency toward both ends of the histogram. This pattern is specific to what we call a normal distribution (also called Gaussian distribution).
* Another common symmetrical distribution is one where the values are distributed uniformly across the entire range. This pattern is specific to a uniform distribution.