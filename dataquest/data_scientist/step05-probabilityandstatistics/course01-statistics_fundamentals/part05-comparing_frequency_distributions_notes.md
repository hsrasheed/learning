# Comparing Frequency Distributions

## Comparing Frequency Distributions

* Let's say we're interested in analyzing how the distribution of the Pos variable (player position) varies with the level of experience. In other words, we want to determine, for instance, what are the positions on the court that rookies play most as, and how do rookies compare to veterans with respect to positions on the field.

* Here's a series of steps we can take to achieve that:

* Segment the players in the data set by level of experience.
* For each segment, generate a frequency distribution table for the Pos variable.
* Analyze the frequency distributions comparatively.

## Grouped Bar Plots

* In the code snippet below, we will:

* Import the seaborn module with the alias sns.
* Generate the plot with sns.countplot(). We'll use the following parameters for this function:
    * x — specifies as a string the name of the column we want on the x-axis. We'll place the Exp_ordinal column on the x-axis.
    * hue — specifies as a string the name of the column we want the bar plots generated for. We want to generate the bar plots for the Pos column.
    * data - specifies the name of the variable which stores the data set. We stored the data in a variable named wnba.

```python
import seaborn as sns
sns.countplot(x = 'Exp_ordinal', hue = 'Pos', data = wnba)
```