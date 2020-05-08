# Statistics Fundamentals

## Definitions

* Sampling Error - difference between the metrics of a population and the metrics of a sample
* Parameter - A metric specific to a population
* Statistic - A metric specific to a sample
* simple random sampling (SRS) - generate random numbers and use them to select a few sample units from the population
* stratified sampling - We can organize our data set into different groups, and then do simple random sampling for every group. each stratified group is also known as a stratum

## Concepts

* When we sample we want to minimize the sampling error as much as possible. We want our sample to mirror the population as closely as possible.
* For this to happen, we need the individuals in our sample to form a group that is similar in structure with the group forming the population. (They should be be representative of their corresponding populations).
* To give every individual an equal chance of being picked, we need to sample randomly.
* `Series.sample()` uses a pseudorandom number generator under the hood. A pseudorandom number generator uses an initial value to generate a sequence of numbers that has properties similar to those of a sequence that is truly random.
* Simple random sampling is not a reliable sampling method when the sample size is small. Because sample means vary a lot around the population mean, there's a good chance we'll get an unrepresentative sample

* How to choose the right strata for sampling:

    1. Minimize the variability within each stratum.
    1. Maximize the variability between strata.
    1. The stratification criterion should be strongly correlated with the property you're trying to measure.

* **Problem**: you want to answer some questions about a population, but the data is scattered in such a way that data collection is either time-consuming or close to impossible. **Solution**: One way is to list all the data sources you can find, and then randomly pick only a few of them to collect data from. Then you can sample individually each of the sources you've randomly picked. This sampling method is called **cluster sampling**, and each of the individual data sources is called a **cluster**.
* When we describe a sample or a population (by measuring averages, proportions, and other metrics; by visualizing properties of the data through graphs; etc.), we do descriptive statistics.
* When we try to use a sample to draw conclusions about a population, we do inferential statistics (we infer information from the sample about the population).
* Statistical workflow
1. Get good data from a data source.
1. Understand how the data is structured and measured
1. Organize the data in comprehensible forms to find patterns.
1. Visualize the patterns.