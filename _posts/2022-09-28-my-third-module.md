---
layout: post
title: Machine Learning
subtitle: The third module of the course
categories: Modules
tags: [machine learning, ML, Midjourney, K-Mean, Elbow Method, Heat Map, Correlation, Kaggle, Backpropagation, Gradient Descent ]
---

## Summary of the Machine Learning module

On this page I collected notes on my humble progress during the ML module.

## Unit 1. Start with mistake

The ML module starts with the collaborative discussion on the 4th Industrial Revolution. As the tutor noticed (Qazi, 2022), I wrote a text slightly away thematically from the given topic on the failures of an information system, moving forward to the issue of property law in AI, which is closer to the topic of second discussion in the module. In this module I realized that any autonomous machine always starts from the point where it was wrong. And in some fields, it is still hard to develop the ideal system. For example, the most common pitfalls in AI in genomics are distributional differences, dependent examples, leaky preprocessing, unbalanced classes etc., researchers complain that predictive models are not accurate. That potentially chips away the credibility of ML in biomedical research (Whalen at el., 2022). ML facial recognizing systems still make an inappropriate percentage of errors, dealing with different human skin type and gender (Wall, 2019).

## Unit 2. Shine like Heat Map

After diving into the tutorial on Exploratory Data Analysis I can better understand the importance of Heat Maps. At first glance some kinds of correlations look very obvious, for instance, in the case with [House Price Kaggle Competition](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) ‘GrLivArea’, ‘OverallQual’, are strongly connected with ‘SalePrice’. It would be surprising if they are not. However, the program is able to count and compare the level of correlations, and it is fantastic. For ‘YearBuilt’ we may see a relatively weak correlation with 'SalePrice', and it is something new for me. It leads to more explorations. You are welcome to find my attempts in the end of the [code here.](https://github.com/Vasilisalook/ML/blob/main/Unit2MLHeatMaps.ipynb)

## Units 3-4. Сorrelation ≠ Сausation

Basic insight for me is related to the concept of correlation. I have learnt some shock content for a journalist: correlation does not mean causation, although they might exist as parallel lines. For example, the level of health and wealth may almost stick together in some countries, but it does not strictly mean that a healthy life leads to a wealthy life and vice-versa, it needs more research. Another understanding relates to the difference between correlation and regression. Within correlation we can mutually interchange x and y and get the same plot, but if we interchange the x and y in regression – the result will be different.

## Unit 5. The silhouette of elbow

I have heard about customers’ segmentation in the marketing course at my first university. Now I have a chance to discover it more practically. K-Mean clustering is very popular, but the main problem is that the number of clusters should be set by humans. This number may be evaluated by the “elbow method”, however for me it is not obvious in the picture of “elbow” what is an optimal number of clusters. Look at the [picture](https://github.com/Vasilisalook/ML/blob/main/ElbowMethod.jpg): even in the famous Iris dataset it is not clear if there are 2 or 3 would be better. That’s why it would be nice to use the silhouette method as well to be sure.

## Unit 6. Team project #1

![Cover](/assets/images/banners/report.png)

[Airbnb business analysis using Data Science](https://github.com/Vasilisalook/ML/blob/main/GROUP1_Team_AirBnB_Business_Analysis.docx) was the first team-project in the ML module. Through the team discussions I evaluate my ability to write code in Python for such a complex model as predicting competitive prices for rooms based on location. To explain in simple terms what we have done and what it means for business was even harder though. Rolling the Airbnb data of the year 2019 we found a large gap between NYC neighborhoods’ popularity for renting, the average price is $65/night, and realized the Bronx was a leader in proposing shared rooms.

![Sandip Biswas](/assets/images/banners/Sandip.png) ***Sandip Biswas, team member:*** *"Vasilisa has led the teamwork by organising the flow of the projects and how it required to be introduced and taken to a conclusion with supporting artefacts. Vasilisa provided conclusive inferences for the Airbnb project so that each step of data analysis could be used towards the team objective making sure the business case is met. Vasilisa played a vital role in summing up the group discussions by providing explanations with a diagrammatic approach".*

## Unit 7. Money, Love, Adventure

To make the basic idea of Artificial Neural Network clear for myself I created the most primitive ANN – PartnerNN ([schematic illustration of the idea](https://github.com/Vasilisalook/ML/blob/main/PartnerNN.jpg)). The aim was to make it so simple to be able to calculate all the inputs, weights, inner layer nodes and activation functions using just a piece of paper and a pen. PartnerNN is trained to choose or ignore a partner with combination of three inputs he/she/they promise for your shared life: Money, Adventure, Love (True or False for each of them). Please, do not take it seriously, it was created just for main understanding of the backpropagation learning concept. [The code is here.](https://github.com/Vasilisalook/ML/blob/main/PartnerNN.ipynb)

## Unit 8. Gradient understanding

One of the main challenges for me was to catch the purpose of gradient descent. I understand the value of the cost function to get the best prediction for any linear model, for example, house price based on its square in some area. At first, I thought that counting the sum of squared errors is enough to fix wrong predictions, but then I realized that we need to optimize the cost function to the minimum. And that is why we use gradient descent. Everything became clear, when I had [connected two graphs in my mind](https://github.com/Vasilisalook/ML/blob/main/Gradient%20Descent.jpg) – one related to the predicted-actual lines, and another – to the sum of residuals and intercept the y-axes.

## Units 9-10. Team project #2

Through fixing “dying kernel” on my Jupyter Notebook I managed to have 50 epochs for the CIFAR-10 CNN for our second team project with TensorFlow library. For training I used a few examples on [Kaggle website](https://www.kaggle.com/code/vivek468/very-basic-cifar-10-data-cnn/notebook). My Mac was warm and noisy, but he made it. The model of CNN given in Unit 9 as an example was very useful to create our [Summative Assessment about Neural Networks](https://github.com/Vasilisalook/ML#:~:text=Summative%20Assessment%2DNeuralNetworks.pptx)
) by Group-1. You are welcome to find transcript of the presentation and the code [here](https://github.com/Vasilisalook/ML)
). Three of us as a team played with the quality and quantity of the kernels, techniques of dropout and early stopping in order to improve the accuracy of the model. According to the test, we were able to improve it from 68% to 71%.

![Nithya Kanakavelu](/assets/images/banners/Nithya.png) ***Nithya Kanakavelu:*** *"Vasilisa played an active role in the team on both the projects. She made remarkable contributions to the team projects and provided valuable inputs throughout. She contributed towards exploratory data analysis, coding and more for the initial project and in CNN modelling".*


## Additional project: Guide for poets

I have put together [a Midjourney based simple guide](https://github.com/Vasilisalook/vasilisalook.github.io/blob/main/AI-Illustration%20for%20Poets.pdf) to help poets become painters with AI even if they have never heard about Machine Learning. Because the first step is hard one. <br>
 ![AIGuide](/assets/images/banners/AIGuide.png)<br>




