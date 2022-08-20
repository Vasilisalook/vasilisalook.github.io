---
layout: post
title: Practical Training for Numerical Analysis
subtitle: Activities for the second module
categories: Practice
tags: [numerical analysis, data science, R, maths, baye's]
---

## R Data Activities

**subset()** is my favourite function by far - if a table is huge, it allows to choose some segments from data by variables and research them deeply. So, for the dataset "Crime Survey for England and Wales (2013-2014)" I created the first subset for victims of a crime only, and then I used the second level of subsetting, working with victims of 75+ age.<br>
Or we can do it at once using logical operator &: 
> new_subset <- subset(data, status == "victim" **&** age > 75)<br>

**plot()** is my second handy function, it helps to visualise the data. Just a couple of observations: most crimes of that specific group 75+ are happened in urban area and they had been living there more than 20 years (may be there are more chances to be a victim if you are live such a long live and in the same place).

**About Mode in R**

I was surprised that R does not have a standard in-built function to calculate mode. For example, I can easily get the mean and median for some data, writing > median(Health_data$age) or > mean(Health_data$age), but it is not the same with **mode()**. It tells you only the internal storage mode of the object, not the value that occurs the most in its argument.<br>
Two ways to calculate mode of a data set in R:

1.<br>
> getmode <- function(Health_Data$age) {<br>
    ux <- unique(Health_Data$age)<br>
    ux[which.max(tabulate(match(Health_Data$age, ux)))]<br>
}<br>

2.<br>
> age <- (Health_Data$age)<br>
> mode <- age[which.max(age)]<br>
> mode

**NA remover**

In case you are unable to return any value other than NA for mean/mode/median, try this:

> mean(HSE$bmival, trim = 0, na.rm = TRUE)

or remove NA:

> BMI <- na.omit(HSE$bmival)

## Maths Topics

## Python for Numerical Analysis – NumPy Exercises

## Understanding Calculus

## Application of Descriptive Statistics and Visualisation

## Scenario-Based Exercise – 95% Confidence Interval 

## Misinterpretation of Statistical Information

## Baye’s Probability Activity
